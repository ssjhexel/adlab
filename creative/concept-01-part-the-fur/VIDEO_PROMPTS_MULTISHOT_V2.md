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
| Result | "…his skin looked like his again." | "Day one… redness calming. the redness faded… the flaking stopped… and his skin healed." ⚠ | C01 "recovers within a week", C06 "in just days" |
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

**Hook swaps:** replace the A1 paragraph with the matching alternate under "Block A hook variants" below. Everything else stays the same.

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

### Block A hook variants (swap the A1 paragraph only)

**H2 — 2 A.M.** (also change the first VOICEOVER line to `0:00.4 to 0:03.0 "If you know this sound at 2 a.m.…"`)
```
SHOT A1 — 0:00 to 0:03.2 — 2 A.M.
First frame: an almost dark bedroom; a tired woman lifts her head off a white pillow, her face lit only from below by the cold glow of a phone screen, looking toward the foot of the bed at screen-right.
Optics: 47° diagonal field of view, standard normal lens character, camera 1 meter away at pillow height.
Camera: handheld, slight low-light micro-movement.
Action: she squints at the phone, lifts her head and stares toward screen-right, then exhales, tired. From 0:00, an off-screen rhythmic collar-tag jingle and thumping are heard from screen-right.
Light: phone-screen glow as the only key; faint blue moonlight stripes on the wall; heavy low-light noise.
```

**H3 — Spray first** (first VOICEOVER line → `0:00.2 to 0:03.0 "This is Korean skincare… for itchy dogs."`)
```
SHOT A1 — 0:00 to 0:03.2 — SPRAY FIRST
First frame: the same overhead close-up of the irritated patch on @WESTIE's left flank, @OWNER's left hand already spreading the fur, her right hand holding @ATOKONG 12 cm above the patch with the nozzle aimed down and the label turned away; a fine mist cloud is already leaving the nozzle.
Optics: 29° diagonal field of view, close detail framing.
Camera: handheld, slow push-in.
Action: two more pumps; the colorless mist drifts down and settles on the fur and skin.
Light: soft window daylight from screen-left; the mist is lit from the side.
```

**H6 — Not just a habit** (first VOICEOVER line → `0:00.2 to 0:03.0 "Constant paw licking isn't always just a habit."`)
```
SHOT A1 — 0:00 to 0:03.2 — PAW LICKING OPEN
First frame: extreme close-up at rug level of @WESTIE licking between the toes of his right front paw, rust-brown staining on the white toe fur.
Optics: 29° diagonal field of view, close detail framing, camera 50 cm away.
Camera: handheld, slow push-in.
Action: obsessive repetitive licking and one nibble; his eyes stay half closed.
Light: soft window daylight from screen-left.
```
*(With H6, shorten A4 to a reaction close-up so the paw licking doesn't repeat.)*

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
| D3 | 4.6–5.6 | 31.6–32.6 | "Day one… redness calming." · super **BEFORE** |
| D4 | 5.6–6.8 | 32.6–33.8 | "Day three… flakes gone." · super **DAY 1** |
| D5 | 6.8–8.0 | 33.8–35.0 | "Day five…" · super **DAY 3** |
| D6 | 8.0–9.8 | 35.0–36.8 | "…brand-new, healthy skin." · super **DAY 5** + *Dramatization. Individual results may vary.* |
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
0:04.7 to 0:05.5 "Day one… redness calming."
0:05.7 to 0:06.7 "Day three… flakes gone."
0:06.9 to 0:07.9 "Day five…"
0:08.1 to 0:09.7 "…brand-new, healthy skin."
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
