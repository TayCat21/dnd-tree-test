# D&D species information site

A static, dependency-free information site. `index.html` loads `data.js`, `model.js`, `app.js`, and `styles.css`; images are in `assets/`.

Every species has at least one Type. The 30 species in the card sort (`typeBasis: "card-sort"`) take each Type that at least 2 of the 6 categorical sorts gave them; AJ's and Matt's ranked sorts are excluded. The other 43 were not sorted (`typeBasis: "inferred"`), so each takes the Types of its closest studied relative, named in `typeAnalog`. All 73 blocks are also available through Size and global search. A–Z navigation is removed. The Design notes page records the hierarchy, color scheme, and Gestalt rationale.

Images are publicly available D&D Beyond species artwork. Each record preserves its original source URL; cards display source links. Search runs locally, without AI or external services.

Run `node species-guide/verify.cjs` from the repository root. Changes on `main` publish automatically to https://ty-oustrich.github.io/dnd-tree-test/species-guide/.
