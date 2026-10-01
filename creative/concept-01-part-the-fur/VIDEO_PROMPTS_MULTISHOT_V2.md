# Concept 01 "PART THE FUR" — Multi-Shot Video Prompts **V2: aggressive first pass** (Seedance 2.0 / Higgsfield)

> **V2 = strongest-possible script, modeled on what the competitor runs.** Compliance is intentionally relaxed for this pass. Lines marked ⚠ below need a claims review before spend (see "Compliance cleanup list" at the end). V1 (`VIDEO_PROMPTS_MULTISHOT.md`) is the claims-safe version. Visuals, timing, references and blocks are identical to V1; only the voiceover and its delivery changed.

## What changed vs. V1 (and which competitor pattern it copies)
| Beat | V1 | V2 | Pattern |
|---|---|---|---|
| Hook | "If your dog keeps scratching the same spot… part the fur." | "Your dog keeps scratching the same spot? Part the fur." | Direct-address question + command (C03, C11) |
| Cycle | "…and round it went." | "Licking, biting, scratching… it never stops." | Behavior list (C01, C03, C07) |
| Turn | "So I stopped guessing…" | "Until I found this." | Classic UGC product reveal (C04 "That's when I started using…") |
| Product promise | "…and tried Korean pet dermatology." | "The Korean mist that stops the itch fast." | Benefit + speed (C07/C08 "fast soothing care") |
| Proof | — | "Officially registered in Korea." | Authority the competitor doesn't have |
| Safety | "No steroids. No fragrance. Lick-safe." | "No steroids. Totally lick-safe." | C01/C06 "safe even if they lick" |
| Demo + mechanism | "Three to five sprays on dry skin." / "…supporting its natural barrier." | "Three sprays… and the itch is gone." / "Soaks in instantly. Calms the itch. Rebuilds damaged skin." ⚠ | C06 "calms inflammation at the source… rebuilds the skin barrier" |
| Relief | "No bath. No rinse. Nothing to rub in." + "From the very first spray…" | "Instant, cooling relief." + "Seconds later… he finally stopped scratching." ⚠ | C06 "it cools the inflamed skin", C07/C08 "in just 8 seconds" |
| Result | "By day three… the redness had calmed… by day five, his skin looked like his again." | "Before… Day one, redness calming. Day three, flakes gone. Day five… brand-new, healthy skin." + "Even those licked-raw paws… calm again." ⚠ | C01 "recovers within a week", C06 "in just days… the angry red spots fade" |
| Payoff | "Less scratching. Less licking." | "No more scratching. No more licking." ⚠ | C06 "the constant licking stops" |
| CTA | "Scratch less, lick less, live more. Tap below…" | "Every pet owner needs one. Tap below… on sale today, while stock lasts." | C07 "Every pet owner should have one", C01 "Stock is limited" |

Voice: same narrator, but **brisk and emotive at ~190 wpm**, matching the competitor's pace (160–215 wpm) instead of V1's unhurried read.

---


**The fast route.** The whole 50s ad comes from **5 generations** instead of ~24. Each block is a 10–12s **controlled multi-shot sequence**, so Seedance makes the hard cuts itself, following the shot list in the prompt. The **macro science dive is generated on its own** (Block C).

The shot-by-shot route (`VIDEO_PROMPTS.md`) is still the fallback for any single shot that keeps failing in a block.

---

## Voiceover direction: why this voice

**Choice: a first-person "owner who found the fix" voice. Female, early 30s, warm, conversational American English, close-mic, unpolished.**
- **Who's watching:** the buyers are mostly women aged 28–55 who own an itchy dog. A peer telling her own story reads as a recommendation. An announcer reads as an ad, and the conversion job here is trust.
- **What the competitors do:** 4 of the 8 competitor spray ads already use first-person owner voiceover ("that's why I keep…", "my dog used to…"), the most common voice choice in the set. We keep that, but make it more human: real pauses, breath, and a relieved smile instead of a rushed delivery at 200 words per minute.
- **How it fits the script:** the lines are written in the first person ("Until I found this.", "for both of us"). A male announcer would break them.
- **Test later:** once Concept 01 has a winning hook, a calm Korean-accented female expert voice for the authority lines (Block B) is a good second voice test.

## How this route works

| Block | Ad time | Length | Shots | First frame | References |
|---|---|---|---|---|---|
| **A — Problem** | 0.0–12.0 | 12s | 6 | **KF-G01** (lesion master) | @WESTIE, @OWNER, @ATOKONG |
| **B — Authority + Demo** | 12.0–24.0 | 12s | 6 | none (text-led) | @WESTIE, @OWNER, @ATOKONG, @RESEARCHER, @PATCH |
| **C — Science dive** | 24.0–27.0 | 3s | 2 (match cut) | **KF-G12** → last **KF-G12-SCI-END** | — *(3s prompt below)* |
| **D — Relief + Proof** | 27.0–39.0 | 12s | 7 | none | @WESTIE, @OWNER, @ATOKONG, @PATCH, @DAY5 |
| **E — Payoff + End** | 39.0–50.0 | 11s | 4 | none | @WESTIE, @CAT, @OWNER, @ATOKONG |

**Images you still need (7 instead of ~30):**
1. `@WESTIE`: REF-WESTIE-1 (+ REF-WESTIE-2 if your UI allows a second image per tag)
2. `@OWNER`: REF-OWNER
3. `@CAT`: REF-CAT
4. `@ATOKONG`: the real packshot (`product/images/atokong_packshot_bottle_box.jpg`)
5. `@RESEARCHER`: KF-G07B (locks the Korean researcher's identity)
6. `@PATCH`: KF-G01 (locks the lesion's look, location and the hands' framing for the "before" state)
7. `@DAY5`: KF-G15-D5 (the calm day-5 skin, an edit of KF-G01)

Plus the two science-dive frames for Block C (KF-G12 and KF-G12-SCI-END).

**Settings:** 9:16 · 1080p · duration as listed · multi-reference mode · audio on (natural foley only).

**Tips for multi-shot**
- Generate **3–4 takes per block**. You can mix shots across takes in the edit, since every block uses the same identity references.
- **Every generation is used whole, at the exact length asked for.** No 5s-per-shot overshoot and no trimming down to a "stable middle". Each block's shot timings add up exactly to its generation length, and the blocks butt-join into the final 50.0s cut. If a take drifts, re-roll the block rather than trimming it.
- The VO lines are written to fit each shot's duration. Small gaps are breathing room, not dead air.
- **Seedance generates the voiceover.** Every prompt contains the same NARRATOR VOICE block word for word, plus the lines timed to the shots. Music, captions, day counters and the end card still go on in post.
- **Voice consistency across 5 generations is the main risk.** If your Seedance UI accepts an audio reference, generate Block A first, pick the take whose voice you like, and upload ~5s of it as the voice reference for Blocks B–E. If a block's voice drifts, re-roll it. As a last resort, regenerate just that block's lines with a TTS clone of the Block A voice.
- If the day-counter shots in Block D change framing between cuts, generate them separately with G15 in `VIDEO_PROMPTS.md` (first-frame route). That is the most consistency-sensitive moment in the ad.

---

## BLOCK A — Problem (0.0–12.0)

**VO for this block (spoken by Seedance; ad timecode = block time):**

| Shot | Block time | VO |
|---|---|---|
| A1 | 0.0–3.2 | "Your dog keeps scratching the same spot? Part the fur." |
| A2 | 3.2–5.0 | "That's what keeps him up all night." |
| A3 | 5.0–6.6 | "And every scratch makes it worse." |
| A4 | 6.6–8.4 | "Licking, biting, scratching… it never stops." |
| A5 | 8.4–10.2 | "Until I found this." |
| A6 | 10.2–12.0 | "The Korean mist that stops the itch fast." |

**Hook swaps:** generate a standalone hook (see "Block A hook variants" below) and lay it over 0.0–3.2 of this block.

```
SCENE CONTEXT
A small white terrier's irritated skin is revealed under his fur, we see the itch keeping him and his owner awake, and his owner picks up a Korean pet skin mist.

ACTIVE REFERENCES
@WESTIE: 5-year-old male West Highland White Terrier, compact 8 kg body, coarse white coat with creamy tips, brown leather collar with a small round brass tag, irritated patch on his left flank just forward of the left hip, rust-brown saliva staining on his right front paw. 100% matches the reference.
@OWNER: early-30s woman seen only as hands and forearms, short unpolished nails, thin gold band on the right ring finger, oatmeal knit sleeves. 100% matches the reference.
@ATOKONG: small 30 ml white round spray bottle, about 10 cm tall, white pump nozzle, clear dome cap, orange cartoon-dog label. Shape, size and label design 100% match the reference.

FORMAT MODE
Controlled multi-shot sequence, 12 seconds, six shots, HARD CUTS only at 3.2, 5.0, 6.6, 8.4 and 10.2 seconds. No fades, no dissolves, no transition effects. Every shot opens with its subject already in frame. Real-time motion except shot A3.

SHOT A1 — 0:00 to 0:03.2 — HOOK REVEAL
First frame matches the start image: overhead close-up of @WESTIE lying on his right side on a cream wool rug, left flank up; both @OWNER hands at the top of frame already spreading the white fur open in a V over the irritated patch at frame center. The patch is about 6 cm wide with irregular edges, blotchy pink-to-red skin, fine scratch marks, dry white flakes at the hair roots and thinned broken fur. Dry and matte, no blood.
Optics: 29° diagonal field of view, close detail framing, phone 35 cm above the coat.
Camera: handheld phone held from above, operator breath, slow push-in toward the patch.
Action: the fingers spread the fur 2 cm wider; stray hairs spring back; the skin twitches once under the fingers; the flank rises with one breath.
Light: soft window daylight from screen-left.

SHOT A2 — 0:03.2 to 0:05.0 — NIGHT SCRATCHING
First frame: bedroom at night; @WESTIE already sitting on a round grey dog bed in the right half of frame at the foot of a double bed, body facing screen-left, left hind leg raised mid-scratch against his left flank. A woman lies in the bed in soft focus in the background.
Optics: 47° diagonal field of view, standard normal lens character, camera on the floor 1.5 meters away.
Camera: static on the floor with tiny handheld micro-movement.
Action: rapid, rhythmic scratching, about four strokes per second, collar tag bouncing; in the background the woman lifts her head off the pillow.
Light: thin stripes of cool blue moonlight from window blinds at screen-right; low-light phone exposure with visible noise; no fill light.

SHOT A3 — 0:05.0 to 0:06.6 — CLAWS MACRO, SLOW MOTION
First frame: extreme close-up of @WESTIE's hind claws already pressed into the white fur over the irritated patch, dark background.
Optics: 18° diagonal field of view, telephoto macro, razor-thin focus on the claws and skin.
Camera: locked off. Slow motion, quarter speed.
Action: the claws drag slowly through the fur across the patch; a small cloud of fine white skin flakes lifts and drifts through a thin beam of warm lamp light.
Light: one sliver of warm lamp light from screen-right; everything else in shadow.

SHOT A4 — 0:06.6 to 0:08.4 — PAW LICKING
First frame: daytime, @WESTIE already lying on the cream rug, head lowered, tongue at his right front paw at frame center-bottom; rust-brown staining on the white toe fur, pink skin between the toes.
Optics: 47° diagonal field of view, standard normal lens character, camera at rug level 1 meter away, three-quarter front angle.
Camera: handheld at floor level, slight push-in.
Action: repetitive licking between the toes, then a quick nibble at the base of the toes.
Light: soft window daylight from screen-left.

SHOT A5 — 0:08.4 to 0:10.2 — PICKING UP THE PRODUCT
First frame: close-up of @ATOKONG standing upright on a sunlit white shelf at frame center, a small trailing plant at screen-left; @OWNER's right hand entering from screen-right.
Optics: 29° diagonal field of view, close detail framing, camera 60 cm from the shelf at chest height.
Camera: handheld, small tilt-up following the bottle.
Action: the fingers wrap fully around the small bottle and lift it 15 cm, turning the label toward camera.
Light: morning sun from screen-left across the shelf.

SHOT A6 — 0:10.2 to 0:12.0 — THE SNIFF
First frame: living room, cream rug; @WESTIE sitting at screen-right facing screen-left; @OWNER's right hand at screen-left holding @ATOKONG at his nose height, 15 cm from his nose, label facing camera.
Optics: 47° diagonal field of view, standard normal lens character, camera low at 70 cm, three-quarter angle.
Camera: handheld, fixed framing.
Action: @WESTIE stretches forward and sniffs the nozzle, ears forward, then licks his nose once and looks up toward the woman off-screen left.
Light: window daylight from screen-left.

CONTINUITY
Same dog in every shot: same face, size, coat, brown collar and brass tag. The irritated patch is always on the left flank. The owner's gold ring is always on the right hand. In daytime living-room shots the window is always at screen-left. The bottle is always the same small 30 ml bottle; it never grows in size.

PHYSICS
Coarse terrier fur bends and springs back along its growth direction. Skin moves slightly under finger pressure. Scratching legs and licking heads move with real weight. Skin flakes are tiny and fall with gravity, never glowing. The bottle has real weight in the hand.

AUDIO
Natural foley only, matched to each shot: soft fur rustle and breathing (A1); rhythmic collar-tag jingle and thumping (A2); slowed dry scratching (A3); wet licking (A4); a soft clink as the bottle leaves the shelf (A5); quick sniffs and a faint tag jingle (A6). No music.

VOICEOVER
NARRATOR VOICE (identical in every line): one off-screen female narrator, early 30s, natural American English, warm and conversational, like a real dog owner telling a close friend what finally worked. Not an announcer, not salesy, no radio voice. Close, intimate microphone, clean and dry with light room tone, soft natural breaths. Brisk and punchy, about 190 words per minute, with short pauses only at each ellipsis; real emotion: frustrated on the problem lines, relieved and excited on the results, confident on the call to action. Nobody on screen speaks and there is no lip movement. Only the quoted lines are spoken, with no extra words or ad-libs.
0:00.2 to 0:03.0 "Your dog keeps scratching the same spot? Part the fur."
0:03.3 to 0:04.9 "That's what keeps him up all night."
0:05.1 to 0:06.6 "And every scratch makes it worse."
0:06.7 to 0:08.3 "Licking, biting, scratching… it never stops."
0:08.5 to 0:10.1 "Until I found this."
0:10.3 to 0:11.8 "The Korean mist that stops the itch fast."
Voice sits clearly on top; foley ducks under the voice.

POSITIVE CONSTRAINTS
Real smartphone footage texture in every shot, natural unretouched detail. One dog in every dog shot; one or two hands only. No subtitles, no on-screen text, no glow effects. The lesion never bleeds, glows or changes shape.
```

### Block A hook variants: standalone single-shot prompts
Each hook is its own 4s single-shot generation. Cut it at 3.2s and lay it over 0.0–3.2 of Block A (replacing A1). Block A from 3.2s onward is unchanged, so one Block A generation serves every hook. Each prompt carries the same NARRATOR VOICE block, so the voice matches the rest of the ad.

### H1 — Part the fur (control)
Refs: @WESTIE, @OWNER · first frame KF-G01 · **4s** (use 0.0–3.2 over Block A's A1; Block A continues from 3.2)
🎙 VO: "Your dog keeps scratching the same spot? Part the fur."
```
SCENE CONTEXT
A woman parts the white coat on her dog's left flank and reveals the irritated, flaky patch he keeps scratching.

ACTIVE REFERENCES
@WESTIE: 5-year-old male West Highland White Terrier, compact 8 kg body, coarse white coat with creamy tips, brown leather collar with a small round brass tag, irritated patch on his left flank just forward of the left hip, rust-brown saliva staining on his right front paw. 100% matches the reference.
@OWNER: early-30s woman seen only as hands and forearms, short unpolished nails, thin gold band on the right ring finger, oatmeal knit sleeves. 100% matches the reference.

FIRST FRAME AND SPATIAL BLOCKING
Matches the start image: overhead close-up of @WESTIE lying on his right side on a cream wool rug, left flank up; both @OWNER hands at the top of frame spreading the fur open in a V over the patch at frame center. The patch is about 6 cm wide with irregular edges, blotchy pink-to-red skin, fine scratch marks, dry white flakes at the hair roots, thinned broken fur; dry and matte, no blood. The first visible frame already contains the subject in position. No empty establishing frame, no delayed reveal.

FORMAT MODE
Single continuous take, 4 seconds. Real-time motion.

OPTICS
29° diagonal field of view, close detail framing, phone 35 cm above the coat. Patch razor-sharp, rug soft at the edges.

CAMERA
Handheld phone held from above: operator breath, micro-settling, slow push-in toward the patch.

ACTION TIMING
0:00 to 0:02 The fingers spread the fur 2 cm wider; stray hairs spring back.
0:02 to 0:04 The skin twitches once under the fingers; the flank rises with one breath; the push-in continues.

PHYSICS
Coarse fur bends and springs back along its growth direction; skin moves slightly under finger pressure.

LIGHTING
Soft window daylight from screen-left; fingers cast a soft shadow at screen-right.

AUDIO
Soft fur rustle, the dog's breathing, one faint collar-tag jingle. No music.
VOICEOVER
NARRATOR VOICE (identical in every line): one off-screen female narrator, early 30s, natural American English, warm and conversational, like a real dog owner telling a close friend what finally worked. Not an announcer, not salesy, no radio voice. Close, intimate microphone, clean and dry with light room tone, soft natural breaths. Brisk and punchy, about 190 words per minute, with short pauses only at each ellipsis; real emotion: frustrated on the problem lines, relieved and excited on the results, confident on the call to action. Nobody on screen speaks and there is no lip movement. Only the quoted lines are spoken, with no extra words or ad-libs.
0:00.2 to 0:03.0 "Your dog keeps scratching the same spot? Part the fur."
Voice sits clearly on top; foley ducks under the voice.

POSITIVE CONSTRAINTS
Real smartphone footage texture, natural unretouched detail. No subtitles, no on-screen text, no glow effects. One dog, one or two hands only.
```
### H2 — 2 A.M.
Refs: none (text-led) · optional first frame KF-H2 · **4s** (use 0.0–3.2 over Block A's A1; Block A continues from 3.2)
🎙 VO: "Hear that at 2 a.m.? That's your dog's skin on fire."
```
SCENE CONTEXT
In a near-dark bedroom at night, a tired woman lifts her head off the pillow, lit only by her phone, at the sound of her dog scratching again.

FIRST FRAME AND SPATIAL BLOCKING
A woman in her early 30s lies on a white pillow at frame center, her face lit from below by the cold glow of a phone in her hand; the rest of the room is dark; faint stripes of blue moonlight from blinds on the back wall. The first visible frame already contains the subject in position. No empty establishing frame, no delayed reveal.

FORMAT MODE
Single continuous take, 4 seconds. Real-time motion.

OPTICS
47° diagonal field of view, standard normal lens character, camera 1 meter away at pillow height. Natural proportions, no distortion.

CAMERA
Handheld, slight low-light micro-movement, fixed framing.

ACTION TIMING
0:00 to 0:01 She squints at the phone screen.
0:01 to 0:03 She lifts her head off the pillow and turns her eyes toward the foot of the bed at screen-right.
0:03 to 0:04 She exhales, exhausted, still staring toward screen-right.

PHYSICS
Hair and pillow move naturally with her head; the duvet shifts with her shoulder.

LIGHTING
The phone screen is the only key light; deep blue darkness elsewhere; heavy low-light noise. No fill light.

AUDIO
From 0:00, an off-screen rhythmic metallic collar-tag jingle and soft thumping from screen-right; her tired exhale at 0:03. No music.
VOICEOVER
NARRATOR VOICE (identical in every line): one off-screen female narrator, early 30s, natural American English, warm and conversational, like a real dog owner telling a close friend what finally worked. Not an announcer, not salesy, no radio voice. Close, intimate microphone, clean and dry with light room tone, soft natural breaths. Brisk and punchy, about 190 words per minute, with short pauses only at each ellipsis; real emotion: frustrated on the problem lines, relieved and excited on the results, confident on the call to action. Nobody on screen speaks and there is no lip movement. Only the quoted lines are spoken, with no extra words or ad-libs.
0:00.2 to 0:03.0 "Hear that at 2 a.m.? That's your dog's skin on fire."
Voice sits clearly on top; foley ducks under the voice.

POSITIVE CONSTRAINTS
Real smartphone footage texture, natural unretouched detail. No subtitles, no on-screen text, no glow effects. One dog, one or two hands only.
```
### H3 — Spray first
Refs: @WESTIE, @OWNER, @ATOKONG · first frame KF-G11 · **4s** (use 0.0–3.2 over Block A's A1; Block A continues from 3.2)
🎙 VO: "Watch what this Korean mist does to an itchy dog."
```
SCENE CONTEXT
The owner holds her dog's fur open over the irritated patch and mists it with the Korean skin spray.

ACTIVE REFERENCES
@WESTIE: 5-year-old male West Highland White Terrier, compact 8 kg body, coarse white coat with creamy tips, brown leather collar with a small round brass tag, irritated patch on his left flank just forward of the left hip, rust-brown saliva staining on his right front paw. 100% matches the reference.
@OWNER: early-30s woman seen only as hands and forearms, short unpolished nails, thin gold band on the right ring finger, oatmeal knit sleeves. 100% matches the reference.
@ATOKONG: small 30 ml white round spray bottle, about 10 cm tall, white pump nozzle, clear dome cap, orange cartoon-dog label. Shape, size and label design 100% match the reference.

FIRST FRAME AND SPATIAL BLOCKING
Matches the start image: overhead close-up of the irritated patch on @WESTIE's left flank at frame center; @OWNER's left hand spreading the fur from the top of frame; her right hand holding @ATOKONG 12 cm above the patch, nozzle aimed down, label turned away; a fine mist cloud already leaving the nozzle. The first visible frame already contains the subject in position. No empty establishing frame, no delayed reveal.

FORMAT MODE
Single continuous take, 4 seconds. Real-time motion.

OPTICS
29° diagonal field of view, close detail framing, camera 45 cm away. Patch, fingers and nozzle sharp.

CAMERA
Handheld, operator breath, slow push-in toward the patch.

ACTION TIMING
0:00 to 0:01 The first mist cloud drifts down over the patch.
0:01 to 0:02 Second pump.
0:02 to 0:04 Third pump; the colorless mist settles on the fur tips and pink skin; the dog stays relaxed and still.

PHYSICS
Each pump makes a short cone of fine droplets that slows with air resistance and falls with gravity. The index finger presses the pump with visible travel.

LIGHTING
Soft window daylight from screen-left; the mist is lit from the side.

AUDIO
Three crisp pump-mist sounds, "tss, tss, tss", one second apart. No music.
VOICEOVER
NARRATOR VOICE (identical in every line): one off-screen female narrator, early 30s, natural American English, warm and conversational, like a real dog owner telling a close friend what finally worked. Not an announcer, not salesy, no radio voice. Close, intimate microphone, clean and dry with light room tone, soft natural breaths. Brisk and punchy, about 190 words per minute, with short pauses only at each ellipsis; real emotion: frustrated on the problem lines, relieved and excited on the results, confident on the call to action. Nobody on screen speaks and there is no lip movement. Only the quoted lines are spoken, with no extra words or ad-libs.
0:00.2 to 0:03.0 "Watch what this Korean mist does to an itchy dog."
Voice sits clearly on top; foley ducks under the voice.

POSITIVE CONSTRAINTS
Real smartphone footage texture, natural unretouched detail. No subtitles, no on-screen text, no glow effects. One dog, one or two hands only.
```
### H6 — Not just a habit
Refs: @WESTIE · first frame KF-G04 · **4s** (use 0.0–3.2 over Block A's A1; Block A continues from 3.2)
🎙 VO: "Your dog licking his paws nonstop? It's not a habit."
```
SCENE CONTEXT
At rug level, a small white terrier obsessively licks and nibbles between the toes of his stained front paw.

ACTIVE REFERENCES
@WESTIE: 5-year-old male West Highland White Terrier, compact 8 kg body, coarse white coat with creamy tips, brown leather collar with a small round brass tag, irritated patch on his left flank just forward of the left hip, rust-brown saliva staining on his right front paw. 100% matches the reference.

FIRST FRAME AND SPATIAL BLOCKING
Extreme close-up at rug level: @WESTIE's head lowered to his right front paw at frame center, tongue between the toes; rust-brown staining on the white toe fur, pink irritated skin between the toes. The first visible frame already contains the subject in position. No empty establishing frame, no delayed reveal.

FORMAT MODE
Single continuous take, 4 seconds. Real-time motion.

OPTICS
29° diagonal field of view, close detail framing, camera 50 cm away. Paw and tongue razor-sharp, background soft.

CAMERA
Handheld at floor level, slow push-in.

ACTION TIMING
0:00 to 0:02 Short repetitive licks between the toes, eyes half closed.
0:02 to 0:03 A quick nibble at the base of the toes, pulling the paw slightly.
0:03 to 0:04 Back to licking, faster.

PHYSICS
A wet, flexible tongue leaves the toe fur damp and clumped; the paw shifts with each pull; the head moves with real weight.

LIGHTING
Soft window daylight from screen-left.

AUDIO
Wet licking and nibbling sounds, quiet room tone. No music.
VOICEOVER
NARRATOR VOICE (identical in every line): one off-screen female narrator, early 30s, natural American English, warm and conversational, like a real dog owner telling a close friend what finally worked. Not an announcer, not salesy, no radio voice. Close, intimate microphone, clean and dry with light room tone, soft natural breaths. Brisk and punchy, about 190 words per minute, with short pauses only at each ellipsis; real emotion: frustrated on the problem lines, relieved and excited on the results, confident on the call to action. Nobody on screen speaks and there is no lip movement. Only the quoted lines are spoken, with no extra words or ad-libs.
0:00.2 to 0:03.0 "Your dog licking his paws nonstop? It's not a habit."
Voice sits clearly on top; foley ducks under the voice.

POSITIVE CONSTRAINTS
Real smartphone footage texture, natural unretouched detail. No subtitles, no on-screen text, no glow effects. One dog, one or two hands only.
```
*With H6, shorten A4 in Block A to a reaction close-up (or reuse A4 as is) so the paw licking doesn't repeat back to back.*

### H6-GR — Not just a habit (Golden Retriever variant)
Refs: @GOLDEN (REF-GOLDEN) · first frame **KF-H6-GR** · **4s** (use 0.0–3.2 over Block A's A1)
🎙 VO: "Your dog licking his paws nonstop? It's not a habit."
Tests the **dog breed** at the hook against the Westie H6, with the same action, framing and VO. Golden Retrievers are the most-used breed in the competitor ads and the most widely owned "allergy dog". The body stays on the Westie; viewers read it as "another dog", which matches the competitor's multi-breed approach.
```
SCENE CONTEXT
At rug level, a golden retriever obsessively licks and chews between the toes of his red, stained front paw.

ACTIVE REFERENCES
@GOLDEN: 4-year-old male Golden Retriever, about 32 kg, medium-gold wavy coat with lighter feathering on the legs and chest, dark brown eyes, black nose, worn green nylon collar. Rust-red saliva staining on the light fur of his right front paw. 100% matches the reference.

FIRST FRAME AND SPATIAL BLOCKING
Extreme close-up at rug level: @GOLDEN lying on a light grey rug, head lowered at frame center-top, tongue between the toes of his right front paw at frame center-bottom; the light gold toe fur is matted and stained rust-red, and the skin between the toes is pink, irritated and slightly swollen. The first visible frame already contains the dog in position. No empty establishing frame, no delayed reveal.

FORMAT MODE
Single continuous take, 4 seconds. Real-time motion.

OPTICS
29° diagonal field of view, close detail framing, camera 60 cm away. Paw, tongue and muzzle razor-sharp, background soft.

CAMERA
Handheld at floor level, operator breath, slow push-in toward the paw.

ACTION TIMING
0:00 to 0:02 Long, repetitive tongue strokes between the toes, eyes half closed and focused.
0:02 to 0:03 He chews at the base of the toes with his front teeth, pulling the paw toward his mouth.
0:03 to 0:04 Back to licking, faster and more frantic.

PHYSICS
A large, wet, flexible tongue leaves the toe fur soaked and clumped; the heavy paw shifts with each pull; the head moves with real weight; the ear flops with the motion.

LIGHTING
Soft window daylight from screen-left, gentle warm tone on the gold coat, natural shadow under the muzzle.

AUDIO
Loud wet licking and chewing sounds, quiet room tone. No music.
VOICEOVER
NARRATOR VOICE (identical in every line): one off-screen female narrator, early 30s, natural American English, warm and conversational, like a real dog owner telling a close friend what finally worked. Not an announcer, not salesy, no radio voice. Close, intimate microphone, clean and dry with light room tone, soft natural breaths. Brisk and punchy, about 190 words per minute, with short pauses only at each ellipsis; real emotion: frustrated on the problem lines, relieved and excited on the results, confident on the call to action. Nobody on screen speaks and there is no lip movement. Only the quoted lines are spoken, with no extra words or ad-libs.
0:00.2 to 0:03.0 "Your dog licking his paws nonstop? It's not a habit."
Voice sits clearly on top; foley ducks under the voice.

POSITIVE CONSTRAINTS
Real smartphone footage texture, natural unretouched fur. One dog, four toes plus dewclaw, natural anatomy. No subtitles, no on-screen text, no glow effects. No blood, no open wound.
```
---

## BLOCK B — Authority + Demo (12.0–24.0)

**VO for this block (spoken by Seedance):**

| Shot | Block time | Ad time | VO / super |
|---|---|---|---|
| B1 | 0:00–2.0 | 12.0–14.0 | "Made in Korea by a veterinarian with twenty years in clinic…" |
| B2 | 2.0–4.0 | 14.0–16.0 | "…and a scientist with thirty years in skin immunity." |
| B3 | 4.0–5.8 | 16.0–17.8 | "Officially registered in Korea." · Super: REGISTERED VETERINARY QUASI-DRUG · KOREA + 0.8s real certificate insert in the edit |
| B4 | 5.8–7.2 | 17.8–19.2 | "Powered by rare Korean botanicals." |
| B5 | 7.2–9.0 | 19.2–21.0 | "No steroids. Totally lick-safe." |
| B6 | 9.0–12.0 | 21.0–24.0 | "Three sprays… and the itch is gone." → leads straight into Block C |

Generate exactly 12s and use all of it.

```
SCENE CONTEXT
The Korean expertise behind the mist: a veterinarian examines a terrier's skin, a Korean researcher studies the formula, a botanical extract is measured, Korean daphne flowers bloom, then the owner mists her palm and sprays her dog's irritated patch.

ACTIVE REFERENCES
@WESTIE: 5-year-old male West Highland White Terrier, compact body, coarse white coat, brown collar with brass tag. 100% matches the reference.
@PATCH: the exact irritated patch on @WESTIE's left flank and the overhead framing of the owner's hands spreading the fur. 100% matches the reference.
@RESEARCHER: Korean veterinary researcher in her early 50s, black hair tied back with a few grey strands, thin reading glasses, white lab coat over navy scrubs. 100% matches the reference.
@OWNER: hands and forearms only, thin gold band on the right ring finger, oatmeal knit sleeves. 100% matches the reference.
@ATOKONG: small 30 ml white round spray bottle, about 10 cm tall, white pump nozzle, clear dome cap, orange cartoon-dog label. 100% matches the reference.

FORMAT MODE
Controlled multi-shot sequence, 12 seconds, six shots, HARD CUTS only at 2.0, 4.0, 5.8, 7.2 and 9.0 seconds. No fades, no dissolves, no transition effects. Every shot opens with its subject already in frame.

SHOT B1 — 0:00 to 0:02.0 — VET EXAM
First frame: clinic exam room; @WESTIE standing calmly on a stainless steel exam table, body facing screen-right; a veterinarian seen only from chest down, navy scrub top and blue nitrile gloves, both hands already resting on his flank under a round illuminated magnifier lamp. The vet's face never appears.
Optics: 47° diagonal field of view, standard normal lens character, camera over the vet's shoulder at chest height, 1 meter away.
Camera: handheld, steady, slight drift toward the hands.
Action: the gloved hands gently part the fur on the flank; the vet lowers the magnifier lamp a few degrees.
Light: clean neutral clinic light plus the cool white ring of the magnifier.

SHOT B2 — 0:02.0 to 0:04.0 — KOREAN RESEARCHER
First frame: a bright modern research lab in Seoul; @RESEARCHER seated at a white bench at center-right in three-quarter view facing screen-left, eyes just lifting from a microscope; a rack of small glass vials at screen-left; window at screen-left; a colleague out of focus behind.
Optics: 29° diagonal field of view, short telephoto portrait character, camera 2 meters away at seated eye level; her face razor-sharp, background soft bokeh.
Camera: handheld documentary drift toward her.
Action: she sits back from the microscope, picks up a small clear vial of pale amber liquid and raises it toward the window light, studying it. She does not look at the camera.
Light: soft window key from screen-left, gentle shadow on the right side of her face, the vial glowing amber only from daylight passing through it. Natural skin texture, no beauty fill.

SHOT B3 — 0:04.0 to 0:05.8 — PIPETTE DROP
First frame: lab bench macro; a glass dropper pipette held vertically at frame center, a drop of pale amber extract hanging 2 cm above a small clear vial.
Optics: 18° diagonal field of view, telephoto macro, razor focus on the drop.
Camera: locked off. Half-speed slow motion.
Action: the drop swells, releases, falls into the vial and sends a small ripple across the liquid.
Light: cool neutral daylight from behind, a soft rim on the glass.

SHOT B4 — 0:05.8 to 0:07.2 — KOREAN DAPHNE
First frame: macro of a dense rounded cluster of small white four-lobed tubular Daphne kiusiana flowers at a branch tip, glossy dark-green leaves around it, dew on the petals.
Optics: 18° diagonal field of view, telephoto macro; the forest background is a soft green wash.
Camera: locked off.
Action: a light breeze sways the branch a few millimeters; one dew drop slides off a petal.
Light: soft overcast morning forest light.

SHOT B5 — 0:07.2 to 0:09.0 — MIST ON PALM
First frame: @OWNER's open left palm facing up at frame center against a bright window; @ATOKONG in her right hand at the right edge of frame, nozzle 15 cm from the palm.
Optics: 29° diagonal field of view, close detail framing, camera 50 cm away.
Camera: handheld, fixed framing. Half-speed slow motion.
Action: one pump; a fine colorless mist cloud spreads over the palm and tiny droplets bead on the skin.
Light: strong side-backlight from the window; the mist is lit only by backlight scatter.

SHOT B6 — 0:09.0 to 0:12.0 — THE SPRAY DEMO
First frame matches @PATCH: overhead close-up of @WESTIE's left flank on the cream rug with the irritated patch exposed at frame center; @OWNER's left hand spreading the fur from the top of frame; her right hand holding @ATOKONG in the upper right, 12 cm above the patch, nozzle aimed down, label turned away.
Optics: 29° diagonal field of view, close detail framing, camera 45 cm away.
Camera: handheld, fixed framing; in the final second a slow push-in toward one droplet on the skin at frame center.
Action: three pumps, one second apart; each releases a short cone of fine mist that drifts down onto the patch; the bottle lifts out of frame top-right; droplets settle on the fur tips and pink skin. The dog stays relaxed and still. The skin does not change color in this shot.
Light: soft window daylight from screen-left; the mist is lit from the side.

CONTINUITY
Same @WESTIE in B1 and B6. Same owner's hands, gold ring on the right hand, same small bottle in B5 and B6. B6 matches the @PATCH framing exactly.

PHYSICS
Gloves crease at the knuckles; the lamp arm moves with mechanical resistance. Liquids have real viscosity and surface tension. The mist is made of real fine droplets that slow with air resistance and fall with gravity. Fur parts along its growth direction.

AUDIO
Natural foley only: quiet clinic room tone and glove rustle (B1); soft lab ambience and a glass clink (B2); a tiny drip (B3); forest ambience and distant birds (B4); one soft pump-mist "tss" (B5); three crisp "tss, tss, tss" one second apart (B6). No music.

VOICEOVER
NARRATOR VOICE (identical in every line): one off-screen female narrator, early 30s, natural American English, warm and conversational, like a real dog owner telling a close friend what finally worked. Not an announcer, not salesy, no radio voice. Close, intimate microphone, clean and dry with light room tone, soft natural breaths. Brisk and punchy, about 190 words per minute, with short pauses only at each ellipsis; real emotion: frustrated on the problem lines, relieved and excited on the results, confident on the call to action. Nobody on screen speaks and there is no lip movement. Only the quoted lines are spoken, with no extra words or ad-libs.
0:00.1 to 0:02.0 "Made in Korea by a veterinarian with twenty years in clinic…"
0:02.1 to 0:04.2 "…and a scientist with thirty years in skin immunity."
0:04.3 to 0:05.7 "Officially registered in Korea."
0:05.9 to 0:07.2 "Powered by rare Korean botanicals."
0:07.3 to 0:09.0 "No steroids. Totally lick-safe."
0:09.3 to 0:11.6 "Three sprays… and the itch is gone."
Voice sits clearly on top; foley ducks under the voice.

POSITIVE CONSTRAINTS
Real documentary and smartphone texture; the lab is a real working lab, not futuristic. No holograms, no screens with graphics, no glowing liquids, no sparkles. No subtitles or on-screen text. The spray never goes toward the dog's head.
```

---

## BLOCK C — Macro science dive (24.0–27.0) · generated on its own

**VO:** 24.0–27.0 "Soaks in instantly. Calms the itch. Rebuilds damaged skin." · Super: *Visualization*
First frame **KF-G12** · last frame **KF-G12-SCI-END** · 3s exactly. It cuts in directly after B6's push-in toward a droplet.

```
SCENE CONTEXT
An extreme macro of a mist droplet on irritated dog skin pushes through the surface into a microscope-style cross-section, where the clear liquid soaks into the gaps of the irritated surface layer and the tissue visibly calms.

FIRST FRAME AND SPATIAL BLOCKING
The first visible frame matches the start image: tiny clear droplets on white hair tips and pink skin, one droplet at frame center. The last frame matches the end image: a calm, sealed skin cross-section with a hair shaft rising diagonally at screen-right.

FORMAT MODE
Controlled multi-shot sequence, 3 seconds, with one MATCH CUT at 0.6 seconds on the droplet at frame center.

SHOT C1 — 0:00 to 0:00.6
18° diagonal field of view, telephoto macro, razor-thin focus on the skin. A slow steady push-in toward the droplet at frame center as it starts to soak into the skin.

SHOT C2 — 0:00.6 to 0:03.0
A scientific microscope view of the skin cross-section, flat even perspective, soft shallow depth of field, continuing the same slow downward push.
0:00.6 to 0:01.4 The surface cell layer is uneven and slightly lifted with small gaps; the tissue below is deep red-pink; clear liquid from the surface flows down into the gaps.
0:01.4 to 0:02.6 The liquid wicks along the gaps; the lifted cells settle flat and close together into a smooth continuous layer; the red-pink tissue slowly cools to calm pale pink.
0:02.6 to 0:03.0 Hold on the calm, sealed layer with a thin film of moisture on top.

PHYSICS
Real water-based fluid: it beads, wicks by capillary action and spreads slowly. Cells settle organically like soft living tissue, never snapping or morphing abruptly. Gradual, even color change.

LIGHTING
Soft, even, cool-neutral light from above like a microscope illuminator. Muted natural tissue colors.

AUDIO
A soft low ambient tone and a faint wet seep. No music.

VOICEOVER
NARRATOR VOICE (identical in every line): one off-screen female narrator, early 30s, natural American English, warm and conversational, like a real dog owner telling a close friend what finally worked. Not an announcer, not salesy, no radio voice. Close, intimate microphone, clean and dry with light room tone, soft natural breaths. Brisk and punchy, about 190 words per minute, with short pauses only at each ellipsis; real emotion: frustrated on the problem lines, relieved and excited on the results, confident on the call to action. Nobody on screen speaks and there is no lip movement. Only the quoted lines are spoken, with no extra words or ad-libs.
0:00.1 to 0:02.9 "Soaks in instantly. Calms the itch. Rebuilds damaged skin."
Voice sits clearly on top; foley ducks under the voice.

POSITIVE CONSTRAINTS
Photoreal scientific micro-photography in every frame. No neon, no glowing particles, no energy rings, no sparkles, no cartoon or 3D-render cells, no text, no labels.
```
---

## BLOCK D — Relief + Proof (27.0–39.0)

**VO for this block (spoken by Seedance):**

| Shot | Block time | Ad time | VO / super (supers added in post) |
|---|---|---|---|
| D1 | 0:00–1.4 | 27.0–28.4 | "Instant, cooling relief." |
| D2 | 1.4–4.6 | 28.4–31.6 | "Seconds later… he finally stopped scratching." |
| D3 | 4.6–5.6 | 31.6–32.6 | "Before…" · super **BEFORE** |
| D4 | 5.6–6.8 | 32.6–33.8 | "Day one, redness calming." · super **DAY 1** |
| D5 | 6.8–8.0 | 33.8–35.0 | "Day three, flakes gone." · super **DAY 3** |
| D6 | 8.0–9.8 | 35.0–36.8 | "Day five… brand-new, healthy skin." · super **DAY 5** + *Dramatization. Individual results may vary.* |
| D7 | 9.8–12.0 | 36.8–39.0 | "Even those licked-raw paws… calm again." · supers **BEFORE / DAY 5** |

Generate exactly 12s and use all of it.

```
SCENE CONTEXT
After his owner sprays him, a small white terrier shakes off, lies down in the sun and relaxes, then a series of identical close-ups taken over five days shows his irritated skin calming, followed by his paw before and after.

ACTIVE REFERENCES
@WESTIE: 5-year-old male West Highland White Terrier, compact 8 kg body, coarse white coat, brown leather collar with a small round brass tag. 100% matches the reference.
@PATCH: the irritated patch on @WESTIE's left flank in its BEFORE state and the exact overhead framing of the owner's two hands spreading the fur. 100% matches the reference.
@DAY5: the same patch and identical framing on day five, skin calm pale pink, no flakes, short fur with faint new fuzz. 100% matches the reference.
@OWNER: hands and forearms only, thin gold band on the right ring finger, oatmeal knit sleeves. 100% matches the reference.
@ATOKONG: small 30 ml white round spray bottle, about 10 cm tall, white pump nozzle, clear dome cap, orange cartoon-dog label. 100% matches the reference.

FORMAT MODE
Controlled multi-shot sequence, 12 seconds, seven shots, HARD CUTS only at 1.4, 4.6, 5.6, 6.8, 8.0, 9.8 and 10.9 seconds. No fades, no dissolves, no morphing between shots. Shots D3, D4, D5 and D6 are four separate photographs-in-motion with IDENTICAL camera position, framing, hand pose and lighting; only the skin condition differs between them.

SHOT D1 — 0:00 to 0:01.4 — SHAKE-OFF
First frame: living room at rug level; @OWNER's right hand setting @ATOKONG upright on the cream rug in the left foreground, label turned away; @WESTIE standing in the midground facing screen-left toward the window.
Optics: 47° diagonal field of view, standard normal lens character, camera 1.2 meters from the dog at rug level.
Camera: handheld at floor level, fixed framing.
Action: the hand releases the bottle and withdraws; @WESTIE does a full-body shake from head to tail, ears flapping, collar tag swinging.
Light: warm afternoon window light from screen-left.

SHOT D2 — 0:01.4 to 0:04.6 — RELIEF
First frame: @WESTIE already lying chest-down at frame center inside a warm rectangle of sunlight on the rug, front paws forward, chin just above his paws, eyes half open; @OWNER's right hand resting on his back from the top-right.
Optics: 29° diagonal field of view, short telephoto portrait character, camera 1.5 meters away at rug height; his face razor-sharp, background compressed into soft warm bokeh.
Camera: static on the floor.
Action: a slow deep breath, then a long audible sigh through the nose; his body visibly relaxes and settles; he lowers his chin onto his paws and his eyes slowly close; the hand strokes once along his back and lifts away. He does not scratch.
Light: warm low sun from screen-left, soft glowing edges on his fur.

SHOT D3 — 0:04.6 to 0:05.6 — BEFORE
First frame matches @PATCH exactly: overhead close-up of the left flank, both hands spreading the fur at the top of frame, the patch blotchy pink-to-red with fine scratch marks, dry white flakes at the hair roots, thinned broken fur.
Optics: 29° diagonal field of view, close detail framing, phone 35 cm above the coat.
Camera: very steady handheld, no push-in, no reframing.
Action: the fingers spread the fur 1 cm further apart; the flank rises with one breath.
Light: soft daylight from screen-left.

SHOT D4 — 0:05.6 to 0:06.8 — DAY 1
Identical camera, framing, hands and light to D3. The patch is a shade calmer: the darkest red center has softened to red-pink, with slightly fewer flakes and faint scratch marks.
Action: the same small finger spread; one breath.

SHOT D5 — 0:06.8 to 0:08.0 — DAY 3
Identical camera, framing, hands and light to D3. The patch is soft even pink with faded scratch marks and almost no flakes; the fur over it is still thin.
Action: the same small finger spread; one breath.

SHOT D6 — 0:08.0 to 0:09.8 — DAY 5
Identical camera, framing, hands and light to D3, matching @DAY5: calm pale-pink skin close to normal skin tone, no flakes, no staining, short fur with a faint first layer of fine new fuzz.
Action: the same small finger spread, then the hands hold still.

SHOT D7 — 0:09.8 to 0:12.0 — PAW BEFORE / DAY 5
0:09.8 to 0:10.9 First frame: close-up of @WESTIE's right front paw resting in @OWNER's open right palm, her thumb gently spreading two toes; rust-brown staining on the white toe fur, pink irritated skin between the toes.
HARD CUT at 0:10.9 to the identical framing: the same paw now with noticeably cleaner fur, staining faded to a light trace, calm pale skin between the toes, no swelling.
Optics: 29° diagonal field of view, close detail framing, camera 30 cm away.
Camera: very steady handheld, no reframing.
Light: soft daylight from screen-left.

CONTINUITY
Same dog, collar and tag throughout. D3–D6 are framed identically, like an owner's daily progress photos; nothing moves between them except the skin condition. Gold ring always on the right hand.

PHYSICS
The shake travels from head to tail with real fur inertia. Breathing is visible in the rib cage and nostrils. Body weight settles into the rug. Fur parts along its growth direction; skin moves slightly with finger pressure. Each day's skin state stays fixed within its shot; no morphing.

AUDIO
Natural foley only: bottle tap on the rug, shake flap and tag jingle (D1); a long dog sigh and soft room tone (D2); soft fur rustle (D3–D7). No music.

VOICEOVER
NARRATOR VOICE (identical in every line): one off-screen female narrator, early 30s, natural American English, warm and conversational, like a real dog owner telling a close friend what finally worked. Not an announcer, not salesy, no radio voice. Close, intimate microphone, clean and dry with light room tone, soft natural breaths. Brisk and punchy, about 190 words per minute, with short pauses only at each ellipsis; real emotion: frustrated on the problem lines, relieved and excited on the results, confident on the call to action. Nobody on screen speaks and there is no lip movement. Only the quoted lines are spoken, with no extra words or ad-libs.
0:00.0 to 0:01.4 "Instant, cooling relief."
0:01.6 to 0:04.4 "Seconds later… he finally stopped scratching."
0:04.7 to 0:05.5 "Before…"
0:05.7 to 0:06.7 "Day one, redness calming."
0:06.9 to 0:07.9 "Day three, flakes gone."
0:08.1 to 0:09.7 "Day five… brand-new, healthy skin."
0:10.0 to 0:11.8 "Even those licked-raw paws… calm again."
Voice sits clearly on top; foley ducks under the voice.

POSITIVE CONSTRAINTS
Real smartphone footage texture. No text, no day labels, no split screen (both added in post). No glow, no sparkles. No full coat regrowth: by day five the fur is still short.
```

---

## BLOCK E — Payoff + End (39.0–50.0)

**VO for this block (spoken by Seedance):**

| Shot | Block time | Ad time | VO |
|---|---|---|---|
| E1 | 0:00–1.8 | 39.0–40.8 | "No more scratching. No more licking." |
| E2 | 1.8–3.6 | 40.8–42.6 | "Finally, we both sleep through the night." |
| E3 | 3.6–5.2 | 42.6–44.2 | "And it works for cats, too." · super FOR DOGS & CATS |
| E4 | 5.2–11.0 | 44.2–50.0 | "Every pet owner needs one. Tap below to get Atokong No-Itch Mist on sale today, while stock lasts." · end card overlays from 45.4 |

Generate exactly 11s and use all of it. Composite the real packshot over the bottle in E4.

```
SCENE CONTEXT
The terrier is happy again: he races across a morning lawn, sleeps peacefully at night beside his sleeping owner, his cat housemate gets a gentle spray too, and both pets rest on a sunny bed beside the bottle.

ACTIVE REFERENCES
@WESTIE: 5-year-old male West Highland White Terrier, compact 8 kg body, clean white coat, brown leather collar with a small round brass tag. 100% matches the reference.
@CAT: 4-year-old grey British Shorthair, dense plush blue-grey coat, round copper eyes. 100% matches the reference.
@OWNER: hands and forearms only, thin gold band on the right ring finger, oatmeal knit sleeves. 100% matches the reference.
@ATOKONG: small 30 ml white round spray bottle, about 10 cm tall, white pump nozzle, clear dome cap, orange cartoon-dog label. 100% matches the reference.

FORMAT MODE
Controlled multi-shot sequence, 11 seconds, four shots, HARD CUTS only at 1.8, 3.6 and 5.2 seconds. No fades, no dissolves, no transition effects. Every shot opens with its subjects already in frame.

SHOT E1 — 0:00 to 0:01.8 — ZOOMIES
First frame: dewy back-garden lawn in low morning sun; @WESTIE already mid-gallop straight toward camera at frame center, front paws off the ground, ears up, tongue out.
Optics: 18° diagonal field of view, classic telephoto lens character, camera at grass level 6 meters away; background compressed and fully blurred into a soft green-gold wash; razor focus on his face; close framing achieved through lens reach.
Camera: handheld at grass level, tracking slightly to keep him centered.
Action: a real bounding gallop with ground contact on every stride, ears flopping, collar tag bouncing, dew kicked up.
Light: low sun behind him, a bright rim along his white coat.

SHOT E2 — 0:01.8 to 0:03.6 — PEACEFUL NIGHT
First frame: the bedroom at night from floor level; @WESTIE already asleep, curled in a ball on the round grey dog bed in the right half of frame at the foot of the bed, chin on his tail; a woman asleep under a white duvet in soft focus behind, turned away.
Optics: 47° diagonal field of view, standard normal lens character, camera 1.5 meters away.
Camera: completely still.
Action: slow, deep sleeping breaths; one ear twitches once. The woman does not move.
Light: cool blue moonlight stripes from blinds at screen-right; low-light noise; calm deep shadows.

SHOT E3 — 0:03.6 to 0:05.2 — CAT TOO
First frame: @CAT sitting on a grey linen sofa at frame center facing screen-left; @OWNER's left hand already parting the fur at the side of the cat's neck behind the jaw; her right hand holding @ATOKONG 15 cm away, aimed at the parted fur and away from the face.
Optics: 47° diagonal field of view, standard normal lens character, camera 70 cm away at the cat's eye level.
Camera: handheld, fixed framing.
Action: one soft pump of mist onto the parted fur; the bottle withdraws; the cat does a long slow blink.
Light: soft window daylight from screen-left.

SHOT E4 — 0:05.2 to 0:11.0 — END HERO
First frame: bright morning bedroom; @WESTIE sitting upright at frame center on the white duvet, looking at camera, mouth slightly open, clean white coat; @CAT lying on the duvet behind him at screen-left, slightly soft; @ATOKONG standing upright on the edge of a bedside table in the lower-right foreground, label facing camera. The upper third of frame is clean, softly lit wall.
Optics: 29° diagonal field of view, short telephoto portrait character, camera 1.8 meters away at the dog's eye level.
Camera: static on a tripod.
Action: @WESTIE tilts his head slightly, ears forward, pants gently, then closes his mouth and looks at camera; @CAT stretches one front paw and settles. The bottle stays still.
Light: bright soft morning daylight from screen-right through open blinds.

CONTINUITY
Same @WESTIE, collar and tag in E1, E2 and E4. Same small 30 ml bottle in E3 and E4. Same bedroom in E2 (night) and E4 (morning).

PHYSICS
Real gallop with weight and ground contact; fur bounces with delay. Slow, natural sleeping breath. The mist settles with gravity. The duvet compresses under both animals.

AUDIO
Natural foley only: paw thuds on grass, tag jingle and panting (E1); quiet slow breathing and a faint ticking clock (E2); one soft "tss" and a purr (E3); quiet morning room tone and distant birds (E4). No music.

VOICEOVER
NARRATOR VOICE (identical in every line): one off-screen female narrator, early 30s, natural American English, warm and conversational, like a real dog owner telling a close friend what finally worked. Not an announcer, not salesy, no radio voice. Close, intimate microphone, clean and dry with light room tone, soft natural breaths. Brisk and punchy, about 190 words per minute, with short pauses only at each ellipsis; real emotion: frustrated on the problem lines, relieved and excited on the results, confident on the call to action. Nobody on screen speaks and there is no lip movement. Only the quoted lines are spoken, with no extra words or ad-libs.
0:00.1 to 0:01.7 "No more scratching. No more licking."
0:01.9 to 0:03.5 "Finally, we both sleep through the night."
0:03.7 to 0:05.1 "And it works for cats, too."
0:05.5 to 0:10.6 "Every pet owner needs one. Tap below to get Atokong No-Itch Mist on sale today, while stock lasts." (say "Atokong" as AH-toh-kong, stress on the first syllable; warm, smiling, with a small pause before "Tap below")
Voice sits clearly on top; foley ducks under the voice.

POSITIVE CONSTRAINTS
Real smartphone and tripod footage texture. One dog, one cat. The spray never goes toward the cat's eyes, ears or mouth. No subtitles or on-screen text.
```

---

## Edit assembly (multi-shot route)
1. Join the blocks with their generated voiceover; check that the voice matches across blocks (see the note above).
2. Butt-join the full generations: A (12s) → B (12s) → C (3s) → D (12s) → E (11s) = 50.0s. No trimming.
3. Only nudge a VO line if a cut landed visibly early or late.
4. Add: captions transcribed from the generated VO, (orange `#F2A21B` highlight), supers, day counters, the real certificate insert in B3, the real packshot composite in A5/A6/E4, music bed, end card, light grain across everything.
5. Hooks: re-generate Block A with the swapped A1 paragraph, or splice a standalone hook clip from `VIDEO_PROMPTS.md` over 0.0–3.2.

---

## Compliance cleanup list (for the next pass)
- ⚠ "stops the itch fast" / "Seconds after the first spray… finally stopped scratching": speed claims; keep only if backed by customer data. Safer: "From the very first spray…"
- ⚠ "Rebuilds damaged skin" / "the itch is gone" / "Instant, cooling relief": drug-type and absolute claims. Safer: "supports the skin barrier", "soothes the itch".
- ⚠ "brand-new, healthy skin" in five days: a transformation claim. Keep the dramatization super.
- ⚠ "No more scratching. No more licking.": absolute. Safer: "Less scratching. Less licking."
- ⚠ "rare Korean botanicals": "rare" needs support. Safer: "Korean medicinal botanicals".
- ⚠ "while stock lasts": only use it if stock is genuinely limited.
- "Officially registered in Korea": fine if it matches the certificate wording.

---

## BLOCK D-X — Extreme transformation test (standalone, no VO)

A standalone test of a **more extreme, faster** version of D3–D7 (the Before → Day 5 skin series plus the paw before/after). Generate as many takes as you like and cut the best one into Block D over 31.6–39.0, or use it as a hook. There's no voiceover; Block D's VO or the music carries it.

- **Length:** generate **6s**, about 1.4s faster than the original 7.4s span. In Block D, lay it over 31.6–37.6 and let the D7 VO line ("Even those licked-raw paws… calm again.") finish over the start of Block E, or trim it.
- **Refs:** @WESTIE, @OWNER, @PATCH (KF-G01). Optional: @DAY5. For the extreme version, a new edit of KF-G01 with a full, healthy coat works better (see the note at the end).
- **Claims:** this is an aggressive test. Full fur regrowth in 5 days goes beyond the brief; it's on the compliance cleanup list.

```
SCENE CONTEXT
A rapid series of identical overhead progress shots of a small white terrier's flank shows a raw, inflamed bald patch transform into healthy skin and a full white coat over five days, followed by his red, licked-raw paw becoming clean and healthy.

ACTIVE REFERENCES
@WESTIE: 5-year-old male West Highland White Terrier, compact 8 kg body, coarse white coat, lying on his right side with the left flank facing up. 100% matches the reference.
@PATCH: the exact overhead framing of the owner's two hands spreading the fur on @WESTIE's left flank, just forward of the left hip. 100% matches the reference for framing, hands and location.
@OWNER: hands and forearms only, thin gold band on the right ring finger, oatmeal knit sleeves. 100% matches the reference.

FORMAT MODE
Controlled multi-shot sequence, 6 seconds, six shots, HARD CUTS only at 1.2, 2.0, 2.8, 4.2 and 5.0 seconds. No fades, no dissolves, no morphing between shots. X1 to X4 are framed IDENTICALLY, like an owner's daily progress photos: same camera position, framing, hand pose and light. Only the skin and fur change between them. X5 and X6 are framed identically to each other.

SHOT X1 — 0:00 to 0:01.2 — BEFORE (severe)
First frame matches @PATCH framing: overhead close-up of the left flank, both hands at the top of frame spreading the fur wide open. At frame center, a large bald patch about 8 cm wide: angry, inflamed deep red skin, visibly swollen and raised at the edges, with thick crusty yellow-white scale and flakes, dense crisscrossing scratch tracks, rough cracked texture, almost no fur left in the patch, and the surrounding white fur matted and stained dark rust-brown from licking. Dry and crusted, no fresh blood, no open wound.
Optics: 29° diagonal field of view, close detail framing, phone 35 cm above the coat; the patch razor-sharp.
Camera: very steady handheld, no push-in, no reframing.
Action: the fingers spread the fur 1 cm further apart; the skin twitches once.
Light: soft daylight from screen-left.

SHOT X2 — 0:01.2 to 0:02.0 — DAY 1
Identical camera, framing, hands and light to X1. Already visibly calmer: swelling gone, the deep red faded to bright pink, most of the crust and scale gone, scratch tracks softened.
Action: the same small finger spread.

SHOT X3 — 0:02.0 to 0:02.8 — DAY 3
Identical camera, framing, hands and light to X1. Smooth, even soft-pink skin, no flakes, no crust, no scratch marks; a dense layer of short new white fur is already covering the patch; the surrounding fur is clean white with no staining.
Action: the same small finger spread.

SHOT X4 — 0:02.8 to 0:04.2 — DAY 5
Identical camera, framing, hands and light to X1. The bald patch is completely gone: a full, thick, clean, bright white coat with healthy shine covers the whole area. Where the fingers part the fur, the skin underneath is healthy pale pink. It looks like a perfectly healthy dog.
Action: the fingers spread the fur, then smooth it back down, revealing how full and healthy the coat is.

SHOT X5 — 0:04.2 to 0:05.0 — PAW BEFORE
First frame: close-up of @WESTIE's right front paw resting in @OWNER's open right palm, her thumb spreading two toes. The fur between and on top of the toes is soaked, matted and stained dark rust-brown from constant licking; the skin between the toes is raw-looking, angry red and swollen, with thinned hair. Dry, no wound.
Optics: 29° diagonal field of view, close detail framing, camera 30 cm away.
Camera: very steady handheld, no reframing.
Action: the thumb gently spreads the toes.
Light: soft daylight from screen-left.

SHOT X6 — 0:05.0 to 0:06.0 — PAW DAY 5
Identical framing, hand pose and light to X5. The same paw is now completely transformed: fluffy, clean, bright white fur between and on top of the toes, no staining at all, calm healthy pale-pink skin, no swelling.
Action: the thumb gently spreads the toes; the paw flexes once.

CONTINUITY
Same dog, same left flank, same hands and gold ring on the right hand in every flank shot. Same paw and palm in X5 and X6. Nothing moves between the identical-framing shots except the skin and fur.

PHYSICS
Fur parts along its growth direction and springs back; skin moves slightly with finger pressure; the healthy coat in X4 is dense and springy, smoothing down under the hand. Each shot's skin state stays fixed inside the shot. No morphing, no time-lapse growth on screen.

AUDIO
Soft fur rustle and quiet room tone, with a subtle camera-shutter tick on each cut. No music. No voice. No narration.

POSITIVE CONSTRAINTS
Real smartphone progress-photo realism; true-to-life skin and fur textures. No subtitles, no day labels, no text, no split screen. No glow, no sparkles, no blood.
```

**Optional extreme reference images** (edit KF-G01 with your image editor, same framing, to anchor X1 and X4):
- *X1 severe:* "Edit this image. Keep everything identical. Change ONLY the patch: make it larger, about 8 cm, fully bald, angry deep red and swollen, with thick crusty yellow-white scale, dense crisscross scratch tracks, and dark rust-stained matted fur around it. Dry, no blood."
- *X4 full coat:* "Edit this image. Keep everything identical. Change ONLY the patch area: it is completely covered by a full, thick, bright white healthy coat identical to the surrounding fur; the skin visible between the parted fingers is healthy pale pink."

---

## BLOCK I — Skin-immunity insert (10s, optional, with VO)

Sells the second differentiator: **ATOKONG doesn't just soothe, it boosts the skin's own immunity**, backed by the 30-year immune-cell research. It also answers the competitor's "topicals only mask surface symptoms" line (C02).

**Where it goes:** straight after **Block C** (the science dive), at 27.0s. Blocks D and E shift +10s, and the ad becomes **60.0s**. For a 50s version, drop Block B's B4 and B5 (botanicals + palm, 3.6s) and trim D-X in place of D3–D7.

**Refs:** @WESTIE, @OWNER, @RESEARCHER · **10s**

| Shot | Block time | Ad time (if inserted) | VO |
|---|---|---|---|
| I1 | 0:00–2.4 | 27.0–29.4 | "Most itch sprays only numb the surface for a few hours." |
| I2 | 2.4–5.4 | 29.4–32.4 | "Atokong is different. It boosts your dog's skin immunity…" |
| I3 | 5.4–8.0 | 32.4–35.0 | "…so his skin can fight back against the next flare-up." |
| I4 | 8.0–10.0 | 35.0–37.0 | "Not just relief. Lasting protection." |

Suggested supers (post): I2 **SKIN-IMMUNITY FORMULA** · I3 **30 YEARS OF IMMUNE-CELL RESEARCH** · I4 **RELIEF + PROTECTION**.

```
SCENE CONTEXT
A dog owner gives up on the generic itch sprays that never lasted, a Korean researcher studies skin-immunity cells under a microscope, water beads off a dog's healthy, protected skin, and the terrier rolls carefree in pollen-filled grass without scratching.

ACTIVE REFERENCES
@WESTIE: 5-year-old male West Highland White Terrier, compact 8 kg body, clean white coat, brown leather collar with a small round brass tag. 100% matches the reference.
@OWNER: hands and forearms only, thin gold band on the right ring finger, oatmeal knit sleeves. 100% matches the reference.
@RESEARCHER: Korean veterinary researcher in her early 50s, black hair tied back with a few grey strands, thin reading glasses, white lab coat over navy scrubs. 100% matches the reference.

FORMAT MODE
Controlled multi-shot sequence, 10 seconds, four shots, HARD CUTS only at 2.4, 5.4 and 8.0 seconds. No fades, no dissolves, no transition effects. Every shot opens with its subject already in frame.

SHOT I1 — 0:00 to 0:02.4 — THE SPRAYS THAT DIDN'T LAST
First frame: top-down view into an open bathroom drawer crammed with half-used, unbranded pet sprays, ointment tubes and shampoo bottles with plain blank labels; @OWNER's right hand holding one more plain unbranded spray bottle above the drawer.
Optics: 47° diagonal field of view, standard normal lens character, camera 60 cm above the drawer.
Camera: handheld, operator breath, fixed framing.
Action: she drops the bottle into the drawer, where it clatters onto the others, and pushes the drawer shut with the heel of her hand.
Light: flat, slightly cool bathroom light from above.

SHOT I2 — 0:02.4 to 0:05.4 — SKIN-IMMUNITY RESEARCH
First frame: a bright Seoul research lab; @RESEARCHER seated at a laboratory microscope at screen-right in three-quarter view facing screen-left; beside her a monitor shows a real fluorescence microscopy image of skin cells, cell nuclei in blue and cell membranes in green, like a real lab capture.
Optics: 29° diagonal field of view, short telephoto portrait character, camera 2 meters away at seated eye level; her face sharp, background soft.
Camera: handheld documentary drift toward the monitor.
Action: she looks from the eyepieces to the monitor and points with a pen at a cluster of cells on screen, focused and calm. She does not look at the camera.
Light: soft window daylight from screen-left; the monitor adds a faint cool glow on her face.

SHOT I3 — 0:05.4 to 0:08.0 — PROTECTED SKIN
First frame: extreme macro of healthy, calm pale-pink dog skin between parted white fur, @OWNER's fingertips holding the fur open at the top of frame; fine water droplets are falling onto the skin from above.
Optics: 18° diagonal field of view, telephoto macro, razor-thin focus on the skin surface.
Camera: locked off. Half-speed slow motion.
Action: water droplets land on the skin and bead up into tight round beads that roll off the surface, leaving it dry and intact, showing a healthy, protected barrier.
Light: soft daylight from screen-left; bright specular highlights in the beads.

SHOT I4 — 0:08.0 to 0:10.0 — CAREFREE IN ALLERGY SEASON
First frame: sunlit meadow in late afternoon, tall grass and wildflowers; @WESTIE already lying on his back in the grass at frame center, wriggling happily, paws in the air; golden pollen and seed fluff drifting in the backlit air.
Optics: 18° diagonal field of view, classic telephoto lens character, camera at grass level 5 meters away; background compressed into a soft golden wash; razor focus on the dog; close framing achieved through lens reach.
Camera: handheld at grass level, slight tracking.
Action: he rolls happily side to side in the grass, then flips onto his belly, shakes his head and trots toward camera. He never scratches.
Light: low golden sun behind him, a bright rim on his white coat, pollen glowing only from backlight.

CONTINUITY
Same @WESTIE (collar and tag) as the rest of the ad. Same owner's hands and ring. Same researcher as Block B.

PHYSICS
Bottles have real weight and clatter as they land. Water beads have real surface tension and roll off with gravity. Grass bends under the dog's weight; pollen drifts slowly with the breeze.

AUDIO
Natural foley: bottles clattering and the drawer thudding shut (I1); quiet lab hum (I2); soft water patter (I3); grass rustle, a happy snort and a tag jingle, birds (I4). No music.
VOICEOVER
NARRATOR VOICE (identical in every line): one off-screen female narrator, early 30s, natural American English, warm and conversational, like a real dog owner telling a close friend what finally worked. Not an announcer, not salesy, no radio voice. Close, intimate microphone, clean and dry with light room tone, soft natural breaths. Brisk and punchy, about 190 words per minute, with short pauses only at each ellipsis; real emotion: frustrated on the problem lines, relieved and excited on the results, confident on the call to action. Nobody on screen speaks and there is no lip movement. Only the quoted lines are spoken, with no extra words or ad-libs.
0:00.1 to 0:02.3 "Most itch sprays only numb the surface for a few hours."
0:02.5 to 0:05.3 "Atokong is different. It boosts your dog's skin immunity…"
0:05.5 to 0:07.9 "…so his skin can fight back against the next flare-up."
0:08.1 to 0:09.9 "Not just relief. Lasting protection."
Voice sits clearly on top; foley ducks under the voice.

POSITIVE CONSTRAINTS
Real smartphone and documentary texture. No real or readable competitor brands on any bottle. The microscopy image looks like a real lab capture, not a 3D render. No subtitles, no on-screen text, no glow effects, no sparkles.
```

**Compliance (later pass):** "boosts skin immunity" and "lasting protection" are strong functional claims, and "most itch sprays only numb the surface" is a comparative claim. Tie the wording to what PITEN's skin-immunity research actually supports, for example "formulated with skin-immunity ingredients from 30 years of immune-cell research".

---

### Block I alternate: I3 as a high-end CGI "skin shield" scene

A test variant for the attention spike. I3 becomes a premium pharma-commercial-style CGI sequence: the formula activates the skin's immune cells, which form a glowing protective shield that pollen and irritants bounce off. This deliberately breaks the realism rule for one beat, as the competitor did with their cell animations. The difference is that this one is built to look expensive, not cartoonish.

**Two ways to use it**
1. **Standalone (recommended):** generate the prompt below as its own **3s** clip and cut it into Block I over 5.4–8.0. Seedance holds a style switch more reliably as its own generation.
2. **In-block:** paste the **SHOT I3** paragraph at the bottom into Block I in place of the photoreal I3, and change "No glow effects, no sparkles" in Block I's POSITIVE CONSTRAINTS to "No glow effects or sparkles except in shot I3."

Super (post): **SKIN-IMMUNITY SHIELD** · small *Visualization*

```
SCENE CONTEXT
A premium CGI science visualization: Korean botanical formula droplets sink into dog skin, wake up the skin's immune cells, and the cells link together into a glowing protective shield across the skin surface that deflects incoming pollen and irritant particles.

FORMAT MODE
Single continuous take, 3 seconds. One continuous CGI camera move, no cuts.

FIRST FRAME AND SPATIAL BLOCKING
The first visible frame already shows a macro CGI cross-section of skin filling the frame: translucent layered epidermis in soft pink and pearl tones at frame center, white hair shafts rising diagonally at screen-right, and three amber-gold liquid droplets just touching the skin surface at the top of frame. Dark blue-black background above the skin. No empty frame.

OPTICS
Virtual macro camera, 29° diagonal field of view, cinematic shallow depth of field, focus on the skin surface.

CAMERA
A slow, smooth, continuous dolly push down and forward into the skin layers, then rising slightly to a low angle across the surface for the final second. Steady and controlled, high-end commercial motion.

ACTION TIMING
0:00 to 0:01 The amber-gold droplets sink into the skin surface, and soft golden ripples spread through the translucent layers.
0:01 to 0:02 Deep in the skin, small round immune cells light up one by one with a warm amber glow and send thin glowing threads to each other, linking into a network.
0:02 to 0:03 The network rises to the surface and forms a thin, glowing honeycomb shield of amber-gold light over the skin; spiky pollen grains and dust particles drifting down from above hit the shield and bounce away with small sparks, while the skin below stays calm pale pink.

PHYSICS
Liquids have weight and viscosity as they sink. Particles drift with gentle air currents and rebound off the shield with believable momentum. The shield flexes slightly on each impact, like a soft membrane.

LIGHTING
Cinematic volumetric lighting: a cool blue rim from above, a warm amber glow from the formula and the shield, subsurface scattering in the translucent skin layers, soft bloom only on the shield and the activated cells. Rich contrast, deep blacks.

STYLE
Ultra-high-end pharmaceutical and skincare commercial CGI, photoreal materials, Octane or Unreal Engine 5 render quality, banding-free smooth gradients, film-grade detail. Color palette: pearl pink, deep navy, amber-gold accents matching ATOKONG orange.

AUDIO
A deep cinematic whoosh as the droplets sink, a soft rising shimmer as the cells activate, light crystalline taps as particles bounce off the shield. No music.
VOICEOVER
NARRATOR VOICE (identical in every line): one off-screen female narrator, early 30s, natural American English, warm and conversational, like a real dog owner telling a close friend what finally worked. Not an announcer, not salesy, no radio voice. Close, intimate microphone, clean and dry with light room tone, soft natural breaths. Brisk and punchy, about 190 words per minute, with short pauses only at each ellipsis; real emotion: frustrated on the problem lines, relieved and excited on the results, confident on the call to action. Nobody on screen speaks and there is no lip movement. Only the quoted lines are spoken, with no extra words or ad-libs.
0:00.1 to 0:02.7 "…so his skin can fight back against the next flare-up."
Voice sits clearly on top; sound design ducks under the voice.

POSITIVE CONSTRAINTS
Premium, polished CGI throughout, not cartoonish: no faces on cells, no cute characters, no bacteria monsters. No text, no labels, no logos, no UI graphics. The shield is subtle and elegant, not a sci-fi force field.
```

**In-block version (paste into Block I in place of SHOT I3):**
```
SHOT I3 — 0:05.4 to 0:08.0 — SKIN-IMMUNITY SHIELD (CGI)
First frame: a premium CGI macro cross-section of translucent pearl-pink skin layers with white hair shafts rising at screen-right and amber-gold formula droplets touching the surface, dark navy background above. Style switches here to ultra-high-end pharmaceutical commercial CGI, photoreal materials, volumetric light, subsurface scattering.
Optics: virtual macro camera, 29° diagonal field of view, shallow depth of field.
Camera: a slow continuous dolly push into the layers, rising to a low angle across the surface.
Action: the droplets sink in with golden ripples; immune cells deep in the skin light up amber and link with glowing threads; the network rises into a thin glowing honeycomb shield over the surface; spiky pollen and dust particles hit the shield and bounce away while the skin below stays calm.
Light: cool blue rim from above, warm amber glow from the shield and cells, soft bloom only on the shield.
```

---

## BLOCK D-X2 — Extreme transformation, "part the fur" reveal at every stage (standalone, no VO)

A revision of D-X. In D-X the skin state appeared to flash from one stage to the next. Here **every stage opens with the fur lying closed over the spot**, and the owner's fingers **press in and push the fur outward** to reveal that day's skin. The viewer watches the same ritual four times and sees the skin get better each time. The stage changes only at the cuts, while the fur is closed, so nothing morphs on screen.

- **Length:** **8s**. Each reveal needs ~1.3s to read; the paw pair takes the last 1.8s. For a 6s version, drop X5–X6 (the paw).
- **Refs:** @WESTIE, @OWNER, @PATCH (KF-G01). Optional anchors: the severe and full-coat edits from D-X.

```
SCENE CONTEXT
Four identical overhead progress shots of a small white terrier's flank: in each one the owner's fingers push the closed fur outward to reveal the same spot, and each reveal shows the skin further healed, from raw and inflamed to healthy skin under a full white coat, followed by his red, licked-raw paw becoming clean and healthy.

ACTIVE REFERENCES
@WESTIE: 5-year-old male West Highland White Terrier, compact 8 kg body, coarse white coat, lying on his right side with the left flank facing up. 100% matches the reference.
@PATCH: the exact overhead framing of the owner's two hands at the dog's left flank, just forward of the left hip. 100% matches the reference for framing, hands and location.
@OWNER: hands and forearms only, thin gold band on the right ring finger, oatmeal knit sleeves. 100% matches the reference.

FORMAT MODE
Controlled multi-shot sequence, 8 seconds, six shots, HARD CUTS only at 1.6, 2.9, 4.2, 6.2 and 7.1 seconds. No fades, no dissolves, no morphing. X1 to X4 are framed IDENTICALLY, like an owner's daily progress videos: same camera position, framing, hand position and light. Every one of X1 to X4 follows the same reveal action: it OPENS with the fur lying closed and flat over the spot, both fingertips resting on the fur 2 cm apart at frame center; the fingers then press down and slide outward in opposite directions, pushing the fur aside to open a gap and reveal the skin underneath; they hold it open. The skin condition never changes inside a shot, only between shots.

SHOT X1 — 0:00 to 0:01.6 — BEFORE (severe)
First frame: overhead close-up of @WESTIE's left flank, fur closed and lying flat at frame center, the white fur around it visibly thin, matted and stained dark rust-brown; both @OWNER fingertips resting on it.
0:00 to 0:00.8 The fingertips press in and push the fur outward to the sides, opening a wide gap.
0:00.8 to 0:01.6 Hold open: revealed underneath is a raw bald patch about 8 cm wide, angry deep red, swollen at the edges, thick crusty yellow-white scale, crisscrossing scratch tracks, almost no fur. Dry and crusted, no fresh blood, no open wound. The skin twitches once.

SHOT X2 — 0:01.6 to 0:02.9 — DAY 1
Identical camera, framing, hands and light to X1. Opens with the fur closed and flat over the spot, the stain around it lighter.
0:01.6 to 0:02.3 The fingertips push the fur outward to the sides.
0:02.3 to 0:02.9 Hold open: the swelling is gone, the deep red has faded to bright pink, most of the crust is gone, the scratch tracks have softened.

SHOT X3 — 0:02.9 to 0:04.2 — DAY 3
Identical camera, framing, hands and light to X1. Opens with the fur closed and flat over the spot, the surrounding fur now clean white.
0:02.9 to 0:03.6 The fingertips push the fur outward to the sides.
0:03.6 to 0:04.2 Hold open: smooth, even soft-pink skin, no flakes, no crust, no scratch marks, a dense layer of short new white fur growing across the patch.

SHOT X4 — 0:04.2 to 0:06.2 — DAY 5
Identical camera, framing, hands and light to X1. Opens with a full, thick, bright, healthy white coat lying smoothly over the whole area: the bald patch is gone.
0:04.2 to 0:05.0 The fingertips push the thick fur outward to the sides; it resists slightly, dense and springy.
0:05.0 to 0:05.6 Hold open: the skin underneath is healthy, calm, pale pink.
0:05.6 to 0:06.2 The fingers release, and the full coat springs back and closes smoothly over the spot.

SHOT X5 — 0:06.2 to 0:07.1 — PAW BEFORE
First frame: close-up of @WESTIE's right front paw resting in @OWNER's open right palm, toes together, the fur on them soaked, matted and stained dark rust-brown.
0:06.2 to 0:06.6 Her thumb pushes two toes apart.
0:06.6 to 0:07.1 Hold: the skin between the toes is raw-looking, angry red and swollen, with thinned hair. Dry, no wound.
Optics for X5 and X6: 29° diagonal field of view, close detail framing, camera 30 cm away.

SHOT X6 — 0:07.1 to 0:08.0 — PAW DAY 5
Identical framing, hand and light to X5. Opens with the same paw, toes together, the fur now fluffy, clean and bright white.
0:07.1 to 0:07.5 Her thumb pushes the same two toes apart.
0:07.5 to 0:08.0 Hold: calm, healthy pale-pink skin between the toes, no staining, no swelling.

OPTICS
X1 to X4: 29° diagonal field of view, close detail framing, phone 35 cm directly above the coat; the fingertips and the revealed skin razor-sharp.

CAMERA
Very steady handheld, locked framing, no push-in and no reframing in any shot, so the reveals line up exactly from cut to cut.

PHYSICS
The fur parts along its growth direction as the fingers slide outward; hairs at the edge of the gap bend, stand up and spring back. The skin moves slightly under finger pressure. The thin, damaged coat in X1 parts easily and stays clumped; the healthy coat in X4 is dense, resists slightly and springs back fully when released.

LIGHTING
Soft daylight from screen-left, identical in every shot; the fingers cast a soft shadow at screen-right.

AUDIO
A soft fur rustle on each reveal, a subtle camera-shutter tick on each cut, quiet room tone. No music. No voice. No narration.

POSITIVE CONSTRAINTS
Real smartphone progress-video realism; true-to-life skin and fur textures. The skin is only ever seen when the fingers open the fur. No subtitles, no day labels, no text, no split screen. No glow, no sparkles, no blood.
```
