# Enteha Group — website (v1.1)

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
`enteha-resume-en-v1.1.pdf` and `enteha-resume-fa-v1.1.pdf` are linked from the hero buttons.
If you publish a new version, update the file names in `index.html` and `sitemap.xml`.
