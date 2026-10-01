# Concept 01 — "PART THE FUR"
### ATOKONG™ Pet Skin Mist · Meta Reels / Feed · 9:16 · 1080×1920

**Files in this package**
- `PRODUCTION_PACKAGE.md` (this file): strategy, script, shot-by-shot sequence, hook variations, edit specs, test plan, claims guardrails
- `IMAGE_PROMPTS.md`: still-image generation prompts (references, keyframes, transformation states)
- `VIDEO_PROMPTS.md`: image-to-video prompts for Seedance 2.0 / Higgsfield, written to the CINEDANCE V4 spec in `reference/CINEDANCE_HIGGSFIELD_SKILL.md`

Background: `research/COMPETITOR_ANALYSIS.md` · Product facts: `product/ATOKONG_PRODUCT_BRIEF.md`

---

## 1. The idea in one line

**An owner parts her dog's fur, finds the spot he's been scratching raw, and — instead of another generic itch spray — tries Korean pet dermatology. We watch the itch-scratch cycle break: first in his behavior (he finally lies down), then in his skin and coat, day by day.**

---

## 2. Creative strategy

### 2.1 Audience
Dog (and cat) owners, skewing women 28–55, whose pet has a *recurring* itch problem: hot spots, paw licking, flaky or dry patches, allergy-season flare-ups. Many have already tried something: a generic spray, an oatmeal shampoo, a vet visit, or a steroid course. They are emotionally invested ("it's heartbreaking to watch") and **skeptical of miracle claims** because the problem keeps coming back.

### 2.2 Insight
> *"The worst part isn't the spot. It's hearing him scratch at 2 a.m. and not knowing what actually helps."*

The owner's pain is helplessness plus sleeplessness. The pet's pain is the itch-scratch cycle. The competitor set sells instant magic. The more sophisticated, more-burned buyer wants **something that makes sense**: a real reason it's different and a result that looks real.

### 2.3 Single-minded proposition
**Korean pet dermatology that helps break the itch-scratch cycle.**

### 2.4 Reasons to believe (in on-screen order)
1. **Korean pet dermatology:** a category frame borrowed from K-beauty's reputation for advanced, gentle skincare.
2. **Built by a vet with 20+ years in clinic and a 30-year immune-cell researcher** (backed by PITEN Inc. biotech).
3. **Korean medicinal botanicals:** *Daphne kiusiana* and *Daphne genkwa*.
4. **Non-steroidal. No fragrance. No artificial colorants.**
5. **3–5 sprays, no bath, no rinse:** easy enough to actually do daily.

### 2.5 How the concept uses the competitor intelligence

| Competitor pattern (see analysis) | How we use it | How we beat it |
|---|---|---|
| Lesion + hand in frame 0 (P1, P2) | Frame 0 = fingers already parting fur over the patch | Lesion art-directed to look *clinically real* (irregular, blotchy, flaky, saliva-stained), not a glowing red disc |
| "Part the fur" ritual (P4) | Our hook and our visual through-line: the same gesture opens the ad and reveals every transformation day | Turned into a *repeatable proof device*: same hands, same spot, same framing on Before / Day 1 / Day 3 / Day 5 |
| Instant healing in seconds (P5) | Instant *behavioral* relief: he stops scratching and lies down | Skin and coat improvement shown **over days** with counters, which is believable and on-brief ("rapid itch relief, visible improvement over continued use") |
| CG mechanism (rings, frost, cartoon cells) (P6) | Replaced by authority shots: vet exam, lab, botanicals | Photographic, not CG. This removes the competitor's most "AI-looking" footage |
| Behavior reframe (P7) | Folded into the itch-scratch cycle beat | Uses the brand's own angle #2 |
| Ease objection (P8) | "3–5 sprays on dry skin. No bath. No rinse. Nothing to rub in." | Same |
| Gentleness, dogs + cats (P9) | Mist on palm + cat cameo | Plus *specific* free-froms (non-steroidal, fragrance-free) |
| Emotional payoff (P10) | "More sleep — for both of us" | Owner's sleep, not just the dog's: the real insight |
| Bundle offer (P11) | End card `[OFFER]` | Pending the client's offer |
| First-person VO, ~190 wpm (P13) | First-person owner VO at ~170 wpm | Slightly slower so the authority lines land |

### 2.6 Emotional arc
**Recognition** (that's my dog) → **guilt/urgency** (it's worse than I thought) → **hope with a reason** (Korean dermatology, vet + researcher) → **relief** (he lies down) → **proof** (day-by-day) → **joy and rest** → **action**.

### 2.7 What makes this the strongest conversion bet (hypotheses)
- Keeps every structural element the competitor repeats most (H1, H2, H5, H6, H7), so we are not gambling on the format.
- Adds the one thing the whole competitor set lacks: **a reason to believe this product is different**. That gives a premium-priced product room to convert people who've "tried a spray before".
- The day-counter transformation is **more credible and more re-watchable** than a 2-second morph. Viewers pause and compare days, which helps hold rate.
- Behavioral relief ("he just lay down") is something every owner can picture, and it doesn't depend on a skin-healing claim.

---

## 3. Format and technical specs

| Spec | Value |
|---|---|
| Aspect / resolution | 9:16, 1080×1920 |
| Frame rate | 30 fps (generate at the model's native rate and conform in edit) |
| Length | **Main: ~47s.** Cutdowns: 30s and 15s (section 7) |
| Pace | New shot every ~1.2–2.6s (median ~1.8s); one 3.6s "breath" shot (S15) |
| VO | Single female voice, early 30s, warm, plain-spoken, first person. ~170 wpm. Human VO artist or a high-quality voice model, with no "announcer" read |
| Music | Soft, warm, minimal (felt piano / muted guitar / light pulse), ducked about 18 dB under VO. It rises only in the transformation beat (S16–S19) and the end card |
| SFX (critical for realism) | Collar-tag jingle, nails scratching fur, paw licking, the *tss-tss-tss* of the pump mist, dog exhale/sigh, room tone. Mix SFX hot. The spray sound is a sensory hook |
| Captions | Burned-in, word-by-word, current word highlighted with an ATOKONG-orange `#F2A21B` box and black text (color sampled from the packshot). Bold rounded sans, ~64px at 1080w, 2 lines max |
| Safe zones (Reels) | Keep captions and key action between ~14% from the top and ~35% from the bottom. Captions sit at ~55–62% of frame height. Hook headline sits in the upper third, below the top 14% |
| Supers | Small-caps clean sans, white with a 20% black shadow. Never more than 6 words |
| Disclosure | "AI-generated content" label applied in Meta, plus a "Dramatization. Individual results may vary." super during the transformation (S16–S20) |

---

## 4. Realism bible (no "AI look")

The competitor ads look AI-made mainly in their CG devices and their too-perfect lesions. The rules below keep us on the right side of that line.

1. **Phone-camera grammar, not cinema grammar.** Everything should look like a capable owner filmed it on a recent phone: handheld micro-movement, natural window light, occasional slight focus breathing, no anamorphic flares, no shallow "AI portrait" bokeh on wide shots.
2. **One hero dog, locked identity.** Same Westie in every shot (`@WESTIE` reference sheet), with the same collar and brass tag. Re-generate any shot where the face, coat or size drifts.
3. **Lesions are clinical, not graphic.** Irregular, asymmetric edges. Blotchy pink-to-red, not a uniform red. Fine linear scratch marks, dry white scale at hair roots, broken short hairs, faint rust-brown saliva staining on the surrounding white fur. Matte and dry. **No blood, open wounds, pus or gloss.** This is more believable, and Meta's policies on sensational or shocking imagery can reject graphic skin.
4. **No glowing rings, sparkles, frost particles, X-rays or cartoon cells.** Proof comes from photography: mist droplets, the day-counter series, the dog's behavior.
5. **Short AI clips.** Use 1.2–2.6s of each generation, taken from its most stable middle section. Dogs and hands drift as generations run long.
6. **Hands are simple.** One hand parts the fur; the other holds the bottle. Keep fingers in plain, relaxed poses and re-roll any extra or merged fingers.
7. **Product label: real, never AI.** The AI will garble the label. For S06, S07 and S24, shoot the real bottle on a phone (best) or composite the real packshot. In other AI shots, keep the bottle label turned away, cropped or out of focus.
8. **One consistent grade.** Neutral-warm daylight, slightly lifted blacks, soft contrast. Add a light film/sensor grain (~3–5%) across *all* shots in post so AI and real footage match. Avoid HDR, crushed saturation and oversharpening.
9. **Day-counter shots are locked off.** Identical framing, light and hand pose across Day 1 / 5 / 12 / 21, like a real owner's progress photos. Create Days 5–21 as **edits of the Day 1 image** (see `IMAGE_PROMPTS.md`) so nothing but the skin and fur changes.
10. **Hybrid shoot recommended.** Any shot without a dog can be filmed for real in an afternoon with a phone: the product pickup, mist on palm, botanical close-ups (or stock), and the end-card bottle. Real footage spliced between AI shots makes the AI shots read as real.

---

**Product appearance:** see `product/images/atokong_packshot_bottle_box.jpg` and brief §4. It's a small 30 ml white bottle with an orange cartoon-dog label and Korean text. Keep its real (palm-sized) scale. The Korean label supports the "Korean pet dermatology" story, so let it read in S06, S07 and S24.

## 5. Full script

**Voice:** first-person owner, intimate, unhurried at the start, quickening slightly through the demo, warm at the end.
**[ ]** = on-screen super (separate from the word-by-word captions).

| # | Time | VO | Supers |
|---|---|---|---|
| 1 | 0.0–3.2 | If your dog keeps scratching the same spot… part the fur. | **[PART THE FUR.]** |
| 2 | 3.2–5.0 | This kept him up all night. | |
| 3 | 5.0–8.4 | Every scratch made the itch worse… and round it went. | **[THE ITCH–SCRATCH CYCLE]** |
| 4 | 8.4–12.0 | So I stopped guessing… and tried Korean pet dermatology. | **[ATOKONG · KOREAN PET DERMATOLOGY]** (from 10.2) |
| 5 | 12.0–17.8 | Created in Korea by a vet with twenty-plus years in clinic… and a thirty-year immune-cell researcher. | **[VET · 20+ YEARS IN CLINIC]** → **[30 YEARS IMMUNE-CELL RESEARCH]** → **[REGISTERED VETERINARY QUASI-DRUG · KOREA]** |
| 6 | 17.8–19.2 | With Korean medicinal botanicals. | **[Daphne kiusiana · Daphne genkwa]** |
| 7 | 19.2–21.0 | No steroids. No fragrance. Lick-safe. | **[NON-STEROIDAL · FRAGRANCE-FREE · LICK-SAFE]** |
| 8 | 21.0–23.6 | Three to five sprays on dry skin. | **[3–5 SPRAYS]** |
| 9 | 23.6–26.4 | Korean botanicals get to work, soothing the skin and supporting its natural barrier. | **[KOREAN BOTANICAL FORMULA]** + small: *Visualization* |
| 10 | 26.4–27.8 | No bath. No rinse. Nothing to rub in. | |
| 11 | 27.8–31.0 | From the very first spray… he stopped scratching and just lay down. | |
| 12 | 31.0–36.2 | By day three, the redness had calmed… by day five, his skin looked like his again. | **[BEFORE] [DAY 1] [DAY 3] [DAY 5]** + small: *Dramatization. Individual results may vary.* |
| 13 | 36.2–37.8 | Even his paws. | **[BEFORE / DAY 5]** |
| 14 | 37.8–39.6 | Less scratching. Less licking. | |
| 15 | 39.6–41.4 | More sleep — for both of us. | |
| 16 | 41.4–43.0 | And it's made for cats, too. | **[FOR DOGS & CATS]** |
| 17 | 43.0–48.2 | Atokong. Scratch less, lick less, live more. `[OFFER LINE, e.g. "Buy two, get one free."]` Tap below. | End card: logo · **Stop Scratching.** · `[OFFER]` · **Free shipping** `[if applicable]` · **Shop Now ↓** |

Word count ≈ 142 (+ offer) over 48s, about 170 wpm.

**Claims check.** Every VO line maps to the brief. "He just lay down" is a dramatized behavioral moment supporting "rapid itch relief". Instant relief from the first spray is client-confirmed (customers report it). The 5-day sequence shows calmer skin, not full fur regrowth. Visible regrowth takes weeks, and showing a full coat at day 5 would look fake and overclaim.

---

## 6. Shot-by-shot sequence

**Source key:** `AI` = generate (keyframe in `IMAGE_PROMPTS.md`, motion in `VIDEO_PROMPTS.md`). `REAL` = phone shoot recommended. `COMP` = real product composited into an AI plate.

| Shot | Time (dur) | Visual | Camera | VO / SFX | Gen ID | Source |
|---|---|---|---|---|---|---|
| **S01** | 0.0–1.6 (1.6) | **FRAME 0:** owner's fingertips already pressed into the Westie's white coat on his left flank, spreading it open. A ~6 cm irregular Day 1 patch shows: blotchy red-pink, scratch lines, white flakes at hair roots, rust-stained fur edges. Fingers spread wider, revealing the full patch | Handheld, phone close-up from above at ~35 cm, slight push-in | "If your dog keeps scratching the same spot…" · SFX: fur rustle, dog breathing, tag jingle | G01 | AI |
| **S02** | 1.6–3.2 (1.6) | Tighter macro of the same patch: flakes on hair shafts, broken hairs, scratch lines. The dog's skin twitches (panniculus reflex) under the fingers | Macro, handheld, very slow drift | "…part the fur." | G01 (2nd half) or G01B | AI |
| **S03** | 3.2–5.0 (1.8) | Night bedroom, cool moonlight through blinds. The Westie sits on his dog bed at the foot of the owner's bed, scratching his left flank hard with a hind leg. Owner in bed (soft background) lifts her head | Static on floor-level side table, slight handheld feel | "This kept him up all night." · SFX: rhythmic tag jingle, thumping | G02 | AI |
| **S04** | 5.0–6.6 (1.6) | Slow-motion macro: hind claws rake through white fur over the patch. Fine white flakes lift and drift through a sliver of lamp light | Macro, locked | "Every scratch made the itch worse…" · SFX: dry scratching, slowed | G03 | AI |
| **S05** | 6.6–8.4 (1.8) | Day, living room rug: the Westie licks and nibbles between the toes of his right front paw. Rust-brown saliva staining on white toe fur | Low, handheld at rug level, 1 m | "…and round it went." · SFX: wet licking | G04 | AI |
| **S06** | 8.4–10.2 (1.8) | Owner's hand lifts the ATOKONG bottle off a sunlit white shelf with a small trailing plant | Handheld, chest height | "So I stopped guessing…" | G05 | **REAL** (or COMP) |
| **S07** | 10.2–12.0 (1.8) | On the rug, the owner holds the bottle toward the Westie at nose height. He sniffs it, ears forward. Label faces camera | Handheld, low 3/4 | "…and tried Korean pet dermatology." | G06 | COMP (real bottle) |
| **S08** | 12.0–14.0 (2.0) | Vet clinic exam table: a veterinarian's gloved hands (navy scrub sleeves, no face) part a white dog's fur under a round magnifier lamp to inspect the skin | Handheld over-shoulder, medium close | "Created in Korea by a vet with twenty-plus years in clinic…" | G07 | AI |
| **S08b** ⭐ | 14.0–16.0 (2.0) | **Korean vet-researcher b-roll:** a Korean veterinary researcher in her 50s, white lab coat over navy scrubs, hair tied back, reading glasses, in a bright Seoul research lab. She looks up from a microscope, then turns to examine a small glass vial of the formula against the window light. Calm, expert, real | 29° portrait, handheld, slow drift | "…and a thirty-year immune-cell researcher." (VO continues) · SFX: lab hum | G07B | AI (or **REAL**: film the actual vet/researcher if available) |
| **S09** | 16.0–17.8 (1.8) | Lab bench: a gloved hand pipettes one drop of pale amber botanical extract into a small glass vial. A rack of vials and a microscope are soft in the background | Macro, locked, shallow focus | (VO tail) · Super: **REGISTERED VETERINARY QUASI-DRUG · KOREA**, + 0.8s certificate insert (§6.2) · SFX: soft lab hum, drip | G08 | AI |
| **S10** | 17.8–19.2 (1.4) | Macro: dense clusters of small white, four-lobed tubular *Daphne kiusiana* flowers among glossy dark-green leaves, morning dew, soft forest light | Macro, slight breeze sway | "With Korean medicinal botanicals." | G09 | AI (or stock) |
| **S11** | 19.2–21.0 (1.8) | Backlit: the owner sprays the mist onto her open palm. The fine cloud catches window light, droplets bead on skin. Clean, colorless | Handheld, side-backlit | "No steroids. No fragrance." · SFX: single *tss* | G10 | **REAL** (or AI) |
| **S12** | 21.0–23.6 (2.6) | **Demo:** the same flank. Left hand parts the fur over the patch; the right hand sprays 3 pumps from ~12 cm. The mist cloud drifts down onto the skin | Handheld close-up, 3/4 above | "Three to five sprays on dry skin." · SFX: *tss-tss-tss* (mix hot) | G11 | AI |
| **S13b** *(optional insert)* | — | 0.8s: the Westie licks his freshly misted paw, no reaction; owner relaxed. Super: **LICK-SAFE** | Low macro | supports VO 7 | G04 variant | AI |
| **S13** ⭐ | 23.6–26.4 (2.8) | **MACRO SCIENCE DIVE:** starts on fine droplets settling on the pink skin, then the camera pushes *through* the surface into a photoreal microscopy-style cross-section of the skin layers. The droplets' clear liquid seeps into the gaps between the irritated, slightly lifted surface cells; the cell layer flattens and closes up and the deep red tone cools to a calm pale pink. Looks like a real lab microscope / documentary micro-photography, not a CG cartoon | Macro push-in | "Korean botanicals get to work, soothing the skin and supporting its natural barrier." · Super: *Visualization* | G12 (first frame) → G12-SCI (first+last frame) | AI |
| **S14** | 26.4–27.8 (1.4) | Owner sets the bottle down on the rug. The Westie stands, gives a short full-body shake and trots two steps toward the sunny window | Low handheld, 1.2 m | "No bath. No rinse. Nothing to rub in." · SFX: shake, tag jingle | G13 | AI |
| **S15** | 27.8–31.0 (3.2) | **Relief beat, minutes after the first spray:** in a patch of sun on the rug, the Westie lies down, exhales a long sigh (chest falls, nostrils flare), lowers his chin onto his front paws, and his eyes slowly close. Owner's hand strokes his back once | Low static at rug level, 1.5 m, long-lens feel | "From the very first spray… he stopped scratching and just lay down." · SFX: long dog sigh, room tone | G14 | AI |
| **S16** | 31.0–32.0 (1.0) | **BEFORE:** exact S01 framing. Fingers part the fur; the patch is raw | Locked, matches S01 | "By day three…" · SFX: soft camera-shutter tick on each day change | G15-D0 | AI |
| **S17** | 32.0–33.2 (1.2) | **DAY 1** (after first sprays): same framing. Redness already a shade softer, the angry dark-red center gone, flakes reduced | Locked | "…the redness had calmed…" | G15-D1 | AI |
| **S18** | 33.2–34.4 (1.2) | **DAY 3:** same framing. Soft even pink, scratch lines faded, almost no flakes | Locked | "…by day five…" | G15-D3 | AI |
| **S19** | 34.4–36.2 (1.8) | **DAY 5:** same framing. Calm pale-pink skin close to normal, no flakes, staining gone; the surrounding fur lies clean and flat over the edges and a faint new fuzz is just starting | Locked | "…his skin looked like his again." | G15-D5 | AI |
| **S20** | 36.2–37.8 (1.6) | Split screen, top/bottom: right front paw held in the owner's palm. **BEFORE** rust-stained toes and pink webbing; **DAY 5** calm skin, staining fading | Locked macro ×2 | "Even his paws." | G16 | AI |
| **S21** | 37.8–39.6 (1.8) | Morning garden: the Westie sprints toward camera across the lawn, ears up, tongue out, collar tag bouncing | Telephoto feel, low, tracking slightly | "Less scratching. Less licking." · SFX: paws on grass, jingle | G17 | AI |
| **S22** | 39.6–41.4 (1.8) | Night bedroom (same as S03): the Westie asleep, curled on his bed, chest slowly rising. The owner asleep in soft background. Still | Static, same position as S03 | "More sleep — for both of us." · SFX: quiet breathing, distant clock | G18 | AI |
| **S23** | 41.4–43.0 (1.6) | Sofa: grey British Shorthair cat. The owner's hand parts the fur at the side of the neck and sprays once from 15 cm, away from the face. The cat slow-blinks | Handheld close, eye level | "And it's made for cats, too." · SFX: *tss*, purr | G19 | AI |
| **S24** | 43.0–48.2 (5.2) | **End:** the healed Westie sits on the white duvet in morning light, the ATOKONG bottle upright in the foreground, the cat lounging behind. At 44.2 the end card animates in over the top: logo, "Stop Scratching.", `[OFFER]`, Shop Now ↓ | Static, eye level with the dog | "Atokong. Scratch less, lick less, live more. [Offer.] Tap below." · Music swell, final *tss* | G20 | COMP |

**Continuity.** The patch is always on the **left flank, just forward of the left hip**. The paw is always the **right front**. The owner's ring is always on the **right hand**. The window is always **camera-left** in the living room.

---

### 6.1 Timing
The Korean vet-researcher b-roll (S08b) and the shorter 5-day sequence are folded into the timeline above. **Total: 48.2s.** To land at 45s, cut S11 (mist on palm) and trim S15 to 2.8s.

**Using an AI person as "the researcher":** S08b is a dramatized, unnamed figure. Don't caption her with the real founders' names or imply she is them; add *Dramatization*. If the real vet or researcher can be filmed for 10 minutes on a phone, use that instead. Real experts beat any AI shot.

### 6.2 Korean registration / certification on screen (post-production)
Yes, use it. The competitor set has no third-party proof at all, so this is a real advantage. Put it on screen in three places:
1. **Authority beat (S09, 14.4–16.6):** add a super under the lab shot: **REGISTERED VETERINARY QUASI-DRUG · KOREA**. In the last 0.6s, cut to a 0.8s insert: the real certificate (scan or phone photo of the document on a desk) with a slow push-in, key line and official seal visible, personal or sensitive numbers blurred. Use the **real document only**; never generate a certificate with AI.
2. **Product shots (S07, S24):** the label already says 동물용의약외품. Add a small callout arrow + "Registered in Korea" pointing to it.
3. **End card:** a small trust badge row: *Registered in Korea · Non-steroidal · Lick-safe*.

Wording guardrails: say exactly what the certificate says ("registered as a veterinary quasi-drug in Korea"). Don't translate it into "FDA-approved", "vet-approved" or "approved in the US/UK", which are different regulators. Keep the scan file in `product/images/` for anyone checking claims.

### 6.3 About the science shot (realism and claims)
- This shot deliberately bends the "no CG" rule in §4, so it has to be made in the **style of real microscopy**: muted natural colors, soft depth of field, fine organic texture, slight imperfection. No neon glow, energy rings, sparkles, cartoon cells or hologram graphics. Those are what made the competitor mechanism shots look AI-made.
- Label it with a small *Visualization* super so it isn't read as real footage of this dog's skin.
- Keep the VO to soothing and barrier support. Don't say "heals from the inside", "repairs" or "penetrates deep".

## 7. Cutdowns

**30s ("Proof"):** S01, S02 (VO 1) → S04, S05 (VO 3) → S07 (VO 4) → S08 (short: "Made by a vet and an immune-cell researcher.") → S12 (VO 8) → S15 (VO 11) → S16–S19 (VO 12) → S22 (VO 15) → S24 (VO 17).

**15s ("Hook + Proof"):** S01 (VO: "Itchy dog? Part the fur.") → S12 ("Korean pet dermatology. Three to five sprays.") → S16–S19 (no VO, day counters + music) → S24 ("Atokong. Stop scratching. Tap below.").

---

## 8. Hook variations for testing

Each hook replaces **0.0–3.2s** (S01–S02 and VO line 1). From S03 onward the body is identical, so results isolate the hook. Each tests a different hypothesis from the competitor analysis.

### H1 — "Part the Fur" (control)
- **Visual:** S01–S02 as scripted.
- **VO:** "If your dog keeps scratching the same spot… part the fur."
- **Headline super:** PART THE FUR.
- **Tests:** H2, the participatory reveal (the competitor's most-reused device), done more realistically.

### H2 — "2 A.M."
- **Visual:** near-black bedroom. Only phone-screen glow lights the owner's face from below as she lifts her head off the pillow (0–1.2s). Cut to the Westie scratching at the foot of the bed in moonlight (1.2–3.2s).
- **Audio first:** 0.4s of rhythmic collar-tag jingle and thumping *before* any VO.
- **VO:** "If you know this sound at 2 a.m.…"
- **Super:** 2:14 AM. AGAIN.
- **Gen:** G-H2 (see prompts) + G02.
- **Tests:** a sound-led, owner-pain hook (the insight) vs. a lesion-led hook. Sound-off viewers still get the super and the scratching.

### H3 — "Watch This Spot" (product in frame 0)
- **Visual:** frame 0 already shows the nozzle misting the Day 1 patch while fingers hold the fur open (S12 framing, Day 1), with a slow push-in.
- **VO:** "This is Korean skincare… for itchy dogs."
- **Super:** KOREAN SKINCARE. FOR DOGS.
- **Gen:** G11 (use its first 3s).
- **Tests:** H1, product + lesion + hand in frame 0 (the competitor's dominant opener), plus the origin claim up front.

### H4 — "K-Beauty Shelf"
- **Visual:** close-up of a bathroom shelf of unbranded Korean-style skincare (glass dropper serums, toner, cushion compact; no readable brands). A hand passes over them and picks up the ATOKONG bottle. Hard cut to the Westie scratching.
- **VO:** "I trust Korean skincare with my face… so why not my dog's itchy skin?"
- **Super:** K-BEAUTY… FOR YOUR DOG?
- **Gen:** G-H4 (REAL recommended).
- **Tests:** the Korean-origin halo as a pure curiosity hook. Likely strongest with women 25–45 who already buy K-beauty.

### H5 — "Same Spot, 5 Days"
- **Visual:** split screen top/bottom. **BEFORE** (S16 frame) above, **DAY 5** (S19 frame) below. Fingers part the fur in both halves simultaneously.
- **VO:** "Same spot. Five days apart."
- **Super:** BEFORE / DAY 5 · *Dramatization*
- **Gen:** G15-D0 + G15-D5.
- **Tests:** H3, proof-first. **Requires the timeline sign-off in brief item 3.2.**

### H6 — "Not a Bad Habit"
- **Visual:** extreme close-up of the Westie obsessively licking between his toes (S05), with a slow push-in.
- **VO:** "Constant paw licking isn't always just a habit."
- **Super:** NOT JUST A HABIT.
- **Gen:** G04.
- **Tests:** H4, the behavior reframe, to widen the audience to owners who don't think "skin problem".

### H7 — "The Vet and the Scientist"
- **Visual:** S08 (vet gloved hands parting fur under a magnifier lamp) → quick cut to S09 (pipette drop).
- **VO:** "A vet and an immune-cell researcher made one spray… for itchy skin."
- **Super:** 50+ YEARS OF COMBINED EXPERTISE
- **Gen:** G07 + G08.
- **Tests:** an authority-first open (brand angle #6). Nothing like it exists in the competitor set.

### H11 — "Inside the Skin" (science-first)
- **Visual:** frame 0 is the S12 spray already misting the patch; at 0.8s it hard-cuts into the S13 science dive.
- **VO:** "Here's what Korean pet skincare does under the fur."
- **Super:** KOREAN PET DERMATOLOGY · *Visualization*
- **Tests:** a mechanism/curiosity hook built on the competitor's cell-animation idea, done photoreal.

### H10 — "Lick-Safe"
- **Visual:** the owner mists the Westie's front paw (Day 1 paw); he licks it straight away; the owner doesn't react.
- **VO:** "Yes, he licked it. That's fine — it's lick-safe."
- **Super:** LICK-SAFE. NON-STEROIDAL.
- **Tests:** turns the biggest safety worry for paw-lickers into the hook. C01/C06 used it as a body claim; none lead with it.

### H8 — "Non-Steroidal"
- **Visual:** S01 framing, but the owner's other hand holds the ATOKONG bottle beside the patch. Slight push-in.
- **VO:** "Looking for a non-steroidal way to care for your dog's itchy skin?"
- **Super:** NON-STEROIDAL ITCH CARE
- **Gen:** G01 + G11 frame.
- **Tests:** the steroid-wary segment (brand angle #7).

### H9 (bonus) — Cat version
- **Visual:** a grey British Shorthair over-grooming a thinning patch on its flank. The owner parts the fur.
- **VO:** "If your cat keeps licking the same spot… part the fur."
- **Note:** run as a separate cat-owner ad set. The body needs cat-specific swaps (S12–S19 recut with the cat).

---

## 9. Test plan

**Phase 1: hook test (week 1–2)**
- One ad set, broad targeting (or Advantage+), the same body with **H1–H6** as six ads. Keep H7 and H8 for round two.
- Primary read: **hook rate** (3-second plays ÷ impressions) and **hold rate** (ThruPlays ÷ 3-second plays). Decision metrics: **link CTR**, **CPA / cost per purchase**, **ROAS**.
- Give each hook ~2–3× target CPA in spend before cutting. Kill clear losers on hook rate early; judge survivors on CPA.

**Phase 2: body/angle test**
- Winning hook × two bodies: (a) this body (Korean dermatology + authority), (b) a "cycle-led" body that expands S03–S05 and shortens the authority section. This tells us whether the Korean/expert story is pulling its weight.

**Phase 3: offer and end card**
- Winning ad × offer variants (e.g. bundle vs. single + free shipping), plus a seasonal end card (the competitors are running Halloween cards right now).

**Qualitative signal:** watch comments for "this is AI" or "fake". A spike means the realism rules in section 4 need tightening on the offending shots.

---

## 10. Claims and policy guardrails

| Say | Don't say / show |
|---|---|
| "helps soothe", "calmer-looking skin", "itch relief", "fast relief" | "heals", "cures", "treats", "infection", "stops itching instantly", "in 8 seconds" |
| "non-steroidal", "no fragrance", "no artificial colorants" | "chemical-free" or "100% natural" (ethanol and other synthetics are in the INCI list) |
| "created by a vet with 20+ years in clinic and a 30-year immune-cell researcher" | "vet-recommended" or "clinically proven" (unless substantiated) |
| Day counters only with timeline substantiation, labelled *Dramatization* | Instant morphs of skin healing in under 3 seconds |
| Spray on the flank, belly, paws, or the side of a cat's neck from 10–15 cm | Spraying into eyes, ears or mouth, or toward the face |
| Realistic, clinical-looking irritation | Blood, open wounds, pus, gore (sensational-content rejection risk) |
| "Dramatization. Individual results may vary." + Meta AI label | Presenting AI people as the real Atokong vet/researcher, or as real customers |

---

## 11. Production order (recommended)

1. **References:** generate `@WESTIE`, `@OWNER` hands, `@LIVINGROOM`, `@BEDROOM` and `@CAT` reference images (IMAGE_PROMPTS §A). Get the product packshots from the client (`@ATOKONG`).
2. **Day 1 master frame (KF-01).** Lock this before anything else; Day 1/3/5 are edits of it.
3. **Keyframes** for every Gen ID (IMAGE_PROMPTS §B), then the transformation states (§C).
4. **Video** from each keyframe (VIDEO_PROMPTS). Generate 3–4 takes per shot and pick the most physically convincing.
5. **Real shoot:** S06, S11, S24 bottle plate, H4 shelf.
6. **Edit:** rough cut to VO → captions → SFX → music → grade + grain → end card.
7. **Hooks:** export H1–H6 as separate files with an identical body.
