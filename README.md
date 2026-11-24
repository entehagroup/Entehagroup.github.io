# Enteha Group website — https://entehagroup.github.io

Static bilingual site for GitHub Pages: English at the root, Persian under `/fa/`.

**All pages are generated.** Do not edit the HTML files by hand; edit `site-src/content_site.py` and run

    python3 site-src/build_site.py

See `site-src/README.md` (in Persian) for how to change text, add a project or a clip, set Google
Analytics, and the domain/DNS setup.

## Domain
The canonical site is served at `https://entehagroup.github.io`. Keep the GitHub Pages custom domain empty. Redirect requests for `entehagroup.ir` to the corresponding Pages URL in Cloudflare.

## Contact form
Uses Formspree (`FORMSPREE` in `site-src/content_site.py`); messages arrive with the subject
"Enteha Group website — new message".
