# Entha Group — website (v1.0)

Includes both resume PDFs (English and Persian, Dubai font, fonts embedded).

Static bilingual site (English default, Persian toggle) for GitHub Pages.

## Deploy
1. Create the organization `enthagroup` on GitHub.
2. Inside it, create a **public** repository named exactly `enthagroup.github.io`.
3. Upload every file in this folder to the repository root (keep `index.html` at the top level).
4. Settings → Pages → Source: *Deploy from a branch* → `main` / root.
5. The site goes live at https://enthagroup.github.io/ within a few minutes.

## Language
- Default is English. The globe button switches language; the visitor's choice is remembered.
- Direct links: `?lang=en` or `?lang=fa` (e.g. https://enthagroup.github.io/?lang=fa).

## Renaming the group later
The name appears in `index.html`, `robots.txt`, `sitemap.xml`. Replace:
- `Entha Group` (English name)
- `گروه فنی مهندسی انتها` (Persian name)
- `enthagroup.github.io` (address, if the organization name changes)

## Contact form
Uses the same Formspree endpoint as the personal site. Messages from this site arrive
with the subject line "Entha Group website — new message" so they are easy to tell apart.

## Resume PDFs
`entha-resume-en-v1.0.pdf` and `entha-resume-fa-v1.0.pdf` are linked from the hero buttons.
If you publish a new version, update the file names in `index.html` and `sitemap.xml`.
