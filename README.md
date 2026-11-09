# Enteha Group website — https://entehagroup.ir

Static bilingual site for GitHub Pages: English at the root, Persian under `/fa/`.

**All pages are generated.** Do not edit the HTML files by hand; edit `site-src/content_site.py` and run

    python3 site-src/build_site.py

See `site-src/README.md` (in Persian) for how to change text, add a project or a clip, set Google
Analytics, and the domain/DNS setup.

## Domain
The site is served at `https://entehagroup.ir` (`CNAME` in the root). DNS is on Cloudflare:
four A records for `@` (185.199.108.153, .109, .110, .111) and a CNAME `www` → `entehagroup.github.io`,
all **DNS only** (grey cloud; with the proxy on, GitHub cannot issue the HTTPS certificate).
GitHub redirects `entehagroup.github.io` to the domain page by page. To go back to the github.io
address, remove the domain in Settings → Pages.

## Contact form
Uses Formspree (`FORMSPREE` in `site-src/content_site.py`); messages arrive with the subject
"Enteha Group website — new message".
