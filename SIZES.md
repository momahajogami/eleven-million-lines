# Course Storage Sizes

Updated manually each session. Run `du -sh 0*/` from the project root to refresh.

## Total

**3.6 GB** (as of 2026-08-18) — 4 of 11 units populated

## By Unit

| Unit | Total | Notes |
|------|-------|-------|
| 01 — Early Unix | 262 MB | Plan 9 dominates (254 MB); xv6 is 856 KB, unix-v6 is 7 MB |
| 02 — C Compilers | 1.5 GB | GCC is the weight (1.5 GB full clone); tcc is 14 MB |
| 03 — Stallman / GNU | 485 MB | Emacs 242 MB, GDB 244 MB (both blobless sparse); FSF texts are trivial |
| 04 — Blender | 1.4 GB | Blender repo, full clone |
| 05 — Public Enterprise | 48 KB | Not yet populated |
| 06–11 | ~4 KB each | Empty |

## USB Drive Feasibility

A **64 GB** drive holds the course comfortably at any reasonable final size.
A **32 GB** drive is tight but probably sufficient — see projection below.

### Projection for full 11 units

Rough estimates based on what's known or likely:

| Unit | Likely repos | Est. size |
|------|-------------|-----------|
| 01 | xv6, unix-v6, Plan 9 ✓ | 262 MB |
| 02 | DMR compiler, tcc, GCC ✓ | 1.5 GB |
| 03 | Emacs, GDB ✓ | 485 MB |
| 04 | Blender ✓ | 1.4 GB |
| 05 | LaTeX/TeX, GIMP, Pd, SageMath | ~500 MB est. |
| 06 | TBD | ~500 MB est. |
| 07 | TBD | ~500 MB est. |
| 08 | TBD | ~500 MB est. |
| 09 | TBD | ~500 MB est. |
| 10 | TBD | ~500 MB est. |
| 11 | TBD | ~500 MB est. |
| **Total** | | **~7–9 GB est.** |

The unknown units are estimated conservatively. If any include something as large as GCC or the Linux kernel, that estimate climbs fast.

### On clone strategy

The GCC and Blender clones are conventional (full history). Emacs and GDB used `--filter=blob:none` (blobless) which significantly reduces size. If storage gets tight, re-cloning GCC and Blender as blobless sparse checkouts could save 1–2 GB.

The `.git/` directories account for most of the weight — the checked-out working files are a fraction of each repo's size.

## How to Update This File

```bash
cd ~/Documents/university-coding
du -sh          # total
du -sh 0*/      # per unit
du -sh 01/*/    # per repo within a unit
```
