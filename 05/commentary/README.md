# Commentary — Unit 05: Public Enterprise

This directory is the annotation layer for Unit 05. There are six primary subjects: LaTeX/TeX, Glimpse/GIMP, Minecraft, SageMath, SourceForge, and Pure Data. The commentary lives alongside all of them.

---

## Structure

```
commentary/
├── README.md              ← you are here
├── vision.md              ← extended frame: what public enterprise means
├── latex.md               ← TeX, WEB, literate programming, π versioning
├── gimp.md                ← GIMP, Glimpse, plugins, the Berkeley origin
├── minecraft.md           ← public development, modding, enclosure
├── sage.md                ← SageMath, the four M's, mathematics as commons
├── sourceforge.md         ← the rise, the betrayal, what infrastructure means
└── puredata.md            ← Pure Data, live coding, the patch as art
```

---

## The challenge of this unit

Six projects is a lot. They are not obviously related. The temptation is to treat this as six separate units bundled together.

Resist that. The theme is real: these are six different ways of enacting the same principle. The commentary connects them to each other and backward to previous units. The student's job is to find the thread.

The commentary for each project follows the usual structure (numbers, code, reading, connections, moment) but emphasizes *connections* more than in earlier units — across projects, and across the whole course.

---

## Repositories

Not all six projects have a single canonical repository. Some notes:

- **TeX:** source in WEB/CWEB at tug.org/texlive/svn/. The most interesting read is `tex.web` — the full source in literate form.
- **LaTeX:** github.com/latex3/latex2e — the LaTeX2e kernel.
- **GIMP:** gitlab.gnome.org/GNOME/gimp — current development on GNOME's GitLab.
- **Minecraft:** closed source. The modding frameworks — Forge (github.com/MinecraftForge) and Fabric (github.com/FabricMC) — are open.
- **SageMath:** github.com/sagemath/sage — large Python/Cython codebase.
- **SourceForge:** no longer open source. Historical artifacts at archive.org.
- **Pure Data:** github.com/pure-data/pure-data — Pd itself; externals are scattered across repositories.

The `scratch/` directory provides starting points for engaging with each.
