# Concept 01 "PART THE FUR" — Video Generation Prompts (Seedance 2.0 / Higgsfield)

Written to the **CINEDANCE V4** spec (`reference/CINEDANCE_HIGGSFIELD_SKILL.md`). Each code block is a **final, paste-ready prompt**. Production notes sit outside the code blocks and never go into the model.

## Setup (UI settings, not in the prompts)
- **Mode:** image-to-video. **First frame = the listed keyframe** from `IMAGE_PROMPTS.md`. Where your Seedance UI supports multi-reference, also upload the listed reference images and name them with the exact @tags below.
- **Aspect ratio 9:16 · 1080p.** Generate 5s unless stated. Plan to use only the most stable 1.2–3.6s of each clip (see PRODUCTION_PACKAGE §6).
- **Takes:** 3–4 per Gen ID. Keep the take with the most physically believable fur, hands and dog motion.
- **Audio:** each prompt asks for natural foley only (no music, no voice). VO and music are added in the edit. If your generator's audio is weak, mute it and use library SFX.

| @tag | Upload | Notes |
|---|---|---|
| `@WESTIE` | REF-WESTIE-1 (+ REF-WESTIE-2) | Hero dog, all dog shots |
| `@OWNER` | REF-OWNER | Hands/forearms only |
| `@CAT` | REF-CAT | S23, S24 only |
| `@ATOKONG` | Client's real packshot | Only where the bottle is visible; label turned away in AI shots |

The location plates (REF-LIVINGROOM, REF-BEDROOM-NIGHT) are already baked into the keyframes, so they are **not** used as @tags. This avoids the location overriding framing.

---

### G01 — Hook: part the fur (S01–S02, hooks H1/H8)
First frame: **KF-G01** · Refs: @WESTIE, @OWNER · 5s
🎙 **VO (0.0–3.2s):** "If your dog keeps scratching the same spot… part the fur." · H8 alt: "Looking for a non-steroidal way to care for your dog's itchy skin?"  
*VO is recorded separately and laid in during the edit. The prompt keeps "No voice" so Seedance doesn't speak over it. Time the clip's action to the length of this line.*
```
SCENE CONTEXT
A woman parts the white coat on her dog's left flank and reveals a patch of irritated, flaky skin he has been scratching.

ACTIVE REFERENCES
@WESTIE: 5-year-old male West Highland White Terrier, compact 8 kg body, coarse white coat with creamy tips, lying still on his right side with the left flank facing up, irritated patch on the left flank just forward of the left hip. 100% matches the reference.
@OWNER: early-30s woman seen only as two hands and forearms, short unpolished nails, thin gold band on the right ring finger, oatmeal knit sleeves. 100% matches the reference.

LOCATION MAP
Living-room floor. Camera directly above the dog's left flank, looking straight down. Cream wool rug visible at the frame edges. Window daylight enters from screen-left.

FIRST FRAME AND SPATIAL BLOCKING
The first visible frame matches the start image: both hands already in the coat at the top of frame, fingertips spreading the white fur open in a V, the irritated patch at frame center. No empty frame, no delayed reveal.
The dog's body runs diagonally from lower-left (hip) to upper-right (shoulder). The hands stay in the top third of frame. The patch stays at frame center for the whole take.

FORMAT MODE
Single continuous take.

OPTICS
29° diagonal field of view, close detail framing, phone held 35 cm above the coat. Patch and fingertips razor-sharp, rug at the frame edges soft, natural phone depth of field. No wide-angle distortion.

CAMERA
Handheld smartphone held by a second person: operator breath, micro-settling, organic small corrections. Slow push-in from the patch filling 30 percent of frame to 55 percent by the end. No rotation, no tilt.

ACTION TIMING
0:00 to 0:01 Fingertips press gently into the coat and begin to spread.
0:01 to 0:03 The fingers slide about 2 cm further apart; the fur opens wider and stray hairs at the edges bend and spring back. Small white flakes at the hair roots become clearly visible. The skin of the flank twitches once under the fingers in a small ripple.
0:03 to 0:05 Hands hold still. The camera keeps its slow push-in toward the center of the patch. The flank rises and falls with one slow breath.

PHYSICS
Coarse terrier fur bends with stiffness and springs back; hairs part along their natural growth direction. Skin moves slightly with finger pressure like real soft tissue. Breathing motion is slow and even. Flakes stay attached to the hair roots.

LIGHTING
Soft daylight from screen-left; fingers cast a soft shadow onto the coat at screen-right. Natural exposure for white fur with detail kept in the highlights. No glow on the patch, no flat front light.

AUDIO
Quiet room tone, soft fur rustle under the fingers, the dog's slow nasal breathing, one faint collar-tag jingle at 0:02. No music. No voice.

POSITIVE CONSTRAINTS
The patch keeps the same size, shape and color in every frame: it does not heal, spread or glow. Exactly two hands with five fingers each. The dog stays in place. Skin stays dry and matte, no blood. Real smartphone footage texture, no CG gloss.
```

---

### G02 — Night scratching (S03, H2 second half)
First frame: **KF-G02** · Refs: @WESTIE · 5s
🎙 **VO (3.2–5.0s):** "This kept him up all night."  
*VO is recorded separately and laid in during the edit. The prompt keeps "No voice" so Seedance doesn't speak over it. Time the clip's action to the length of this line.*
```
SCENE CONTEXT
At night in a dark bedroom, a small white terrier scratches his left flank hard with his hind leg on his dog bed while his owner lifts her head in bed behind him.

ACTIVE REFERENCES
@WESTIE: 5-year-old male West Highland White Terrier, compact 8 kg body, coarse white coat, brown leather collar with a small round brass tag, sitting on a round grey dog bed, scratching his left flank with his left hind leg. 100% matches the reference.

LOCATION MAP
Bedroom at night. Camera at floor level on the left side of the room, facing the foot of the bed. Foreground-right: round grey dog bed with @WESTIE. Background: double bed with white duvet, a woman lying in it. Window blinds on the right wall throw thin stripes of blue moonlight across the floor and the dog bed.

FIRST FRAME AND SPATIAL BLOCKING
The first visible frame matches the start image: @WESTIE already sitting on the dog bed in the right half of frame, body facing screen-left, left hind leg raised against his left flank. The woman is a soft shape in the background bed at the upper left. No empty frame.

FORMAT MODE
Single continuous take.

OPTICS
47° diagonal field of view, standard normal lens character, camera 1.5 meters from the dog. Natural human-eye perspective, no distortion. Dog in focus, background bed softly out of focus.

CAMERA
Camera resting on a low surface with tiny handheld micro-movements, as if the owner is filming from the floor. Fixed framing, no pan.

ACTION TIMING
0:00 to 0:03 @WESTIE scratches his left flank rapidly with his left hind leg in a steady rhythm, about four strokes per second; his head tilts toward the scratch, eyes half closed; the collar tag bounces with each stroke.
0:03 to 0:04 He pauses, lowers the leg briefly, then starts scratching again.
0:02 to 0:05 In the background the woman slowly lifts her head off the pillow and looks toward the dog.

PHYSICS
The hind leg has weight and real joint motion; the body rocks slightly with each stroke; fur on the flank flicks with each pass of the claws. The dog bed cushion compresses under his weight.

LIGHTING
Cool blue moonlight in stripes from the blinds at screen-right, falling across the dog. A faint warm spill from a hallway at the far left edge. Low-light phone exposure with visible noise, deep shadows that keep some detail. No bright fill, no studio light.

AUDIO
Rhythmic metallic collar-tag jingle synced to each scratch, soft thumping of the leg on the cushion, quiet room tone. No music. No voice.

POSITIVE CONSTRAINTS
One dog, one person. The dog stays on the dog bed. Scratching motion is fast, repetitive and physically real. Low-light smartphone realism.
```

---

### G03 — Claws macro, slow motion (S04)
First frame: **KF-G03** · Refs: @WESTIE · 5s
🎙 **VO (5.0–6.6s):** "Every scratch made the itch worse…"  
*VO is recorded separately and laid in during the edit. The prompt keeps "No voice" so Seedance doesn't speak over it. Time the clip's action to the length of this line.*
```
SCENE CONTEXT
In slow motion, a white terrier's hind claws rake through the fur over an irritated patch on his flank, lifting tiny skin flakes into a sliver of lamp light.

ACTIVE REFERENCES
@WESTIE: 5-year-old male West Highland White Terrier, coarse white coat, dark nails, irritated pink-red patch on the left flank. 100% matches the reference.

FIRST FRAME AND SPATIAL BLOCKING
The first visible frame matches the start image: the hind paw already in contact with the fur of the flank, claws pointing down-right, the irritated patch below the claws at frame center. Dark background.

FORMAT MODE
Single continuous take. Slow motion, about one quarter real speed.

OPTICS
18° diagonal field of view, classic telephoto detail character, camera 1 meter away. Razor focus on the claws and patch; background dissolves into dark bokeh.

CAMERA
Locked off. No movement.

ACTION TIMING
0:00 to 0:02 The claws drag slowly downward through the fur and across the patch, hairs bending and separating.
0:02 to 0:04 The paw lifts away; a small cloud of fine white flakes rises and drifts through the beam of warm light.
0:04 to 0:05 The paw comes back for a second slow stroke.

PHYSICS
Each hair bends and springs back individually. Flakes are tiny, light and irregular, drifting slowly and settling with gravity, never glowing. Claws press into the coat with visible weight.

LIGHTING
A thin sliver of warm lamp light from screen-right cuts across the patch; everything else falls into deep shadow. Flakes are lit only where they cross the beam.

AUDIO
Slowed, dry scratching sound, low and textured. No music. No voice.

POSITIVE CONSTRAINTS
Photographic macro realism. No sparkles, no particles beyond real skin flakes, no blood.
```

---

### G04 — Paw licking (S05, hook H6)
First frame: **KF-G04** · Refs: @WESTIE · 5s
🎙 **VO (6.6–8.4s):** "…and round it went." · H6 alt: "Constant paw licking isn't always just a habit."  
*VO is recorded separately and laid in during the edit. The prompt keeps "No voice" so Seedance doesn't speak over it. Time the clip's action to the length of this line.*
```
SCENE CONTEXT
On a living-room rug in daylight, a white terrier obsessively licks between the toes of his right front paw.

ACTIVE REFERENCES
@WESTIE: 5-year-old male West Highland White Terrier, coarse white coat, rust-brown saliva staining on the fur of his right front paw, lying on the rug with his head lowered to the paw. 100% matches the reference.

LOCATION MAP
Bright living room. Camera at rug level, 1 meter in front of the dog at a three-quarter angle. Window light from screen-left. Background: sofa and plant, softly out of focus.

FIRST FRAME AND SPATIAL BLOCKING
The first visible frame matches the start image: @WESTIE already lying on the cream rug, head lowered, tongue at the right front paw, which is positioned at frame center-bottom. No empty frame.

FORMAT MODE
Single continuous take.

OPTICS
47° diagonal field of view, standard normal lens character, camera 1 meter away at rug height. Natural perspective, dog and paw sharp, background soft but readable.

CAMERA
Handheld at floor level: operator breath, micro-settling, very slight push-in.

ACTION TIMING
0:00 to 0:02 @WESTIE licks between the toes with short repetitive tongue strokes, eyes half closed.
0:02 to 0:03 He nibbles at the base of the toes with his front teeth, pulling the paw slightly.
0:03 to 0:05 He returns to licking, a little faster.

PHYSICS
The tongue is wet and flexible, and leaves the toe fur damp and clumped. The paw shifts with each pull. The head moves with real weight.

LIGHTING
Soft window daylight from screen-left, gentle shadow on the right side of the face. Natural exposure, white fur detail held.

AUDIO
Wet licking and soft nibbling sounds, quiet room tone. No music. No voice.

POSITIVE CONSTRAINTS
One dog, four legs, natural anatomy. The paw has four visible toes and a dewclaw. Real smartphone footage feel.
```

---

### G05 — Product pickup (S06) · REAL SHOOT PREFERRED
First frame: **KF-G05** · Refs: @OWNER, @ATOKONG · 4s · *AI fallback only. Composite the real label in post.*
🎙 **VO (8.4–10.2s):** "So I stopped guessing…"  
*VO is recorded separately and laid in during the edit. The prompt keeps "No voice" so Seedance doesn't speak over it. Time the clip's action to the length of this line.*
```
SCENE CONTEXT
A woman's hand lifts a small 30 ml white round spray bottle (about 10 cm tall) with a white pump nozzle and clear dome cap, orange cartoon-dog label, off a sunlit shelf.

ACTIVE REFERENCES
@OWNER: early-30s woman, right hand and forearm only, thin gold band on the ring finger, oatmeal knit sleeve. 100% matches the reference.
@ATOKONG: small 30 ml white round spray bottle (about 10 cm tall) with a white pump nozzle and clear dome cap, orange cartoon-dog label, shape and proportions 100% match the reference.

FIRST FRAME AND SPATIAL BLOCKING
The first visible frame matches the start image: the bottle stands upright on the white shelf at frame center; the hand is entering from screen-right, fingers about to close around it.

FORMAT MODE
Single continuous take.

OPTICS
29° diagonal field of view, close detail framing, camera 60 cm from the shelf at chest height. Bottle sharp, background softly blurred.

CAMERA
Handheld smartphone, operator breath, small tilt-up following the bottle as it lifts.

ACTION TIMING
0:00 to 0:01 The fingers wrap around the bottle.
0:01 to 0:03 The hand lifts the bottle 15 cm and turns it slightly toward camera.
0:03 to 0:04 The hand holds the bottle steady in the upper third of frame.

PHYSICS
The bottle has real weight: a slight wrist flex on lift-off, and the liquid inside shifts.

LIGHTING
Morning sun from screen-left across the shelf, soft shadow of the plant leaves on the wall.

AUDIO
Soft clink of the bottle leaving the shelf, room tone. No music. No voice.

POSITIVE CONSTRAINTS
Bottle shape stays constant. The label area stays flat and evenly lit for compositing. Five fingers.
```

---

### G06 — Dog sniffs the bottle (S07)
First frame: **KF-G06** · Refs: @WESTIE, @OWNER, @ATOKONG · 4s · *Composite the real bottle in post.*
🎙 **VO (10.2–12.0s):** "…and tried Korean pet dermatology."  
*VO is recorded separately and laid in during the edit. The prompt keeps "No voice" so Seedance doesn't speak over it. Time the clip's action to the length of this line.*
```
SCENE CONTEXT
A woman holds a small 30 ml white round spray bottle (about 10 cm tall) with a white pump nozzle and clear dome cap, orange cartoon-dog label, near her dog's nose and he leans in to sniff it.

ACTIVE REFERENCES
@WESTIE: 5-year-old male West Highland White Terrier, coarse white coat, brown collar with brass tag, sitting on the rug facing screen-left. 100% matches the reference.
@OWNER: right hand and forearm only, thin gold band, oatmeal knit sleeve. 100% matches the reference.
@ATOKONG: small 30 ml white round spray bottle (about 10 cm tall) with a white pump nozzle and clear dome cap, orange cartoon-dog label, shape 100% matches the reference.

LOCATION MAP
Bright living room, cream rug. Camera low at a three-quarter angle, 70 cm from the dog. Window light from screen-left.

FIRST FRAME AND SPATIAL BLOCKING
The first visible frame matches the start image: @WESTIE sits at screen-right facing screen-left; the hand holds the bottle at screen-left at the dog's nose height, 15 cm from his nose. No empty frame.

FORMAT MODE
Single continuous take.

OPTICS
47° diagonal field of view, standard normal lens character, camera 70 cm away. Natural proportions, dog and bottle both sharp.

CAMERA
Handheld, operator breath, fixed framing.

ACTION TIMING
0:00 to 0:02 @WESTIE stretches his neck forward and sniffs the nozzle, nostrils flaring, ears forward.
0:02 to 0:04 He pulls back slightly, licks his nose once, and looks up toward the woman, off-screen to the left.

PHYSICS
The neck stretches with real weight transfer to the front legs. Nostrils move with each sniff.

LIGHTING
Window daylight from screen-left, soft natural shadows, white fur detail held.

AUDIO
Quick sniffing sounds, a faint tag jingle, room tone. No music. No voice.

POSITIVE CONSTRAINTS
One dog, one hand. The dog does not bite or lick the bottle. The bottle stays in the hand.
```

---

### G07 — Veterinarian exam (S08, hook H7)
First frame: **KF-G07** · Refs: @WESTIE · 5s
🎙 **VO (12.0–14.0s):** "Created in Korea by a vet with twenty-plus years in clinic…" · H7 alt: "A vet and an immune-cell researcher made one spray… for itchy skin."  
*VO is recorded separately and laid in during the edit. The prompt keeps "No voice" so Seedance doesn't speak over it. Time the clip's action to the length of this line.*
```
SCENE CONTEXT
In a veterinary clinic, a vet's gloved hands part a white terrier's fur under a magnifier lamp to examine his skin.

ACTIVE REFERENCES
@WESTIE: 5-year-old male West Highland White Terrier, coarse white coat, standing calmly on a stainless steel exam table. 100% matches the reference.

LOCATION MAP
Clinic exam room. Stainless steel exam table at frame center. Round illuminated magnifier lamp on an articulated arm entering from upper-right. The veterinarian stands behind the table at screen-left, visible only from chest down: navy scrub top, forearms, blue nitrile gloves. Camera over the vet's right shoulder at chest height, 1 meter away.

FIRST FRAME AND SPATIAL BLOCKING
The first visible frame matches the start image: @WESTIE standing on the table, body facing screen-right; the gloved hands already resting on his flank; the magnifier lamp positioned 25 cm above the flank. No face of the vet in frame at any time.

FORMAT MODE
Single continuous take.

OPTICS
47° diagonal field of view, standard normal lens character, camera 1 meter away. Natural perspective, hands and flank sharp, clinic background softly out of focus.

CAMERA
Handheld, steady, slight drift toward the hands.

ACTION TIMING
0:00 to 0:02 The gloved hands part the fur on the flank with practiced, gentle movements.
0:02 to 0:04 The vet tilts the magnifier lamp a few degrees lower with the left hand while the right hand keeps the fur open.
0:04 to 0:05 @WESTIE stands still, blinks, ears relaxed.

PHYSICS
Gloves crease at the knuckles. The lamp arm moves with mechanical resistance. Fur parts along the growth direction.

LIGHTING
Clean neutral clinic light from overhead, plus the cool white ring of the magnifier lamp lighting the patch of fur from above. No dramatic shadows, no colored light.

AUDIO
Quiet clinic room tone, a soft creak of the lamp arm, glove rustle. No music. No voice.

POSITIVE CONSTRAINTS
The vet's face never appears. Exactly two gloved hands. Realistic working veterinary clinic, not futuristic.
```

---

### G07B — Korean vet-researcher b-roll ⭐ (S08b, hook H7)
First frame: **KF-G07B** · No @tags · 5s
🎙 **VO (14.0–16.0s):** "…and a thirty-year immune-cell researcher."  
*VO is recorded separately and laid in during the edit. The prompt keeps "No voice" so Seedance doesn't speak over it. Time the clip's action to the length of this line.*
```
SCENE CONTEXT
In a bright Seoul research lab, a Korean veterinary researcher looks up from her microscope and lifts a small glass vial of pale amber formula to the window light to examine it.

FIRST FRAME AND SPATIAL BLOCKING
The first visible frame matches the start image: the researcher seated at a white bench in the center-right of frame at a three-quarter angle facing screen-left, eyes just lifting from the microscope eyepieces; a rack of glass vials on the bench at screen-left; a window at screen-left. One colleague softly out of focus in the background. No empty frame.

FORMAT MODE
Single continuous take.

OPTICS
29° diagonal field of view, short telephoto portrait character, camera 2 meters away at seated eye level. Her face and hands razor-sharp, the lab background compressed into soft bokeh, natural flattering face proportions.

CAMERA
Handheld documentary style: operator breath, micro-settling, a very slow drift toward her.

ACTION TIMING
0:00 to 0:02 She sits back from the microscope, adjusts her reading glasses with her left hand, focused expression.
0:02 to 0:04 She picks a small clear vial of pale amber liquid from the rack with her right hand and raises it to eye level toward the window light.
0:04 to 0:05 She tilts the vial slightly and studies it; the liquid moves inside. Her eyes stay on the vial.

PHYSICS
Real hand and arm weight, the lab coat folds and creases with her movement, the liquid in the vial shifts with the tilt and settles.

LIGHTING
Soft daylight from the window at screen-left as the key, gentle shadow on the screen-right side of her face, the amber vial lit through by the window. Clean neutral lab light in the background. No beauty fill.

AUDIO
Quiet lab ambience, a soft clink of glass. No music. No voice.

POSITIVE CONSTRAINTS
One person in focus, natural unretouched skin texture, real documentary feel. She does not look at the camera. No text, no screens with graphics.
```

---

### G08 — Lab pipette (S09, hook H7)
First frame: **KF-G08** · No @tags · 5s
🎙 **VO (16.0–17.8s):** (tail of the researcher line) · Super: REGISTERED VETERINARY QUASI-DRUG · KOREA  
*VO is recorded separately and laid in during the edit. The prompt keeps "No voice" so Seedance doesn't speak over it. Time the clip's action to the length of this line.*
```
SCENE CONTEXT
In a laboratory, a gloved hand releases a single drop of pale amber botanical extract from a glass pipette into a small vial.

FIRST FRAME AND SPATIAL BLOCKING
The first visible frame matches the start image: the glass dropper pipette held vertically at frame center, a drop of pale amber liquid hanging from its tip 2 cm above the open mouth of a small clear glass vial. Background: a rack of vials and a microscope, softly out of focus.

FORMAT MODE
Single continuous take. Slight slow motion, about half real speed.

OPTICS
18° diagonal field of view, classic telephoto detail character, camera 50 cm away. Razor focus on the drop and the vial mouth; background melts into soft bokeh.

CAMERA
Locked off.

ACTION TIMING
0:00 to 0:02 The drop swells slightly at the pipette tip.
0:02 to 0:03 The drop releases and falls straight into the vial.
0:03 to 0:05 Small ripples spread across the liquid surface inside the vial and settle.

PHYSICS
The liquid has real viscosity and surface tension: the drop stretches before release, falls with gravity, and makes a small realistic ripple.

LIGHTING
Cool neutral daylight from a window behind the bench, with a soft rim highlight on the glass edges and the amber drop. Clean white bench.

AUDIO
Faint lab ventilation hum, a tiny drip sound. No music. No voice.

POSITIVE CONSTRAINTS
Real laboratory glassware, no glowing liquid, no holograms, no screens with graphics.
```

---

### G09 — Daphne kiusiana botanicals (S10)
First frame: **KF-G09** (or KF-G09B) · No @tags · 5s
🎙 **VO (17.8–19.2s):** "With Korean medicinal botanicals."  
*VO is recorded separately and laid in during the edit. The prompt keeps "No voice" so Seedance doesn't speak over it. Time the clip's action to the length of this line.*
```
SCENE CONTEXT
Dense clusters of small white Korean daphne flowers sway gently in a misty evergreen forest in the early morning.

FIRST FRAME AND SPATIAL BLOCKING
The first visible frame matches the start image: one rounded cluster of small white four-lobed tubular flowers at frame center, glossy dark-green leaves around it, dew on the petals.

FORMAT MODE
Single continuous take.

OPTICS
18° diagonal field of view, classic telephoto macro character, camera 40 cm from the flowers. Razor focus on the front flower cluster; the forest background dissolves into a soft green wash.

CAMERA
Locked off, with a very slow focus pull from the leaf edge to the front flowers in the first second.

ACTION TIMING
0:00 to 0:01 Focus settles on the flower cluster.
0:01 to 0:05 A light breeze sways the branch a few millimeters back and forth; one dew drop slides down a petal and falls.

PHYSICS
Branch and leaves move with natural springy resistance. The dew drop obeys gravity and surface tension.

LIGHTING
Soft overcast morning light through the canopy, gentle and even. No sun flares.

AUDIO
Soft forest ambience, distant birds, a light breeze. No music. No voice.

POSITIVE CONSTRAINTS
Real botanical photography, true colors, no glow, no particles.
```

---

### G10 — Mist on palm (S11) · REAL SHOOT PREFERRED
First frame: **KF-G10** · Refs: @OWNER · 4s
🎙 **VO (19.2–21.0s):** "No steroids. No fragrance. Lick-safe."  
*VO is recorded separately and laid in during the edit. The prompt keeps "No voice" so Seedance doesn't speak over it. Time the clip's action to the length of this line.*
```
SCENE CONTEXT
A woman sprays a clear mist onto her open palm next to a bright window, and the fine droplets catch the light.

ACTIVE REFERENCES
@OWNER: early-30s woman, left hand open palm-up and right hand holding a small 30 ml white round spray bottle (about 10 cm tall) with a white pump nozzle and clear dome cap, orange cartoon-dog label entering from screen-right, oatmeal knit sleeves. 100% matches the reference.

FIRST FRAME AND SPATIAL BLOCKING
The first visible frame matches the start image: the open left palm at frame center, the bright window behind it; the nozzle of the spray bottle at the right edge of frame, 15 cm from the palm.

FORMAT MODE
Single continuous take. Slight slow motion, about half real speed.

OPTICS
29° diagonal field of view, close detail framing, camera 50 cm away. Palm and mist sharp, window background a soft bright wash.

CAMERA
Handheld, operator breath, fixed framing.

ACTION TIMING
0:00 to 0:01 One pump: a fine clear mist cloud bursts from the nozzle toward the palm.
0:01 to 0:03 The cloud drifts and settles; tiny droplets land and bead on the skin of the palm.
0:03 to 0:04 The palm stays still; the droplets glisten and begin to absorb.

PHYSICS
The mist is made of real fine droplets that spread in a cone, slow with air resistance and fall with gravity. The droplets bead on the skin without sliding.

LIGHTING
Strong side-backlight from the window behind and screen-left. The mist glows only from backlight scatter. The palm keeps natural exposure.

AUDIO
One soft pump-mist "tss" sound, room tone. No music. No voice.

POSITIVE CONSTRAINTS
The mist is completely colorless. Exactly two hands. No sparkle effects.
```

---

### G11 — Spray demo (S12, hook H3)
First frame: **KF-G11** · Refs: @WESTIE, @OWNER, @ATOKONG · 5s
🎙 **VO (21.0–23.6s):** "Three to five sprays on dry skin." · H3 alt: "This is Korean skincare… for itchy dogs."  
*VO is recorded separately and laid in during the edit. The prompt keeps "No voice" so Seedance doesn't speak over it. Time the clip's action to the length of this line.*
```
SCENE CONTEXT
The woman holds her dog's fur open over the irritated patch on his flank and sprays it three times with a fine mist.

ACTIVE REFERENCES
@WESTIE: 5-year-old male West Highland White Terrier, coarse white coat, lying on his right side with the irritated patch on the left flank facing up. 100% matches the reference.
@OWNER: left hand spreading the fur around the patch, right hand holding the spray bottle, thin gold band on the right ring finger, oatmeal knit sleeves. 100% matches the reference.
@ATOKONG: small 30 ml white round spray bottle (about 10 cm tall) with a white pump nozzle and clear dome cap, orange cartoon-dog label, shape 100% matches the reference, label turned away from camera.

LOCATION MAP
Living-room floor. Camera above and slightly behind the dog's back at a three-quarter overhead angle. Cream rug at the frame edges. Window light from screen-left.

FIRST FRAME AND SPATIAL BLOCKING
The first visible frame matches the start image: the patch at frame center held open by the left hand from the top of frame; the right hand holds the bottle in the upper-right, nozzle aimed down at the patch from 12 cm away. No empty frame.

FORMAT MODE
Single continuous take.

OPTICS
29° diagonal field of view, close detail framing, camera 45 cm away. Patch, fingers and nozzle sharp; rug soft.

CAMERA
Handheld smartphone held by a second person: operator breath, micro-settling, fixed framing.

ACTION TIMING
0:00 to 0:01 First pump: a fine mist cloud leaves the nozzle and spreads over the patch.
0:01 to 0:02 Second pump.
0:02 to 0:03 Third pump.
0:03 to 0:05 The bottle lifts away out of the top-right of frame; the mist settles onto the fur and skin; the left hand keeps the fur open. The dog stays relaxed and still.

PHYSICS
Each pump produces a short cone of fine droplets that drifts down with gravity and settles. The index finger presses the pump with visible travel. Fur tips catch the droplets.

LIGHTING
Soft daylight from screen-left; the mist cloud is softly lit from the side. No glow on the skin.

AUDIO
Three crisp pump-mist sounds, "tss, tss, tss", with one-second spacing, quiet room tone. No music. No voice.

POSITIVE CONSTRAINTS
The spray goes only onto the flank patch, never toward the head. The patch does not change color in this shot. Exactly two hands. The label stays turned away.
```

---

### G12 — Droplets macro (S13)
First frame: **KF-G12** · Refs: @WESTIE · 5s
🎙 **VO (23.6–26.4s):** (first frame for G12-SCI) "Korean botanicals get to work, soothing the skin and supporting its natural barrier."  
*VO is recorded separately and laid in during the edit. The prompt keeps "No voice" so Seedance doesn't speak over it. Time the clip's action to the length of this line.*
```
SCENE CONTEXT
Extreme close-up of fine mist droplets resting on white hair tips and irritated pink skin, slowly settling and soaking in.

ACTIVE REFERENCES
@WESTIE: coarse white coat and pink irritated skin of the left flank. 100% matches the reference.

FIRST FRAME AND SPATIAL BLOCKING
The first visible frame matches the start image: hundreds of tiny clear droplets on the hair tips and skin across the whole frame.

FORMAT MODE
Single continuous take.

OPTICS
18° diagonal field of view, classic telephoto macro character. Razor-thin focus plane on the skin surface at frame center; hair tips in the foreground soft.

CAMERA
Locked off, with a very slow focus pull from the hair tips to the skin surface across the first two seconds.

ACTION TIMING
0:00 to 0:02 Focus moves from the droplets on the hair tips to the skin.
0:02 to 0:05 Several droplets on the skin shrink and disappear as they absorb; two small droplets on a hair merge and slide down the shaft.

PHYSICS
Droplets keep real surface tension and roundness; absorption is gradual; merging droplets run down the hair with gravity.

LIGHTING
Soft daylight from screen-left creating tiny specular points in the droplets. Skin stays matte.

AUDIO
Near silence, very quiet room tone. No music. No voice.

POSITIVE CONSTRAINTS
No oily sheen, no residue, no color change, no glow. Photographic macro realism.
```

---

### G12-SCI — Macro science dive ⭐ (S13, hook H11)
First frame: **KF-G12** (droplets macro) · Last frame: **KF-G12-SCI-END** · Optional middle reference: KF-G12-SCI-MID · Refs: @WESTIE · 5s (use ~2.8s)
🎙 **VO (23.6–26.4s):** "Korean botanicals get to work, soothing the skin and supporting its natural barrier." · H11 alt: "Here's what Korean pet skincare does under the fur."  
*VO is recorded separately and laid in during the edit. The prompt keeps "No voice" so Seedance doesn't speak over it. Time the clip's action to the length of this line.*
*If your Seedance UI has no first+last-frame mode, generate two clips (KF-G12 → push-in, and KF-G12-SCI-MID → END) and join them with a HARD CUT on the push-in.*
```
SCENE CONTEXT
An extreme macro of fine mist droplets on irritated dog skin pushes through the surface into a microscope-style cross-section of the skin, where the clear liquid soaks into the gaps of the irritated surface layer and the tissue visibly calms.

ACTIVE REFERENCES
@WESTIE: coarse white hair shafts and pink irritated skin of the left flank at the start of the shot. 100% matches the reference.

FIRST FRAME AND SPATIAL BLOCKING
The first visible frame matches the start image: tiny clear droplets on white hair tips and pink skin across the frame. The last frame matches the end image: a calm, sealed skin cross-section with a hair shaft rising diagonally at screen-right.

FORMAT MODE
Controlled multi-shot sequence with one MATCH CUT at 1.0 second.
Shot A 0:00 to 0:01: surface macro. Shot B 0:01 to 0:05: microscope cross-section, opening on the same droplet position at frame center.

OPTICS
Shot A: 18° diagonal field of view, classic telephoto macro character, razor-thin focus on the skin surface.
Shot B: scientific microscope view, flat even perspective, soft shallow depth of field, focus on the surface cell layer.

CAMERA
Shot A: a slow, steady push-in toward one droplet resting on the skin at frame center.
Shot B: continues the same slow downward push, settling on the surface layer. No rotation, no shake.

ACTION TIMING
0:00 to 0:01 The camera pushes toward the droplet at frame center as it starts to soak into the skin.
0:01 to 0:02 MATCH CUT into the cross-section: the surface cell layer is uneven and slightly lifted with small gaps, the tissue below is deep red-pink, and clear liquid from the surface flows down into the gaps between the cells.
0:02 to 0:04 The liquid spreads along the gaps; the lifted cells settle flat and close together into a smooth continuous layer; the red-pink tissue below slowly cools to a calm pale pink.
0:04 to 0:05 Hold on the calm, sealed skin layer with a thin film of moisture on top.

PHYSICS
The liquid behaves like real water-based fluid: it beads, wicks along the gaps by capillary action and spreads slowly. Cells move slightly and organically as they settle, like soft living tissue, never snapping or morphing abruptly. Color change is gradual and even.

LIGHTING
Soft, even, cool-neutral light from above like a microscope illuminator. Natural muted tissue colors. No glow, no rim light effects, no colored light.

AUDIO
A soft, low ambient tone and a faint wet seep sound. No music. No voice.

POSITIVE CONSTRAINTS
Photoreal scientific micro-photography in every frame. No neon, no glowing particles, no energy rings, no sparkles, no cartoon or 3D-render cells, no text, no labels, no holograms.
```

---

### G13 — Bottle down, shake-off (S14)
First frame: **KF-G13** · Refs: @WESTIE, @OWNER, @ATOKONG · 5s
🎙 **VO (26.4–27.8s):** "No bath. No rinse. Nothing to rub in."  
*VO is recorded separately and laid in during the edit. The prompt keeps "No voice" so Seedance doesn't speak over it. Time the clip's action to the length of this line.*
```
SCENE CONTEXT
The woman sets the spray bottle down on the rug as her dog stands, shakes out his coat and trots toward the sunny window.

ACTIVE REFERENCES
@WESTIE: 5-year-old male West Highland White Terrier, coarse white coat, brown collar with brass tag. 100% matches the reference.
@OWNER: right hand and forearm only, thin gold band, oatmeal knit sleeve. 100% matches the reference.
@ATOKONG: small 30 ml white round spray bottle (about 10 cm tall) with a white pump nozzle and clear dome cap, orange cartoon-dog label, shape 100% matches the reference, label turned away from camera.

LOCATION MAP
Bright living room. Camera at rug level. Foreground screen-left: the bottle being set down on the cream rug. Midground center: @WESTIE standing. Window at screen-left beyond the frame edge, light coming from screen-left.

FIRST FRAME AND SPATIAL BLOCKING
The first visible frame matches the start image: the hand placing the bottle upright in the left foreground; @WESTIE standing in the midground, body facing screen-left, starting to shake. No empty frame.

FORMAT MODE
Single continuous take.

OPTICS
47° diagonal field of view, standard normal lens character, camera 1.2 meters from the dog at rug level. Natural perspective, no distortion.

CAMERA
Handheld at floor level, operator breath, fixed framing.

ACTION TIMING
0:00 to 0:01 The hand releases the bottle upright on the rug and withdraws out of the top-left of frame.
0:01 to 0:03 @WESTIE does a full-body shake from head to tail: ears flap, coat fluffs out, collar tag swings.
0:03 to 0:05 He trots two steps toward screen-left, toward the window light.

PHYSICS
The shake travels in a wave from head to tail with real fur inertia; loose fur settles after the shake. Paws press into the rug with weight. The bottle stands stable after release.

LIGHTING
Warm afternoon window light from screen-left, rim light on the dog's fur.

AUDIO
Bottle tap on the rug, fur shake flap, collar-tag jingle, soft paw steps. No music. No voice.

POSITIVE CONSTRAINTS
One dog, one hand. The dog keeps the same size and coat. The bottle stays upright.
```

---

### G14 — Relief: he lies down ⭐ (S15)
First frame: **KF-G14** · Refs: @WESTIE, @OWNER · 5s
🎙 **VO (27.8–31.0s):** "From the very first spray… he stopped scratching and just lay down."  
*VO is recorded separately and laid in during the edit. The prompt keeps "No voice" so Seedance doesn't speak over it. Time the clip's action to the length of this line.*
```
SCENE CONTEXT
In a patch of afternoon sun on the rug, the small white terrier lets out a long sigh, rests his chin on his paws and slowly closes his eyes while his owner strokes his back once.

ACTIVE REFERENCES
@WESTIE: 5-year-old male West Highland White Terrier, coarse white coat, brown collar with brass tag, lying chest-down on the rug with front paws forward. 100% matches the reference.
@OWNER: right hand only, thin gold band, oatmeal knit sleeve, resting on the dog's back from the top-right. 100% matches the reference.

LOCATION MAP
Bright living room. Camera at rug level, 1.5 meters in front of the dog. Window at screen-left casts a warm rectangle of sunlight on the rug; the dog lies inside it. Background: sofa and plant, softly out of focus.

FIRST FRAME AND SPATIAL BLOCKING
The first visible frame matches the start image: @WESTIE lying chest-down at frame center inside the sunlight rectangle, head up slightly, chin 3 cm above his paws, eyes half open; the hand resting on his back from the top-right. No empty frame.

FORMAT MODE
Single continuous take.

OPTICS
29° diagonal field of view, short telephoto portrait character, camera 1.5 meters away at rug height. The dog's face razor-sharp, the background compressed into soft warm bokeh, close framing achieved through lens reach.

CAMERA
Static, resting on the floor. No movement.

ACTION TIMING
0:00 to 0:02 @WESTIE takes a slow deep breath: chest expands, then a long exhale through the nose; his flanks sink and his body visibly relaxes.
0:02 to 0:03 He lowers his chin onto his front paws.
0:03 to 0:05 His eyes slowly close. The hand strokes once along his back from shoulders toward hips, then lifts out of frame.

PHYSICS
The breath is visible in the rib cage and nostrils. The body weight settles into the rug. The fur flattens and springs back under the stroke.

LIGHTING
Warm low afternoon sun from screen-left, the dog inside the sunlit rectangle with soft glowing edges on his fur, the room around him slightly darker. Natural exposure for white fur in sunlight.

AUDIO
A long, audible dog sigh through the nose at 0:01, soft room tone, distant birds outside. No music. No voice.

POSITIVE CONSTRAINTS
The dog does not scratch, lick or move away. Calm, slow, real behavior. One dog, one hand.
```

---

### G15 — Transformation series: BEFORE / DAY 1 / 3 / 5 (S16–S19, hook H5)
First frames: **KF-G15-D0, -D1, -D3, -D5** · Refs: @WESTIE, @OWNER · **3s each**
🎙 **VO (31.0–36.2s):** D0 "By day three…" · D1 "…the redness had calmed…" · D3 "…by day five…" · D5 "…his skin looked like his again." · H5 alt: "Same spot. Five days apart."  
*VO is recorded separately and laid in during the edit. The prompt keeps "No voice" so Seedance doesn't speak over it. Time the clip's action to the length of this line.*
Run the same prompt four times, once per start frame, swapping only the bracketed `[SKIN STATE]` line. The motion is deliberately minimal, so the cut between days carries the change.

`[SKIN STATE]` per day:
- **D0 (BEFORE):** the exposed patch is blotchy pink-to-red with fine scratch marks, dry white flakes at the hair roots and thin broken fur.
- **D1:** the exposed patch is a shade calmer: the darkest red center has softened to red-pink, with slightly fewer flakes and faint scratch marks.
- **D3:** the exposed patch is soft even pink with faded scratch marks and almost no flakes; the fur over it is still thin.
- **D5:** the exposed skin is calm pale pink close to normal skin tone with no flakes; the fur over it is short with a faint first layer of fine new fuzz.

```
SCENE CONTEXT
A close-up progress shot: the owner's fingers hold open the white coat on her dog's left flank to show the condition of the skin.

ACTIVE REFERENCES
@WESTIE: 5-year-old male West Highland White Terrier, coarse white coat, lying on his right side with the left flank facing up. 100% matches the reference.
@OWNER: two hands, fingertips holding the fur open, thin gold band on the right ring finger, oatmeal knit sleeves. 100% matches the reference.

FIRST FRAME AND SPATIAL BLOCKING
The first visible frame matches the start image exactly: same camera position, same finger positions, the skin area at frame center. [SKIN STATE]

FORMAT MODE
Single continuous take.

OPTICS
29° diagonal field of view, close detail framing, camera 35 cm above the coat. Skin and fingertips razor-sharp, rug at the edges soft.

CAMERA
Handheld but very steady, like an owner taking progress footage: minimal micro-movement, no push-in, no reframing.

ACTION TIMING
0:00 to 0:02 The fingertips spread the fur 1 cm further apart in one slow, gentle motion.
0:02 to 0:03 Hands hold still; the flank rises gently with one breath.

PHYSICS
Fur parts along its growth direction and springs at the edges. The skin moves slightly with finger pressure. Slow, even breathing.

LIGHTING
Soft daylight from screen-left, identical in every take; fingers cast a soft shadow at screen-right.

AUDIO
Soft fur rustle and quiet room tone. No music. No voice.

POSITIVE CONSTRAINTS
The skin condition stays exactly as described for the whole clip: no change, no morphing, no glow. Same framing as the start image from first to last frame. Exactly two hands.
```

---

### G16 — Paw progress, BEFORE and DAY 5 (S20)
First frames: **KF-G16-D1** and **KF-G16-D5** · Refs: @WESTIE, @OWNER · 3s each · Stack top/bottom in the edit.
🎙 **VO (36.2–37.8s):** "Even his paws."  
*VO is recorded separately and laid in during the edit. The prompt keeps "No voice" so Seedance doesn't speak over it. Time the clip's action to the length of this line.*
```
SCENE CONTEXT
Close-up of a small white terrier's front paw resting in his owner's palm while her thumb gently spreads his toes to show the skin between them.

ACTIVE REFERENCES
@WESTIE: right front paw of a 5-year-old male West Highland White Terrier, coarse white fur, four toes and black pads. 100% matches the reference.
@OWNER: right hand, palm up under the paw, thin gold band on the ring finger. 100% matches the reference.

FIRST FRAME AND SPATIAL BLOCKING
The first visible frame matches the start image exactly: the paw at frame center resting in the palm, the thumb on top of the toes.

FORMAT MODE
Single continuous take.

OPTICS
29° diagonal field of view, close detail framing, camera 30 cm away. Paw and toes razor-sharp, background soft.

CAMERA
Handheld, very steady, no reframing.

ACTION TIMING
0:00 to 0:02 The thumb gently spreads two toes apart, opening the space between them.
0:02 to 0:03 Hold. The paw's toes flex once slightly.

PHYSICS
The pads are firm and leathery; the toes move with real joints; the fur between the toes parts with the thumb.

LIGHTING
Soft daylight from screen-left, natural exposure for white fur.

AUDIO
Quiet room tone. No music. No voice.

POSITIVE CONSTRAINTS
The paw condition stays exactly as in the start image for the whole clip. Four toes, natural anatomy, five fingers.
```

---

### G17 — Garden zoomies (S21)
First frame: **KF-G17** · Refs: @WESTIE · 5s
🎙 **VO (37.8–39.6s):** "Less scratching. Less licking."  
*VO is recorded separately and laid in during the edit. The prompt keeps "No voice" so Seedance doesn't speak over it. Time the clip's action to the length of this line.*
```
SCENE CONTEXT
On a dewy morning lawn, the small white terrier gallops straight toward the camera, full of energy.

ACTIVE REFERENCES
@WESTIE: 5-year-old male West Highland White Terrier, full clean white coat, brown collar with a brass tag, mouth open, tongue out. 100% matches the reference.

LOCATION MAP
Back garden lawn. Camera at grass level, 6 meters in front of the dog at the start. The sun is low behind the dog. Hedges and a fence in the soft background.

FIRST FRAME AND SPATIAL BLOCKING
The first visible frame matches the start image: @WESTIE mid-gallop at frame center, front paws off the ground, heading straight at camera. No empty frame.

FORMAT MODE
Single continuous take. Real-time motion.

OPTICS
18° diagonal field of view, classic telephoto lens character, camera 6 meters from the dog. Background compressed flat behind the dog and completely blurred into a soft green-gold wash; razor focus on the dog's face; the dog pops sharply against the dissolved background; close framing achieved through lens reach, not physical proximity.

CAMERA
Handheld at grass level, operator tracking slightly to keep the dog centered, focus following the dog.

ACTION TIMING
0:00 to 0:03 @WESTIE gallops toward camera in a real bounding gait: front paws reach, back legs push, ears flop up and down, tongue out, collar tag bouncing.
0:03 to 0:05 He slows to a trot as he gets close, filling more of the frame.

PHYSICS
Real ground contact on every stride, grass and dew kicked up by the paws, fur bouncing with delay, body mass rising and falling with each bound. No floaty motion.

LIGHTING
Low morning sun behind the dog creating a bright rim along his white coat and ears; the front of the dog is lit by soft bounce from the lawn.

AUDIO
Rhythmic paw thuds on grass, collar-tag jingle, panting, morning birds. No music. No voice.

POSITIVE CONSTRAINTS
One dog, four legs moving in a correct gallop pattern. No telephoto-to-wide drift: the background stays compressed and blurred in every frame.
```

---

### G18 — Night sleep (S22)
First frame: **KF-G18** · Refs: @WESTIE · 5s
🎙 **VO (39.6–41.4s):** "More sleep — for both of us."  
*VO is recorded separately and laid in during the edit. The prompt keeps "No voice" so Seedance doesn't speak over it. Time the clip's action to the length of this line.*
```
SCENE CONTEXT
At night in the bedroom, the small white terrier sleeps peacefully curled on his dog bed while his owner sleeps in the bed behind him.

ACTIVE REFERENCES
@WESTIE: 5-year-old male West Highland White Terrier, full white coat, curled in a ball on a round grey dog bed, chin on his tail, eyes closed. 100% matches the reference.

LOCATION MAP
Same bedroom and camera position as the night scratching shot: camera at floor level on the left side of the room, facing the foot of the bed. Foreground-right: the dog bed. Background: the double bed with a sleeping woman under a white duvet, turned away. Blinds on the right wall throw stripes of blue moonlight across the floor and dog bed.

FIRST FRAME AND SPATIAL BLOCKING
The first visible frame matches the start image: @WESTIE curled asleep in the right half of frame; the woman a still, soft shape in the background bed. No empty frame.

FORMAT MODE
Single continuous take.

OPTICS
47° diagonal field of view, standard normal lens character, camera 1.5 meters from the dog. Dog in focus, background bed softly out of focus.

CAMERA
Completely still, resting on the floor.

ACTION TIMING
0:00 to 0:05 @WESTIE breathes slowly and deeply, his side rising and falling about every two seconds; at 0:03 one ear twitches once. The woman does not move.

PHYSICS
Slow, natural sleeping breath moving the rib cage and fur. The cushion holds the dog's weight.

LIGHTING
Cool blue moonlight stripes from the blinds at screen-right falling across the dog. Low-light phone exposure with gentle noise, deep calm shadows.

AUDIO
Very quiet slow dog breathing, faint ticking clock, room tone. No music. No voice.

POSITIVE CONSTRAINTS
Completely calm and still. No scratching. One dog, one person.
```

---

### G19 — Cat cameo (S23)
First frame: **KF-G19** · Refs: @CAT, @OWNER, @ATOKONG · 4s
🎙 **VO (41.4–43.0s):** "And it's made for cats, too."  
*VO is recorded separately and laid in during the edit. The prompt keeps "No voice" so Seedance doesn't speak over it. Time the clip's action to the length of this line.*
```
SCENE CONTEXT
On the sofa, the owner parts the fur at the side of her grey cat's neck and gives it one gentle spray; the cat slow-blinks, relaxed.

ACTIVE REFERENCES
@CAT: 4-year-old grey British Shorthair, dense plush blue-grey coat, round copper eyes, sitting on a grey linen sofa facing screen-left. 100% matches the reference.
@OWNER: left hand parting the fur on the right side of the cat's neck behind the jaw, right hand holding the spray bottle, thin gold band on the right ring finger, oatmeal knit sleeves. 100% matches the reference.
@ATOKONG: small 30 ml white round spray bottle (about 10 cm tall) with a white pump nozzle and clear dome cap, orange cartoon-dog label, shape 100% matches the reference, label turned away from camera.

FIRST FRAME AND SPATIAL BLOCKING
The first visible frame matches the start image: @CAT at frame center facing screen-left; the left hand already parting the fur at the side of the neck; the bottle 15 cm from the neck at screen-right, aimed at the parted fur and away from the face. No empty frame.

FORMAT MODE
Single continuous take.

OPTICS
47° diagonal field of view, standard normal lens character, camera 70 cm away at the cat's eye level. Natural proportions.

CAMERA
Handheld, operator breath, fixed framing.

ACTION TIMING
0:00 to 0:01 One pump: a soft mist lands on the parted fur at the side of the neck.
0:01 to 0:03 The bottle withdraws out of frame right; the cat slowly closes and opens its eyes in a long slow blink.
0:03 to 0:04 The left hand smooths the fur back down once.

PHYSICS
The mist cone drifts onto the fur and settles. The plush coat compresses and springs back under the hand.

LIGHTING
Soft window daylight from screen-left, gentle shadow on the right side of the cat's face.

AUDIO
One soft pump-mist "tss", a quiet purr, room tone. No music. No voice.

POSITIVE CONSTRAINTS
The spray never goes toward the cat's eyes, ears or mouth. The cat stays calm and seated. One cat, two hands.
```

---

### G20 — End hero (S24)
First frame: **KF-G20** · Refs: @WESTIE, @CAT, @ATOKONG · 5s · *Composite the real bottle in post. The end card overlays from 43.0s.*
🎙 **VO (43.0–48.2s):** "Scratch less, lick less, live more. Tap below to get Atokong No-Itch Mist on sale today."  
*VO is recorded separately and laid in during the edit. The prompt keeps "No voice" so Seedance doesn't speak over it. Time the clip's action to the length of this line.*
```
SCENE CONTEXT
On a bright morning bed, the healthy white terrier sits happily looking at camera while the grey cat lounges behind him, with a small 30 ml white round spray bottle (about 10 cm tall) with a white pump nozzle and clear dome cap, orange cartoon-dog label on the bedside table in the foreground.

ACTIVE REFERENCES
@WESTIE: 5-year-old male West Highland White Terrier, full clean white coat, brown collar with brass tag, sitting upright on a white duvet, looking at camera, mouth slightly open. 100% matches the reference.
@CAT: 4-year-old grey British Shorthair lying on the duvet behind the dog. 100% matches the reference.
@ATOKONG: small 30 ml white round spray bottle (about 10 cm tall) with a white pump nozzle and clear dome cap, orange cartoon-dog label standing upright on the bedside table edge in the lower-right foreground, label facing camera, shape 100% matches the reference.

LOCATION MAP
Bedroom in morning daylight. Camera at the dog's eye level, 1.8 meters from the bed. Window with open blinds on screen-right. Bed with white duvet fills the middle of frame. The bedside table edge occupies the lower-right foreground.

FIRST FRAME AND SPATIAL BLOCKING
The first visible frame matches the start image: @WESTIE sitting at frame center; @CAT lying behind him slightly to screen-left; the bottle in the lower-right foreground. Upper third of frame is clean wall and soft light. No empty frame.

FORMAT MODE
Single continuous take.

OPTICS
29° diagonal field of view, short telephoto portrait character, camera 1.8 meters away. Dog razor-sharp, cat slightly soft, bottle in the foreground slightly soft, background wall softly compressed.

CAMERA
Static on a tripod. No movement.

ACTION TIMING
0:00 to 0:02 @WESTIE tilts his head slightly to one side, ears forward.
0:02 to 0:04 He pants gently, mouth open, then closes it and looks at camera.
0:01 to 0:05 @CAT slowly stretches one front paw and settles.

PHYSICS
Natural small head and ear movements, real breathing, the duvet compresses under both animals.

LIGHTING
Bright soft morning daylight from screen-right through open blinds, clean and airy, white fur detail held, gentle shadow on the screen-left side of the dog.

AUDIO
Quiet morning room tone, soft panting, distant birds. No music. No voice.

POSITIVE CONSTRAINTS
One dog, one cat, one bottle. The bottle stays still and upright. The animals stay on the bed.
```

---

## Hook-specific generations

### G-H2 — 2 A.M. owner (hook H2, 0–1.2s)
First frame: **KF-H2** · No @tags · 4s
🎙 **VO (hook 0.0–3.2s):** "If you know this sound at 2 a.m.…"  
*VO is recorded separately and laid in during the edit. The prompt keeps "No voice" so Seedance doesn't speak over it. Time the clip's action to the length of this line.*
```
SCENE CONTEXT
In a near-dark bedroom at night, a tired woman lifts her head off the pillow, her face lit only by her phone screen, and looks toward the foot of the bed.

FIRST FRAME AND SPATIAL BLOCKING
The first visible frame matches the start image: the woman's head on a white pillow at frame center, the phone in her hand lighting her face from below. The rest of the room is dark.

FORMAT MODE
Single continuous take.

OPTICS
47° diagonal field of view, standard normal lens character, camera 1 meter away at pillow height. Natural proportions.

CAMERA
Handheld, slight low-light micro-movement, fixed framing.

ACTION TIMING
0:00 to 0:01 She squints at the phone screen.
0:01 to 0:03 She lifts her head off the pillow and turns her eyes toward the foot of the bed at screen-right.
0:03 to 0:04 She exhales, tired, still looking toward screen-right.

PHYSICS
Hair and pillow move naturally with her head; the duvet shifts with her shoulder.

LIGHTING
The only key light is the cold blue-white phone screen below her face. Faint blue moonlight stripes on the wall behind. Very low-light phone exposure with visible noise. No fill light.

AUDIO
Off-screen at screen-right: rhythmic metallic collar-tag jingle and soft thumping, starting at 0:00. Her quiet tired exhale at 0:03. No music. No voice.

POSITIVE CONSTRAINTS
One person. Her face stays mostly in shadow except for the phone glow. Real low-light smartphone texture.
```

### G-H4 — K-beauty shelf (hook H4) · REAL SHOOT PREFERRED
First frame: **KF-H4** · Refs: @OWNER, @ATOKONG · 4s
🎙 **VO (hook 0.0–3.2s):** "I trust Korean skincare with my face… so why not my dog's itchy skin?"  
*VO is recorded separately and laid in during the edit. The prompt keeps "No voice" so Seedance doesn't speak over it. Time the clip's action to the length of this line.*
```
SCENE CONTEXT
A woman's hand passes along a shelf of minimalist skincare bottles and picks up a small 30 ml white round spray bottle (about 10 cm tall) with a white pump nozzle and clear dome cap, orange cartoon-dog label at the end of the row.

ACTIVE REFERENCES
@OWNER: right hand only, thin gold band, oatmeal knit sleeve. 100% matches the reference.
@ATOKONG: small 30 ml white round spray bottle (about 10 cm tall) with a white pump nozzle and clear dome cap, orange cartoon-dog label at the right end of the row, shape 100% matches the reference.

FIRST FRAME AND SPATIAL BLOCKING
The first visible frame matches the start image: a row of unbranded glass skincare bottles and jars on a white shelf filling the frame from left to right; the hand entering from screen-right.

FORMAT MODE
Single continuous take.

OPTICS
29° diagonal field of view, close detail framing, camera 50 cm from the shelf. Bottles sharp, wall soft.

CAMERA
Handheld, operator breath, gentle slide right-to-left following the hand, then settling.

ACTION TIMING
0:00 to 0:02 The fingers glide past the serum bottles without touching them.
0:02 to 0:03 The hand closes around the small 30 ml white round spray bottle (about 10 cm tall) with a white pump nozzle and clear dome cap, orange cartoon-dog label.
0:03 to 0:04 The hand lifts it off the shelf toward camera.

PHYSICS
Bottles stay still; the lifted bottle has real weight.

LIGHTING
Soft morning daylight from screen-left, clean and bright.

AUDIO
Soft glass clinks, room tone. No music. No voice.

POSITIVE CONSTRAINTS
No readable text or brand names on any bottle except the composited product. Five fingers.
```
