# Concept 01 "PART THE FUR": Music (Suno)

Instrumental bed for the 50s multi-shot cut (V1 and V2). Seedance generates the VO, so the music must sit **under a voice**: no vocals, no busy lead melody in the 1–4 kHz speech range, and a clear lift at the transformation.

**Emotional map of the ad → music**
| Ad time | Beat | Music |
|---|---|---|
| 0–12 | Problem: scratching, sleepless night | Sparse, tense-but-tender: muted plucks, soft low pad, light ticking pulse |
| 12–27 | Korean expertise + spray + science | Steady, curious, clean: add a soft kick and a gentle bell/marimba motif |
| 27–39 | Relief + Day 1→5 transformation | **The lift:** chords open up, warm bass enters, light claps; this is the emotional peak |
| 39–50 | Happy dog, sleep, cat, CTA | Bright, warm, resolved; full but soft; clean ending on the final word |

---

## Prompt 1: main (recommended)

**Style of Music** (paste into Suno's style field):
```
instrumental, warm uplifting acoustic pop, 100 bpm, soft felt piano, muted acoustic guitar plucks, gentle marimba, light claps, warm sub bass, airy pads, hopeful, tender to joyful build, clean modern ad music, no vocals
```

**Lyrics field** (structure tags only; this drives the arc):
```
[Instrumental]
[Intro: sparse felt piano and muted guitar plucks, tense and tender, quiet]
[Verse: soft ticking pulse, low pad, steady and curious, light marimba motif]
[Build: gentle kick enters, rising]
[Chorus: lift, open warm chords, bass and light claps, hopeful and joyful]
[Outro: bright, warm, resolved, clean ending]
[End]
```
- **Settings:** Instrumental ON. Generate 4–8 versions and pick the one whose "Chorus" lift lands closest to 27s once trimmed. Suno tracks run longer than 50s, so cut in the edit from the intro into the chorus at the transformation.

## Prompt 2: alternate, more "K-beauty" premium feel
```
instrumental, minimal K-pop inspired lo-fi, 95 bpm, soft electric piano, plucked gayageum accents, warm sub bass, crisp light percussion, glassy bells, clean, premium skincare commercial, calm to bright build, no vocals
```
Use the same Lyrics-field structure. The gayageum (Korean zither) quietly supports the "Korean" story; keep it as accents, not the lead.

## Prompt 3: alternate, punchy UGC / TikTok energy (pairs with V2's faster VO)
```
instrumental, upbeat feel-good pop, 112 bpm, bouncy muted guitar, finger snaps, playful pizzicato, warm bass, bright synth pluck lead, positive, energetic, social media ad music, no vocals
```

---

## Mix notes
- Music ducked **about 18 dB under the VO**; let it rise about 6 dB in the gaps and at the transformation (27–37s) and the end card.
- High-pass the music around 120 Hz under the VO if the voice sounds muddy, and dip 2–4 kHz by 2–3 dB so it doesn't mask speech.
- Keep foley (scratching, "tss" spray, sigh, tag jingle) **above** the music. It sells the realism.
- End on the last word of the CTA with a short ring-out, no fade to silence before the end card is readable.
- Hook test versions: the same music for every hook so only the hook differs.
