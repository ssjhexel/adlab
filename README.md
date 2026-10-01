# adlab — ATOKONG™ Meta video ad development

Competitive intelligence and production packages for ATOKONG™ Pet Skin Mist (Korean pet dermatology) video ads on Meta.

## Start here
| What | Where |
|---|---|
| Product facts, claims and open questions | `product/ATOKONG_PRODUCT_BRIEF.md` |
| Competitor teardown (12 ads, observations vs. hypotheses) | `research/COMPETITOR_ANALYSIS.md` |
| **Concept 01 "Part the Fur"**: strategy, script, shot list, hooks, test plan | `creative/concept-01-part-the-fur/PRODUCTION_PACKAGE.md` |
| Still-image prompts (references, keyframes, transformation edits) | `creative/concept-01-part-the-fur/IMAGE_PROMPTS.md` |
| Image-to-video prompts (Seedance 2.0 / Higgsfield) | `creative/concept-01-part-the-fur/VIDEO_PROMPTS.md` |
| Video prompt-writing system (CINEDANCE V4) | `reference/CINEDANCE_HIGGSFIELD_SKILL.md` |

## Folder map
```
competitor_ads/            source competitor videos (Meta Ad Library downloads, 360×360)
research/
  COMPETITOR_ANALYSIS.md
  transcripts/C01–C12.md   timestamped VO transcripts + detected cut points
  contact_sheets/          per-ad frame grids: full ad @1fps, first 3s @3fps
  tools/                   scripts that regenerate transcripts and contact sheets
product/                   product brief (source of truth for claims)
reference/                 prompt-writing skill used for video prompts
creative/concept-XX-*/     one folder per ad concept
```
Competitor IDs (C01–C12) follow the sorted filename order in `competitor_ads/`. Each transcript file records its source filename.

## Deliverable spec
9:16 · 1080×1920 · hyper-real, phone-footage look (not an "AI look") · labelled as AI-generated in Meta.

## Before the final edit
See `product/ATOKONG_PRODUCT_BRIEF.md` §3. Still needed from the client: the offer, sign-off on the transformation timeline and coat-regrowth claim, and the launch market. (Packshot received; lick-safe confirmed.)
