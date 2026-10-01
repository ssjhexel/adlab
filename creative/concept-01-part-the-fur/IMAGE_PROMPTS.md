# Concept 01 "PART THE FUR" — Still-Image Generation Prompts

These prompts are model-agnostic: Nano Banana Pro, Seedream, GPT-Image, Higgsfield Soul and similar.
- **Aspect ratio: 9:16 vertical** for every keyframe. Generate at the highest available resolution (≥1080×1920).
- **§A** builds reusable references. **§B** builds the first frame for every video generation (Gen IDs match `PRODUCTION_PACKAGE.md` §6 and `VIDEO_PROMPTS.md`). **§C** builds the transformation states as **edits** of one master frame.
- When your tool supports reference images, attach the ones listed under **Refs** for each prompt.

---

## Global blocks (append to every prompt)

**REALISM SUFFIX** (append to every §B/§C prompt):
```
Candid vertical smartphone photo taken by the pet owner on the main camera of a recent iPhone, natural available light, true-to-life color, soft natural contrast, slight sensor noise in the shadows, mild lens vignetting, real depth of field for a phone main camera (background soft but recognizable, not creamy portrait-mode blur). Individual fur strands visible with natural clumping, a few stray hairs and lint, small real-world imperfections (rug fibers, knit pilling, faint dust). Unretouched, documentary, everyday home realism.
```

**AVOID** (paste into the negative field if your tool has one; otherwise append as "Avoid: …"):
```
CGI, 3D render, illustration, cartoon, plastic or waxy fur, airbrushed skin, glossy over-smooth surfaces, HDR look, oversaturated colors, glowing effects, sparkles, lens flares, studio lighting, beauty lighting, cinematic color grade, perfect symmetry, extra fingers, merged fingers, deformed paws, extra legs, duplicate animals, text, watermark, logo, garbled label text, blood, open wound, pus, gore.
```

---

## §A — Reference images

### REF-WESTIE-1 — Hero dog identity (side)
**Use for:** `@WESTIE` identity in all dog shots. Keep the coat healthy here; skin states are added per shot.
```
Full-body left side view of a 5-year-old male West Highland White Terrier standing calmly on a cream wool rug in a bright living room, head turned slightly toward camera. Compact sturdy body about 8 kg, coarse white double coat with slightly creamy tips, natural un-groomed length (not show-trimmed), dark almond-shaped eyes, black nose, black pigmented lips, small upright pointed ears. Worn soft brown leather collar with one small round brass ID tag. Soft daylight from a large window camera-left. Camera at the dog's shoulder height, 1.5 meters away.
```
+ REALISM SUFFIX

### REF-WESTIE-2 — Hero dog identity (face, 3/4)
```
Close portrait of the same 5-year-old male West Highland White Terrier from REF-WESTIE-1, three-quarter view facing camera-right, sitting on a cream wool rug. Coarse white coat slightly creamy at the tips, natural fur around the eyes and muzzle with very faint light-tan tear staining, dark almond eyes with a small window catchlight, black nose with visible texture, upright ears. Worn brown leather collar with a small round brass ID tag. Soft window daylight from camera-left. Camera at eye level, 60 cm away.
```
Refs: REF-WESTIE-1 · + REALISM SUFFIX

### REF-OWNER — Owner's hands and wardrobe
**Use for:** `@OWNER`. Face never shown clearly (it appears only soft and out of focus in S03/S22).
```
Close photo of a woman's two hands resting on a white dog's back, seen from above. Woman in her early 30s, natural light-medium skin tone, short clean unpolished nails, a thin plain gold band on the ring finger of her right hand, oatmeal-colored chunky cable-knit sweater with the sleeves pushed up to mid-forearm. Relaxed natural finger poses, five fingers per hand clearly separated. Soft window daylight.
```
+ REALISM SUFFIX

### REF-LIVINGROOM — Location plate
```
Vertical photo of a bright, lived-in modern apartment living room. Large window on the left side of frame with sheer white curtains and soft daylight, light oak floorboards, a cream wool rug in the center, a grey linen sofa against the back wall with a knitted throw, a small round side table with a trailing pothos plant, a dog toy on the floor. Calm, neutral, warm-white color palette. Camera at seated eye height, 3 meters from the sofa.
```
+ REALISM SUFFIX

### REF-BEDROOM-NIGHT — Location plate
```
Vertical photo of a bedroom at night. A double bed with a white duvet against the back wall, a round grey dog bed on the floor at the foot of the bed, horizontal window blinds on the right wall letting in thin stripes of cool blue moonlight across the floor and dog bed, a small bedside lamp switched off. Dim, quiet, low-light phone exposure with gentle noise, deep but not crushed shadows.
```
+ REALISM SUFFIX

### REF-CAT — Cat identity
```
A 4-year-old grey British Shorthair cat with dense plush blue-grey coat, round copper-orange eyes, round face and full cheeks, lying relaxed on a grey linen sofa in soft window daylight, looking toward camera-left. Camera at the cat's eye level, 80 cm away.
```
+ REALISM SUFFIX

### REF-ATOKONG — Product
**Do not generate.** Use the client's real packshots (front, 45°, back) on a plain background. Upload as `@ATOKONG`. See PRODUCTION_PACKAGE §4 rule 7.

---

## §B — Keyframes (first frame of each video generation)

### KF-G01 — HOOK / DAY 1 MASTER FRAME ⭐ (also KF-G15-D1)
**Most important image in the project.** Lock it before anything else.
Refs: REF-WESTIE-1, REF-OWNER
```
Overhead close-up of the left flank of a white West Highland White Terrier lying on his right side on a cream wool rug, just in front of his left hip. A woman's two hands enter from the top of frame: fingertips pressed into the coarse white coat, spreading the fur open in a V to reveal a patch of irritated skin about 6 cm wide in the center of frame. The patch has irregular, asymmetric edges; blotchy uneven pink-to-red inflammation, darker red at the center fading to pink at the margins; several fine linear scratch marks; small dry white flakes and scale clinging to the base of the hair shafts; short broken hairs and thinned fur across the patch; the white fur around the edges has faint rust-brown saliva staining. The skin surface is dry and matte — no blood, no open wound, no shine. The woman wears a thin gold band on her right ring finger and oatmeal knit sleeves. Soft daylight from the left. Phone held 35 cm above the dog.
```
+ REALISM SUFFIX

### KF-G01B — Macro of the patch (optional second angle for S02)
Refs: KF-G01
```
Extreme close-up macro of the same irritated patch from KF-G01: individual white hair shafts with tiny white flakes clinging at their bases, short broken hairs, fine linear scratch marks, blotchy pink-red skin with visible skin texture and pores, rust-brown saliva staining on surrounding white fur, two fingertips holding the fur apart at the top edge of frame. Dry, matte, clinical but not graphic. Soft daylight from the left.
```
+ REALISM SUFFIX

### KF-G02 — Night scratching
Refs: REF-WESTIE-1, REF-BEDROOM-NIGHT
```
Bedroom at night in cool moonlight from window blinds on the right, casting thin stripes across the floor. In the foreground-right, the white West Highland White Terrier sits on his round grey dog bed at the foot of the bed, body facing camera-left, his left hind leg raised mid-scratch against his left flank, head tilted toward the scratch, eyes half closed. In the soft-focus background, a woman lies in the double bed under a white duvet, lifting her head slightly off the pillow toward the dog. Low-light phone exposure, gentle noise, deep blue shadows, faint warm glow from a hallway door on the left edge.
```
+ REALISM SUFFIX

### KF-G03 — Claws macro
Refs: REF-WESTIE-1
```
Extreme close-up at night: the hind paw of a white West Highland White Terrier with dark nails mid-scratch, nails dragged through the coarse white fur of his left flank over a patch of blotchy pink-red irritated skin. Tiny white skin flakes are lifted into the air, lit by a thin sliver of warm lamp light from the right against a dark background. Motion blur on the paw only.
```
+ REALISM SUFFIX

### KF-G04 — Paw licking
Refs: REF-WESTIE-1, REF-LIVINGROOM
```
Daytime, the white West Highland White Terrier lies on a cream wool rug, head lowered, licking between the toes of his right front paw, tongue visible, eyes half closed in concentration. The white fur between his toes and on the top of the paw is stained rust-brown from licking, the skin between the toes is pink and irritated. Camera at rug level 1 meter away, three-quarter front view. Window daylight from the left.
```
+ REALISM SUFFIX

### KF-G05 — Product pickup (REAL shoot recommended; else composite)
Refs: REF-OWNER, @ATOKONG
```
Close-up of a woman's right hand (thin gold band on ring finger, oatmeal knit sleeve) lifting a small 30 ml white round spray bottle (about 10 cm tall) with a white pump nozzle and clear dome cap, orange cartoon-dog label off a sunlit white floating shelf, a small trailing plant at frame left, soft morning sunlight across the shelf. The bottle is a plain blank placeholder to be replaced by the real product in compositing; label area facing camera, flat and evenly lit for tracking.
```
+ REALISM SUFFIX

### KF-G06 — Dog sniffs bottle (composite real bottle)
Refs: REF-WESTIE-2, REF-OWNER, @ATOKONG
```
On a cream wool rug in a bright living room, a woman's right hand (gold band, oatmeal knit sleeve) holds a small 30 ml white round spray bottle (about 10 cm tall) with a white pump nozzle and clear dome cap, orange cartoon-dog label at the dog's nose height, label facing camera. The white West Highland White Terrier sits facing camera-left, leaning forward to sniff the bottle nozzle, ears forward, curious expression. Camera low, three-quarter angle, 70 cm away. Window daylight from the left.
```
+ REALISM SUFFIX · *Replace the bottle with the real packshot in post.*

### KF-G07 — Veterinarian exam
Refs: REF-WESTIE-1
```
Veterinary clinic exam room. A white West Highland White Terrier stands calmly on a stainless steel exam table. A veterinarian, seen only from chest down — navy scrub top, forearms, blue nitrile gloves — uses both hands to part the white fur on the dog's flank and inspect the skin under a round illuminated magnifier lamp on an articulated arm. Clinic background soft: cabinets, a wall-mounted otoscope, clean neutral light. Camera over the vet's shoulder, chest height, 1 meter away.
```
+ REALISM SUFFIX

### KF-G08 — Lab pipette
```
Laboratory bench macro. A gloved hand holds a glass dropper pipette above a small clear glass vial, one drop of pale amber botanical extract hanging from the tip. In the soft background: a rack of small amber and clear glass vials, a laboratory microscope, a notebook. Clean white bench, cool-neutral daylight from a window behind, shallow focus on the drop. Real scientific laboratory, not futuristic, no screens with glowing graphics.
```
+ REALISM SUFFIX (replace "pet owner" with "researcher")

### KF-G09 — Daphne kiusiana botanicals
```
Macro photograph of Daphne kiusiana (Korean white daphne) in bloom: dense rounded clusters of small white four-lobed tubular flowers at the tips of branches, surrounded by glossy dark-green elliptical leaves, tiny morning dew drops on the petals, soft overcast light in an evergreen forest, background a soft wash of green. Natural botanical photography, true colors.
```
**Alt KF-G09B (Daphne genkwa):**
```
Macro photograph of Daphne genkwa (lilac daphne) in early spring: small lilac-purple four-lobed flowers clustered along bare slender brown branches before the leaves appear, soft morning light, background a soft wash of pale green and grey. Natural botanical photography, true colors.
```

### KF-G10 — Mist on palm (REAL shoot recommended)
Refs: REF-OWNER
```
Side-backlit close-up of a woman's open left palm facing up near a bright window; a fine clear mist cloud from a spray bottle just entering frame from the right is catching the window light; tiny droplets beading on the skin of the palm. Background is a soft bright window. No color in the mist, crystal clear.
```
+ REALISM SUFFIX

### KF-G11 — Spray demo (also hook H3)
Refs: KF-G01, REF-OWNER, @ATOKONG
```
Same framing and lighting as KF-G01: overhead close-up of the white Westie's left flank on the cream rug with the irritated Day 1 patch exposed. The woman's left hand spreads the fur open around the patch; her right hand enters from the upper right holding a small 30 ml white round spray bottle (about 10 cm tall) with a white pump nozzle and clear dome cap, orange cartoon-dog label angled down toward the patch from about 12 cm away, nozzle pointing at the skin, index finger on the pump. The bottle label is turned away from camera.
```
+ REALISM SUFFIX

### KF-G12 — Droplets macro
Refs: KF-G01B
```
Extreme macro of the irritated pink skin patch and surrounding white hair shafts, freshly misted: hundreds of tiny clear droplets resting on hair tips and on the skin surface, a few merging and soaking in, soft daylight from the left creating tiny highlights in the droplets. No oily sheen, no residue.
```
+ REALISM SUFFIX

### KF-G13 — Bottle down, dog stands
Refs: REF-WESTIE-1, REF-OWNER, REF-LIVINGROOM
```
Low angle at rug level in the bright living room: a woman's right hand sets a small 30 ml white round spray bottle (about 10 cm tall) with a white pump nozzle and clear dome cap, orange cartoon-dog label down upright on the cream rug in the left foreground (label turned away); the white West Highland White Terrier is standing up in the midground facing camera-left toward the sunlit window, body mid-shake with ears flapping and fur fluffing out. Window light from the left.
```
+ REALISM SUFFIX

### KF-G14 — Relief: lying down ⭐
Refs: REF-WESTIE-2, REF-LIVINGROOM
```
Low static view at rug level: the white West Highland White Terrier lies on the cream wool rug inside a warm rectangle of afternoon sunlight from the window on the left, chest down, front paws stretched forward, chin just about to rest on his paws, eyes half closed, body relaxed and heavy. A woman's right hand (gold band) rests lightly on his back from the top-right of frame. Background softly out of focus: sofa, plant. Calm, quiet mood.
```
+ REALISM SUFFIX

### KF-G16 — Paw split (generate two frames, combine in edit)
Refs: REF-WESTIE-1, REF-OWNER
**D1:**
```
Close-up of a white West Highland White Terrier's right front paw resting in a woman's open right palm (gold band visible), toes slightly spread by her thumb. The white fur between and on top of the toes is stained rust-brown from licking, the skin between the toes is pink and irritated, slightly swollen, with a few broken hairs. Dry, no wound. Soft daylight from the left, cream rug background.
```
**D21:** *edit of D1* — see §C.

### KF-G17 — Garden zoomies
Refs: REF-WESTIE-1
```
Morning back garden, green lawn with dew, soft low sun from behind the dog creating a gentle rim light on the white fur. The white West Highland White Terrier is mid-gallop straight toward camera, front paws off the ground, ears up, mouth open with tongue out, brass collar tag swinging. Clean, full white coat. Camera at grass level 6 meters away, long-lens perspective with the background compressed and soft.
```
+ REALISM SUFFIX

### KF-G18 — Night sleep
Refs: REF-WESTIE-1, REF-BEDROOM-NIGHT, KF-G02
```
Same bedroom and camera position as KF-G02, at night in cool moonlight from the blinds on the right. The white West Highland White Terrier is asleep, curled in a ball on his round grey dog bed at the foot of the bed, chin resting on his tail, eyes closed. In the soft-focus background the woman sleeps peacefully under the white duvet, turned away. Still, quiet, low-light phone exposure with gentle noise.
```
+ REALISM SUFFIX

### KF-G19 — Cat spray
Refs: REF-CAT, REF-OWNER, REF-LIVINGROOM
```
The grey British Shorthair cat sits on the grey linen sofa facing camera-left, eyes half closed in a slow blink. A woman's left hand gently parts the plush grey fur on the right side of the cat's neck behind the jaw; her right hand holds a small 30 ml white round spray bottle (about 10 cm tall) with a white pump nozzle and clear dome cap, orange cartoon-dog label 15 cm away aimed at the parted fur, pointed away from the cat's face, a fine mist just released. Window daylight from the left. Camera at the cat's eye level, 70 cm away.
```
+ REALISM SUFFIX

### KF-G20 — End hero (composite real bottle)
Refs: REF-WESTIE-2, REF-CAT, REF-BEDROOM-NIGHT (daytime version), @ATOKONG
```
Morning in the same bedroom, now bright with soft daylight through open blinds on the right. The healthy white West Highland White Terrier with a full clean white coat sits upright on the white duvet in the center of the bed, looking toward camera, mouth slightly open, relaxed and bright-eyed. The grey British Shorthair cat lounges on the duvet behind him, slightly out of focus. In the lower-right foreground on the bedside table edge, a small 30 ml white round spray bottle (about 10 cm tall) with a white pump nozzle and clear dome cap, orange cartoon-dog label stands upright, label facing camera (placeholder for the real product). Leave clean space in the upper third for the end card.
```
+ REALISM SUFFIX · *Replace the bottle with the real packshot in post.*

### KF-H2 — 2 A.M. owner (hook H2)
Refs: REF-BEDROOM-NIGHT
```
Almost dark bedroom at night. A woman in her early 30s lifts her head off a white pillow, face lit only from below by the cold glow of a phone screen in her hand, squinting, tired, hair messy, looking toward the foot of the bed (camera-right). The rest of the room falls into deep blue darkness, faint stripes of moonlight from the blinds. Very low-light phone image, visible noise.
```
+ REALISM SUFFIX

### KF-H4 — K-beauty shelf (REAL shoot recommended)
Refs: REF-OWNER, @ATOKONG
```
Close-up of a clean white bathroom shelf with an arrangement of minimalist unbranded skincare: glass dropper serum bottles, a frosted toner bottle, a cushion compact, small jars — no readable text or brands. A woman's right hand (gold band) reaches in from the right toward a small 30 ml white round spray bottle (about 10 cm tall) with a white pump nozzle and clear dome cap, orange cartoon-dog label at the end of the row. Soft morning daylight, calm spa-like mood.
```
+ REALISM SUFFIX

---

## §C — Transformation states (EDITS of the master frame)

Use an **image-edit model** (e.g. Nano Banana / Seedream edit) with **KF-G01 as the input image**. Run each edit from KF-G01 itself, not from the previous day's image, so error doesn't accumulate. Then check that framing, hands, ring, lighting, rug and fur direction are identical.

### KF-G15-D1
= **KF-G01** unchanged.

### KF-G15-D5 (edit of KF-G01)
```
Edit this image. Keep everything identical — camera position, framing, the woman's hands and finger positions, the gold ring, knit sleeves, rug, lighting, fur direction and the dog. Change ONLY the exposed skin patch: the inflammation is now noticeably calmer — soft even pink instead of red, the darker red center is gone, the scratch marks are faint and almost healed, only a few small white flakes remain, the rust-brown staining on the surrounding fur is lighter. The fur over the patch is still thin and short. Dry, matte skin.
```

### KF-G15-D12 (edit of KF-G01)
```
Edit this image. Keep everything identical — camera position, framing, the woman's hands and finger positions, the gold ring, knit sleeves, rug, lighting, fur direction and the dog. Change ONLY the exposed skin patch: the skin is now a calm pale pink close to normal skin tone, no redness, no scratch marks, no flakes. A layer of new short white fuzz about 2–3 mm long is emerging evenly across the patch. The surrounding fur is clean white with no staining.
```

### KF-G15-D21 (edit of KF-G01)
```
Edit this image. Keep everything identical — camera position, framing, the woman's hands and finger positions, the gold ring, knit sleeves, rug, lighting and the dog. Change ONLY the patch area: it is now covered by healthy white fur that is slightly shorter and softer than the surrounding coat, so a subtle difference in fur length is still visible. Where the fingers part the coat, the visible skin underneath is calm, pale and healthy. Clean white fur, no staining, no flakes.
```
*Keep the slight fur-length difference. A perfect match reads as fake.*

### KF-G16-D21 (edit of KF-G16-D1)
```
Edit this image. Keep everything identical — the paw position, the woman's hand and thumb position, the gold ring, rug and lighting. Change ONLY the paw: the fur between and on top of the toes is now clean white with no rust-brown staining, the skin between the toes is calm, pale pink and not swollen, hair is full and healthy.
```

**QA for §C.** Lay the four frames over each other in your editor at 50% opacity. Nothing should move except the patch. If the hands or framing shifted, re-run the edit; don't fix it in the video step.
