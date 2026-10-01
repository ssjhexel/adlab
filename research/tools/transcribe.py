"""Timestamped transcripts for every ad in competitor_ads/.

HuggingFace is blocked in the cloud sandbox, so this uses sherpa-onnx with
models from its GitHub releases:
  pip install sherpa-onnx numpy
  curl -LO https://github.com/k2-fsa/sherpa-onnx/releases/download/asr-models/sherpa-onnx-whisper-small.en.tar.bz2 && tar xjf sherpa-onnx-whisper-small.en.tar.bz2
  curl -LO https://github.com/k2-fsa/sherpa-onnx/releases/download/asr-models/silero_vad.onnx
Run from the directory holding the models: python3 transcribe.py <repo>/competitor_ads <out_dir>
Files are numbered C01..Cnn in sorted filename order.
"""
import glob, os, subprocess, sys
import numpy as np, sherpa_onnx

src, out = sys.argv[1], sys.argv[2]
d = "sherpa-onnx-whisper-small.en/"
rec = sherpa_onnx.OfflineRecognizer.from_whisper(
    encoder=d + "small.en-encoder.int8.onnx", decoder=d + "small.en-decoder.int8.onnx",
    tokens=d + "small.en-tokens.txt", num_threads=4, tail_paddings=800)
cfg = sherpa_onnx.VadModelConfig()
cfg.silero_vad.model = "silero_vad.onnx"
cfg.silero_vad.min_silence_duration = 0.25
cfg.silero_vad.max_speech_duration = 12
cfg.sample_rate = 16000
os.makedirs(out, exist_ok=True)
for i, f in enumerate(sorted(glob.glob(os.path.join(src, "*.mp4"))), 1):
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", f, "-ac", "1", "-ar", "16000", "-f", "s16le", "-"],
                         capture_output=True).stdout
    a = np.frombuffer(raw, dtype=np.int16).astype(np.float32) / 32768
    vad = sherpa_onnx.VoiceActivityDetector(cfg, buffer_size_in_seconds=120)
    for k in range(0, len(a), 512):
        vad.accept_waveform(a[k:k + 512])
    vad.flush()
    lines = []
    while not vad.empty():
        seg = vad.front
        st = seg.start / 16000
        s = rec.create_stream()
        s.accept_waveform(16000, np.array(seg.samples))
        rec.decode_stream(s)
        lines.append(f"[{st:5.1f}-{st + len(seg.samples) / 16000:5.1f}] {s.result.text.strip()}")
        vad.pop()
    open(os.path.join(out, f"C{i:02d}.txt"), "w").write("\n".join(lines) + "\n")
    print(f"C{i:02d}", os.path.basename(f))
