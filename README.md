# Enteha Group — website (v1.4)

Includes both resume PDFs (English and Persian, Dubai font, fonts embedded).

Static bilingual site (English default, Persian toggle) for GitHub Pages.

## Deploy
1. Create the organization `entehagroup` on GitHub.
2. Inside it, create a **public** repository named exactly `entehagroup.github.io`.
3. Upload every file in this folder to the repository root (keep `index.html` at the top level).
4. Settings → Pages → Source: *Deploy from a branch* → `main` / root.
5. The site goes live at https://entehagroup.github.io/ within a few minutes.

## Language
- Default is English. The globe button switches language; the visitor's choice is remembered.
- Direct links: `?lang=en` or `?lang=fa` (e.g. https://entehagroup.github.io/?lang=fa).

## Renaming the group later
The name appears in `index.html`, `robots.txt`, `sitemap.xml`. Replace:
- `Enteha Group` (English name)
- `گروه فنی مهندسی انتها` (Persian name)
- `entehagroup.github.io` (address, if the organization name changes)

## Contact form
Uses the same Formspree endpoint as the personal site. Messages from this site arrive
with the subject line "Enteha Group website — new message" so they are easy to tell apart.

## Resume PDFs
`enteha-resume-en-v1.4.pdf` and `enteha-resume-fa-v1.4.pdf` are linked from the hero buttons.
If you publish a new version, update the file names in `index.html` and `sitemap.xml`.

## Logo
`logo.png` (512 px, round, transparent corners) is used for Google and the apple-touch icon;
`logo-96.webp` is the mark in the top bar; `favicon.png` / `favicon.ico` are the browser-tab icons.

## Clips
Clips are listed in `clips.js` (field guide at the top of that file). Each clip needs an MP4
(`v-<slug>.mp4`, H.264, ideally under 10 MB) and a poster (`v-<slug>.jpg`, 540×960 for vertical)
next to `index.html`. While the list is empty, the Clips section and its menu link are hidden.

## Service pages
Persian: `custom-machines.html`, `automation.html`, `parts-manufacturing.html` (site root).
English: the same names under `en/`. They are plain HTML (text, FAQ and schema.org JSON-LD
written in), so search engines and AI crawlers that do not run JavaScript can read them.
All their text lives in `tools/build_services.py`; edit it there and rebuild:

    python3 tools/build_services.py

`services.css` styles these pages. If you change a page, also update the date in `UPDATED`
(in the build script) and `<lastmod>` in `sitemap.xml`.

## AI search
`llms.txt` is a plain summary of the group and its services for AI assistants; keep its facts in
step with the service pages. `robots.txt` explicitly allows the AI crawlers.
