# D&D Species Tree Test

A dependency-free, low-fidelity clickable wireframe for testing how participants find D&D species information through card-sort-derived categories and a relative-size facet.

## Run locally

Serve this directory with any static web server, then open `index.html` through that server. For example:

```sh
python3 -m http.server 4173
```

## Update the final tasks

Edit `window.TASKS` near the bottom of `data.js`. Each task needs a unique `id`, participant-facing `prompt`, an `answer` summary for the CSV, and either `acceptedNames` or `criteria` for scoring.

## Update classifications

Edit the applicable species record in `data.js`. The `types` array enables intentional cross-listing. `size` must be `Small`, `Medium`, or `Large`. Commonality assignments are defined in `COMMONALITY_BY_NAME`; names not listed there default to `Rare`.

## Data collection

Completed test sessions are stored in this browser's local storage and are never transmitted. The main menu's Download CSV button exports all completed sessions as one file containing event rows and task-result rows. Free-roam activity is not recorded, and refreshing or closing the page still clears an unfinished session. Completed data remains available on the same browser and device until that site's browser storage is cleared.

## GitHub Pages

The site uses only relative static assets and can be served directly from the repository root through GitHub Pages.


## Collaborative website (v1)

- Website: https://ty-oustrich.github.io/dnd-tree-test/species-guide/
- Website source: `species-guide/`
- The repository root preserves the original tree-test wireframe.

### Work together

Clone this repository and edit `species-guide/`. TayCat21 has been invited as a collaborator with write access; the invitation must be accepted before pushing.

For larger changes, create a branch, push it, and open a pull request so the other teammate can review. Small agreed changes can go directly to `main`. GitHub Pages publishes `main` automatically; allow a minute or two after pushing.

Edit `species-guide/data.js` for species records, category membership, keywords, and image sources. Edit `species-guide/app.js` for the shared card template and navigation; `styles.css` controls appearance and `model.js` implements local search.

Run `node species-guide/verify.cjs` to check hierarchy, all 73 blocks, images, and search. For a local preview, run `python3 -m http.server 4173` from the repository root, then visit http://localhost:4173/species-guide/.

The separate ChatGPT Sites URL is a published snapshot. GitHub edits automatically update the GitHub Pages URL above; they do not update the ChatGPT Sites snapshot.

Species cards show original concise summaries based on the public D&D Beyond species listing, with links to the species source pages. These summaries are paraphrases, not verbatim official descriptions. Size, Type, and Commonality remain available to filtering, sorting, and search without appearing as metadata on the cards.
