# D&D species information site

A static, dependency-free information site. `index.html` loads `data.js`, `model.js`, `app.js`, and `styles.css`; images are in `assets/`.

Type follows the tree-test report's exact 22 named placements. All 73 original blocks remain available through Size and global search. Users can sort species by A–Z or Commonality; the selected order persists when changing Type or Size filters. The Design notes page records the hierarchy, color scheme, and Gestalt rationale.

Images are publicly available D&D Beyond species artwork. Each record preserves its original source URL; cards display source links. Search runs locally, without AI or external services.

Run `node species-guide/verify.cjs` from the repository root. Changes on `main` publish automatically to https://ty-oustrich.github.io/dnd-tree-test/species-guide/.
