---
name: deploy-species-guide
description: Commit, push, deploy, and verify this project's GitHub Pages species guide after every UI change, with content-addressed CSS and JavaScript to prevent stale assets.
---

# Deploy species guide

Run from the `github-collaboration` repository root. The user authorized this workflow after every UI change; apply it without requesting repeat deployment permission, unless the user overrides that instruction.

1. Inspect `git status` and the diff. Include the intended UI changes and their release artifacts; preserve unrelated changes. Run `node species-guide/verify.cjs` and any focused checks required by the edit.
2. Run `python3 skills/deploy-species-guide/scripts/release.py prepare`. It copies the current CSS and JavaScript to content-addressed filenames, updates the entrypoint, and adds a release marker. Edit source files, then regenerate releases. Also regenerate after merging or rebasing: a merge can keep an older `index.html` that loads stale release files, which `verify.cjs` now reports; keep older release assets so previously opened HTML remains functional. Species artwork is untouched by this step.
3. Review and stage the intended source files, `species-guide/index.html`, generated `species-guide/releases/` files, and any changed deployment instructions. Commit with an accurate message. Push to `origin main`, which is the configured GitHub Pages publishing branch. If on another branch, inspect the difference and integrate the intended changes into main without overwriting unrelated work. Resolve ordinary non-fast-forward updates; never force-push.
4. Confirm GitHub Pages built the pushed commit: inspect `gh api repos/Ty-Oustrich/dnd-tree-test/pages/builds/latest` and compare its commit with the pushed SHA. Wait between status checks, up to ten minutes. If the build fails, inspect its error and fix the cause. If it stalls or access fails, report the actual deployment state and blocker.
5. Run `python3 skills/deploy-species-guide/scripts/release.py verify`. This fetches a release-specific page URL with cache revalidation requested, checks the complete HTML against the local entrypoint, and checks every referenced release asset byte for byte. Retry propagation failures with bounded waits within the ten-minute deployment window. Success requires both the correct Pages build and matching live files.
6. Open the printed release-specific URL in the browser and inspect the changed screen. Return that clickable URL and the commit ID. Report deployment as complete only after live verification succeeds.

The new asset filenames bypass cached CSS and JavaScript. The release-specific page URL bypasses an older cached entrypoint. GitHub Pages controls HTTP response headers; this workflow cannot force an already-open tab to refresh. Always give the fresh URL. Changes to additional local stylesheets, scripts, or other browser assets require extending the release helper to version and verify those assets too.
