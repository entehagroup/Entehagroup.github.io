# -*- coding: utf-8 -*-
"""سازنده‌ی سایت انتها: همه‌ی صفحه‌ها (انگلیسی در ریشه، فارسی در /fa/) را از content_site.py می‌سازد.
اجرا از ریشه‌ی ریپازیتوری:  python3 site-src/build_site.py
خروجی‌ها در ریشه‌ی ریپازیتوری نوشته می‌شوند؛ HTMLهای خروجی را دستی ویرایش نکنید.
"""
import datetime, html, json, os, re, shutil, sys

SRC = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(SRC)
sys.path.insert(0, SRC)
from content_site import *  # noqa

TODAY = datetime.date.today()
LANGS = ("en", "fa")
OTHER = {"en": "fa", "fa": "en"}
PROJ = {p["slug"]: p for p in PROJECTS}
SVC = {s["slug"]: s for s in SERVICES}
ARROW = {"fa": "←", "en": "→"}
ORG_ID = BASE + "/#org"
SITE_ID = BASE + "/#website"


def esc(s): return html.escape(str(s), quote=True)
def plain(s): return html.unescape(re.sub(r"<[^>]+>", "", str(s)))
def fa_num(s): return str(s).translate(str.maketrans("0123456789", "۰۱۲۳۴۵۶۷۸۹"))
def jalali_year(d): return d.year - 621 if (d.month, d.day) >= (3, 21) else d.year - 622


# ---------------------------------------------------------------- آدرس‌ها
def url(page, L, slug=None):
    pre = "" if L == "en" else "/fa"
    if page == "index": return pre + "/"
    if page == "project": return f"{pre}/projects/{slug}.html"
    return f"{pre}/{page}.html"   # services, projects, about، و slug صفحه‌های خدمات


def absu(path): return BASE + path


def out_path(path):
    p = path.lstrip("/")
    if p == "" or p.endswith("/"): p += "index.html"
    return os.path.join(ROOT, p)


def thumb(src): return re.sub(r"\.(\w+)$", r"-t.\1", src)


# ---------------------------------------------------------------- آیکون‌ها
def svg(paths, w=24):
    return (f'<svg viewBox="0 0 24 24" width="{w}" height="{w}" fill="none" stroke="currentColor" stroke-width="1.8" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{paths}</svg>')


ICON = {
 "medal": '<circle cx="12" cy="8" r="6"/><path d="M8.2 13.5L7 22l5-3 5 3-1.2-8.5"/>',
 "trophy": '<path d="M8 21h8M12 17v4M7 4h10v5a5 5 0 0 1-10 0V4z"/><path d="M17 5h3v2a3 3 0 0 1-3 3M7 5H4v2a3 3 0 0 0 3 3"/>',
 "star": '<path d="M12 3l2.8 5.7 6.2.9-4.5 4.4 1.1 6.2L12 17.3 6.4 20.2l1.1-6.2L3 9.6l6.2-.9z"/>',
 "phone": '<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.7a2 2 0 0 1-.5 2.1L8.1 9.8a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.7.7a2 2 0 0 1 1.7 2z"/>',
 "email": '<rect x="2" y="4" width="20" height="16" rx="2"/><path d="M2 7l10 6 10-6"/>',
 "instagram": '<rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><path d="M17.5 6.5v.01"/>',
 "linkedin": '<rect x="3" y="3" width="18" height="18" rx="3"/><path d="M8 10v7M8 7v.01M12 17v-4a2 2 0 0 1 4 0v4M12 10v7"/>',
 "globe": '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3a14 14 0 0 1 0 18M12 3a14 14 0 0 0 0 18"/>',
}


# ---------------------------------------------------------------- داده‌ی ساخت‌یافته (JSON-LD)
def person_node(k, L):
    p = PEOPLE[k]
    return {"@type": "Person", "@id": BASE + "/#" + {"h": "hassan", "a": "alireza", "m": "mostafa"}[k],
            "name": p["name"]["en"], "alternateName": p["name"]["fa"], "jobTitle": plain(p["role"][L]),
            "description": plain(p["bio"][L]), "image": BASE + "/" + p["por"], "sameAs": [p["linkedin"]],
            "worksFor": {"@id": ORG_ID}}


def org_full(L):
    return {
        "@type": "Organization", "@id": ORG_ID, "name": NAME["en"], "alternateName": ALT_NAMES,
        "description": HOME[L]["desc"], "disambiguatingDescription": DISAMBIG[L],
        "url": BASE + "/", "logo": {"@type": "ImageObject", "url": BASE + "/logo.png", "width": 512, "height": 512},
        "image": BASE + "/og-image.jpg", "email": "mailto:" + EMAIL, "telephone": PHONE,
        "address": [{"@type": "PostalAddress", "addressLocality": "Tehran", "addressCountry": "IR"},
                    {"@type": "PostalAddress", "addressLocality": "Isfahan", "addressCountry": "IR"}],
        "areaServed": {"@type": "Country", "name": "Iran"},
        "contactPoint": {"@type": "ContactPoint", "telephone": PHONE, "email": EMAIL, "contactType": "sales",
                         "areaServed": "IR", "availableLanguage": ["fa", "en"]},
        "sameAs": [INSTAGRAM],
        "knowsAbout": ["Special-purpose machine design", "Industrial robots", "Test rigs", "Mechanism design", "Finite element analysis",
                       "PLC programming", "HMI design", "Motion control", "Production line automation", "CNC machining", "Laser cutting",
                       "Welded structures", "Plastic injection moulds", "Reverse engineering", "3D printing", "Medical robotics",
                       "طراحی و ساخت دستگاه خاص‌منظوره", "ربات صنعتی", "اتوماسیون خط تولید", "ساخت قطعات صنعتی"],
        "member": [person_node(k, L) for k in ("h", "a", "m")],
        "award": [plain(h["en"][0]) for h in HONORS],
        "hasOfferCatalog": {"@type": "OfferCatalog", "name": UI[L]["nav"][0][1], "itemListElement": [
            {"@type": "Offer", "itemOffered": {"@type": "Service", "@id": absu(url(s["slug"], L)) + "#service",
                                               "name": plain(s[L]["h1"]), "url": absu(url(s["slug"], L))}} for s in SERVICES]},
    }


def org_ref(): return {"@type": "Organization", "@id": ORG_ID, "name": NAME["en"], "url": BASE + "/"}


def website_node():
    return {"@type": "WebSite", "@id": SITE_ID, "url": BASE + "/", "name": NAME["en"], "alternateName": NAME["fa"],
            "inLanguage": ["en", "fa"], "publisher": {"@id": ORG_ID}}


def webpage(L, path, name, desc, kind="WebPage", **kw):
    n = {"@type": kind, "@id": absu(path) + "#page", "url": absu(path), "name": name, "description": desc, "inLanguage": L,
         "isPartOf": {"@id": SITE_ID}, "dateModified": TODAY.isoformat(), "breadcrumb": {"@id": absu(path) + "#bc"}}
    n.update(kw)
    return n


def breadcrumbs(path, items):
    return {"@type": "BreadcrumbList", "@id": absu(path) + "#bc", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": plain(n), "item": absu(p)} for i, (n, p) in enumerate(items)]}


def clip_ld(c, L):
    return {"@type": "VideoObject", "@id": BASE + "/#clip-" + c["slug"], "name": c[L]["title"], "description": c[L]["desc"],
            "thumbnailUrl": BASE + "/" + c["poster"], "contentUrl": BASE + "/" + c["video"], "uploadDate": c["date"],
            "duration": c.get("duration", ""), "inLanguage": "fa", "publisher": {"@id": ORG_ID}}


def ld_script(nodes):
    return '<script type="application/ld+json">' + json.dumps({"@context": "https://schema.org", "@graph": nodes}, ensure_ascii=False) + "</script>"


# ---------------------------------------------------------------- اسکلت صفحه
def ga():
    if not GA_ID: return ""
    return f"""
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id={GA_ID}"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  gtag('js', new Date());
  gtag('config', '{GA_ID}');
</script>"""


def head(L, title, desc, path, alt_path, nodes, og_img="/og-image.jpg", og_type="website", extra="", robots="index, follow, max-image-preview:large"):
    en_p = path if L == "en" else alt_path
    fa_p = alt_path if L == "en" else path
    v = TODAY.strftime("%Y%m%d")
    return f"""<!DOCTYPE html>
<html lang="{L}" dir="{'rtl' if L == 'fa' else 'ltr'}">
<head>
<meta charset="UTF-8">{ga()}
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<meta name="author" content="{esc(NAME[L])}">
<meta name="robots" content="{robots}">{extra}
<link rel="canonical" href="{absu(path)}">
<link rel="alternate" hreflang="en" href="{absu(en_p)}">
<link rel="alternate" hreflang="fa" href="{absu(fa_p)}">
<link rel="alternate" hreflang="x-default" href="{absu(en_p)}">
<link rel="icon" type="image/png" href="/favicon.png">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<meta name="theme-color" content="#16191D">
<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="{esc(NAME[L])}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{absu(path)}">
<meta property="og:locale" content="{'fa_IR' if L == 'fa' else 'en_US'}">
<meta property="og:locale:alternate" content="{'en_US' if L == 'fa' else 'fa_IR'}">
<meta property="og:image" content="{BASE}{og_img}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{esc(title)}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(title)}">
<meta name="twitter:description" content="{esc(desc)}">
<meta name="twitter:image" content="{BASE}{og_img}">
{ld_script(nodes)}
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/site.css?v={v}">
</head>
<body>
"""


def nav(L, active, alt_path):
    u = UI[L]
    links = "".join(f'<a href="{url(p, L)}"{" class=\"active\" aria-current=\"page\"" if p == active else ""}>{t}</a>' for p, t in u["nav"])
    other = OTHER[L]
    return f"""<nav><div class="wrap">
  <a href="{url("index", L)}" class="brand"><img class="mk" src="/logo-96.webp" width="34" height="34" alt="{esc(u["logo_alt"])}">{NAME[L]}</a>
  <div class="menu">{links}<a href="#contact" class="nav-cta">{u["contact"]}</a></div>
  <div class="tools">
    <a class="lang" href="{alt_path}" hreflang="{other}" lang="{other}">{svg(ICON["globe"], 15)}{u["lang_label"]}</a>
    <a href="tel:{PHONE}" class="nav-phone" aria-label="{u["call"]}">{svg(ICON["phone"], 17)}</a>
  </div>
</div></nav>
<main>
"""


def contact_section(L, source):
    c = CONTACT[L]
    ext = ' target="_blank" rel="noopener"'
    return f"""<section class="block contact" id="contact"><div class="wrap">
  <h2 class="reveal">{c["h"]}</h2>
  <p class="reveal">{c["p"]}</p>
  <form class="cform reveal" id="contactForm" action="{FORMSPREE}" method="POST">
    <input type="hidden" name="_subject" value="Enteha Group website — new message">
    <input type="hidden" name="source" value="{absu(source)}">
    <div class="cf-row">
      <input type="text" name="name" placeholder="{c["name"]}" aria-label="{c["name"]}" required>
      <input type="email" name="email" placeholder="{c["email"]}" aria-label="{c["email"]}" required>
    </div>
    <textarea name="message" rows="4" placeholder="{c["msg"]}" aria-label="{c["msg"]}" required></textarea>
    <button type="submit" class="cf-btn">{c["send"]}</button>
    <div class="cf-status" id="cfStatus" role="status" aria-live="polite"></div>
  </form>
  <p class="c-other reveal">{c["other"]}</p>
  <div class="c-links reveal">
    <a href="mailto:{EMAIL}">{svg(ICON["email"], 18)}<span>{EMAIL}</span></a>
    <a href="tel:{PHONE}">{svg(ICON["phone"], 18)}<span>{PHONE_TXT[L]}</span></a>
    <a href="{INSTAGRAM}"{ext} data-contact="instagram">{svg(ICON["instagram"], 18)}<span>{INSTAGRAM_HANDLE}</span></a>
  </div>
</div></section>
"""


def footer(L):
    u = UI[L]
    yr = fa_num(jalali_year(TODAY)) if L == "fa" else str(TODAY.year)
    links = "".join(f'<a href="{url(p, L)}">{t}</a>' for p, t in u["nav"])
    links += "".join(f'<a href="{url(s["slug"], L)}" data-service="{s["slug"]}" data-place="footer">{s[L]["nav"]}</a>' for s in SERVICES)
    return f"""</main>
<footer>
  <div class="f-links">{links}</div>
  © {yr} {NAME[L]} — {u["rights"]}
</footer>
<a href="tel:{PHONE}" class="fab-phone" aria-label="{u["call"]}">{svg(ICON["phone"], 23)}</a>
<script src="/assets/site.js?v={TODAY.strftime('%Y%m%d')}" defer></script>
</body>
</html>
"""


def page_hero(L, kk, h1, leads=(), crumbs=None, meta=None, btns=""):
    c = ""
    if crumbs:
        c = '<div class="crumbs">' + '<span class="sep">/</span>'.join(
            f'<a href="{p}">{n}</a>' if p else f'<span aria-current="page">{n}</span>' for n, p in crumbs) + "</div>"
    m = ('<div class="ph-meta">' + "".join(meta) + "</div>") if meta else ""
    ls = "".join(f'<p class="lead">{x}</p>' for x in leads)
    return f"""<header class="page-hero"><div class="wrap">
  {c}<div class="kk">{kk}</div><h1>{h1}</h1>{ls}{m}{btns}
</div></header>
"""


def head_block(kk, h, p=""):
    return f'<div class="head reveal"><div class="kk">{kk}</div><h2>{h}</h2>{f"<p>{p}</p>" if p else ""}</div>'


def more(L, href, text, attrs=""):
    return f'<div class="center"><a class="more-link" href="{href}"{attrs}>{text}</a></div>'


# ---------------------------------------------------------------- بخش‌های مشترک
def avs(who, L, size=56):
    return "".join(f'<img class="av" src="/{PEOPLE[k]["av"]}" alt="{esc(PEOPLE[k]["name"][L])}" title="{esc(PEOPLE[k]["name"][L])}" width="{size}" height="{size}" loading="lazy">' for k in who)


def project_row(p, i, L, place):
    d, im = p[L], p["imgs"][0]
    yr = p["year"][L]
    n = len(p["imgs"])
    sub = []
    if yr: sub.append((UI[L]["year"] + " " + yr) if L == "fa" else yr)
    if n > 1: sub.append(f'{fa_num(n) if L == "fa" else n} {UI[L]["photos"]}')
    subh = f'<div class="pt-sub">{("، " if L == "fa" else " · ").join(sub)}</div>' if sub else ""
    num = fa_num(f"{i + 1:02d}") if L == "fa" else f"{i + 1:02d}"
    return (f'<li class="pli"><a class="prow" href="{url("project", L, p["slug"])}" data-project="{p["slug"]}" data-place="{place}">'
            f'<span class="pn">{num}</span>'
            f'<img class="pthumb" src="/{thumb(im[0])}" alt="{esc(plain(d["title"]))}" loading="lazy" width="{im[1]}" height="{im[2]}">'
            f'<div class="pinfo"><div class="pt-title">{d["title"]}</div>{subh}</div>'
            f'<span class="who">{avs(p["who"], L)}</span><span class="pchev">{UI[L]["view"]}</span></a></li>')


def service_card(s, i, L, place):
    d, u = s[L], UI[L]
    lis = "".join(f"<li>{x}</li>" for x in d["card_list"])
    exs = "".join(f'<a class="exb" href="{url("project", L, sl)}" data-project="{sl}" data-place="service-card">{PROJ[sl][L]["title"]}</a>' for sl in s["examples"])
    return (f'<div class="svc reveal"><div class="ico">{SVC_ICONS[i]}</div>'
            f'<h3><a href="{url(s["slug"], L)}" data-service="{s["slug"]}" data-place="{place}">{d["card_h"]}</a></h3>'
            f'<p class="sd">{d["card_p"]}</p><ul>{lis}</ul>'
            f'<div class="exs"><span class="exl">{u["examples"]}</span>{exs}</div>'
            f'<div class="svc-links"><a class="svc-more" href="{url(s["slug"], L)}" data-service="{s["slug"]}" data-place="{place}">{u["details"]}</a>'
            f'<a class="svc-cta" href="#contact">{u["quote"]}</a></div></div>')


def member_card(k, L):
    p = PEOPLE[k]
    return f"""<div class="member reveal" id="member-{k}">
  <img class="ph" src="/{p["por"]}" alt="{esc(p["name"][L])}" loading="lazy" width="124" height="124">
  <h3>{p["name"][L]}</h3>
  <span class="role">{p["role"][L]}</span>
  <p class="edu">{p["edu"][L]}</p>
  <p class="bio">{p["bio"][L]}</p>
  <a class="li" href="{p["linkedin"]}" target="_blank" rel="noopener" data-contact="linkedin">{svg(ICON["linkedin"], 16)}{UI[L]["linkedin"]}</a>
</div>"""


def honor_card(h, L):
    t, p = h[L]
    return (f'<div class="card reveal{" top" if h["top"] else ""}"><span class="who">{avs(h["who"], L)}</span>'
            f'<div class="ico">{svg(ICON[h["icon"]], 23)}</div><h3>{t}</h3><p>{p}</p></div>')


def clip_card(c, L):
    d = c[L]
    return (f'<article class="m-card"><div class="m-vid v"><video controls playsinline preload="none" poster="/{c["poster"]}" data-id="{c["slug"]}" '
            f'aria-label="{esc(d["title"])}"><source src="/{c["video"]}" type="video/mp4"></video></div>'
            f'<div class="m-bd"><h3>{d["title"]}</h3><div class="m-meta">{d["year"]}</div><p class="m-desc">{d["desc"]}</p></div></article>')


def about_block(L, numbers=True):
    paras = [x[L] for x in ABOUT_PARAS]
    if numbers: paras.insert(1, HOME[L]["numbers"])
    facts = "".join(f'<div class="fact"><span class="k">{f[L][0]}</span><span class="v">{f[L][1]}</span></div>' for f in ABOUT_FACTS)
    return (f'<div class="about"><div class="reveal">{"".join(f"<p>{x}</p>" for x in paras)}</div>'
            f'<div class="facts reveal">{facts}</div></div>')


# ---------------------------------------------------------------- نوشتن صفحه
PAGES = []


def write(path, content, sitemap=True):
    fp = out_path(path)
    os.makedirs(os.path.dirname(fp), exist_ok=True)
    open(fp, "w", encoding="utf-8").write(content)
    if sitemap: PAGES.append(path)


# ---------------------------------------------------------------- صفحه‌ی اصلی
def build_home(L):
    h, u = HOME[L], UI[L]
    path, alt = url("index", L), url("index", OTHER[L])
    nodes = [org_full(L), website_node(),
             webpage(L, path, h["title"], h["desc"], about={"@id": ORG_ID}, mainEntity={"@id": ORG_ID},
                     primaryImageOfPage=BASE + "/og-image.jpg"),
             breadcrumbs(path, [(u["home"], path)])] + [clip_ld(c, L) for c in CLIPS]
    extra = ""
    if L == "en":
        extra = ('\n<meta name="google-site-verification" content="fU2lqYzDNWrzfksv2M-7JnUH_YPVxpO9Hlq-vi2N9NU">'
                 "\n<script>if(/[?&]lang=fa\\b/.test(location.search))location.replace('/fa/');</script>")
    trio = "".join(f'<img src="/{PEOPLE[k]["por"]}" width="420" height="420" alt="{esc(PEOPLE[k]["name"][L])}">' for k in ("h", "a", "m"))
    svcs = "".join(service_card(s, i, L, "home") for i, s in enumerate(SERVICES))
    rows = "".join(project_row(p, i, L, "home") for i, p in enumerate(PROJECTS))
    clips = "".join(clip_card(c, L) for c in CLIPS)
    team = "".join(member_card(k, L) for k in ("h", "a", "m"))
    hons = "".join(honor_card(x, L) for x in HONORS if x["top"])
    body = f"""<header class="hero" id="top">
  <div class="cover"><picture><source srcset="/cover.webp" type="image/webp">
    <img src="/cover.jpg" width="2172" height="724" alt="{esc(u["cover_alt"])}" fetchpriority="high"></picture></div>
  <div class="wrap profile">
    <div class="intro">
      <img class="hero-logo" src="/logo-256.webp" srcset="/logo-256.webp 1x, /logo-512.webp 2x" width="128" height="128" alt="{esc(u["logo_alt"])}">
      <span class="eyebrow">{HERO["eyebrow"][L]}</span>
      <h1>{NAME[L]}</h1>
      <p class="headline">{HERO["headline"][L]}</p>
      <p class="lead">{HERO["lead"][L]}</p>
      <div class="btns">
        <a class="btn btn-gold" href="{url("services", L)}">{h["cta1"]}</a>
        <a class="btn btn-ghost" href="{url("projects", L)}">{h["cta2"]}</a>
        <a class="btn-link" href="/{RESUME["en"]}" download>{u["resume_en"]}</a>
        <a class="btn-link" href="/{RESUME["fa"]}" download>{u["resume_fa"]}</a>
      </div>
    </div>
    <div class="trio">{trio}</div>
  </div>
</header>
<section class="block" id="about"><div class="wrap">
  {head_block(h["about_kk"], h["about_h"])}
  {about_block(L)}
  {more(L, url("about", L), u["more_about"])}
</div></section>
<section class="block alt" id="services"><div class="wrap">
  {head_block(h["svc_kk"], h["svc_h"], h["svc_p"])}
  <div class="svc-grid">{svcs}</div>
  {more(L, url("services", L), u["all_services"])}
</div></section>
<section class="block" id="projects"><div class="wrap">
  {head_block(h["proj_kk"], h["proj_h"], h["proj_p"])}
  <ol class="p-list reveal">{rows}</ol>
</div></section>
<section class="block clips" id="clips"><div class="wrap">
  {head_block(h["clip_kk"], h["clip_h"])}
  <div class="m-grid">{clips}</div>
</div></section>
<section class="block alt" id="team"><div class="wrap">
  {head_block(h["team_kk"], h["team_h"], h["team_p"])}
  <div class="t-grid">{team}</div>
</div></section>
<section class="block" id="honors"><div class="wrap">
  {head_block(h["hon_kk"], h["hon_h"], h["hon_p"])}
  <div class="h-grid">{hons}</div>
  {more(L, url("about", L) + "#honors", u["all_honors"])}
</div></section>
"""
    write(path, head(L, h["title"], h["desc"], path, alt, nodes, extra=extra) + nav(L, None, alt) + body + contact_section(L, path) + footer(L))


# ---------------------------------------------------------------- صفحه‌ی خدمات (نمای کلی)
def build_services(L):
    s, u = SERVICES_PAGE[L], UI[L]
    path, alt = url("services", L), url("services", OTHER[L])
    nodes = [org_ref(), webpage(L, path, s["title"], s["desc"], about={"@id": ORG_ID}),
             breadcrumbs(path, [(u["home"], url("index", L)), (s["kk"], path)]),
             {"@type": "ItemList", "name": s["svc_h"], "itemListElement": [
                 {"@type": "ListItem", "position": i + 1, "url": absu(url(x["slug"], L)), "name": plain(x[L]["h1"])} for i, x in enumerate(SERVICES)]},
             {"@type": "FAQPage", "@id": absu(path) + "#faq", "inLanguage": L, "mainEntity": [
                 {"@type": "Question", "name": plain(q), "acceptedAnswer": {"@type": "Answer", "text": plain(a)}} for q, a in FAQ[L]]}]
    svcs = "".join(service_card(x, i, L, "services") for i, x in enumerate(SERVICES))
    steps = "".join(f'<div class="step reveal"><h3>{a}</h3><p>{b}</p></div>' for a, b in STEPS[L])
    why = "".join(f"<li>{w}</li>" for w in WHY[L]["why_list"])
    inds = "".join(f"<li>{x}</li>" for x in WHY[L]["industry_list"])
    faq = "".join(f'<details class="reveal"><summary>{q}</summary><p>{a}</p></details>' for q, a in FAQ[L])
    body = page_hero(L, s["kk"], s["h1"], [s["lead"]], crumbs=[(u["home"], url("index", L)), (s["kk"], None)]) + f"""
<section class="block alt" id="lines"><div class="wrap">
  {head_block(s["kk"], s["svc_h"])}
  <div class="svc-grid">{svcs}</div>
</div></section>
<section class="block" id="process"><div class="wrap">
  {head_block(s["kk"], s["steps_h"])}
  <div class="steps">{steps}</div>
</div></section>
<section class="block alt" id="why"><div class="wrap">
  {head_block(s["kk"], u["why"])}
  <ul class="why-list reveal">{why}</ul>
  <div class="head reveal" style="margin:40px auto 18px"><h2 style="font-size:22px">{u["industries"]}</h2></div>
  <ul class="inds reveal">{inds}</ul>
</div></section>
<section class="block" id="faq"><div class="wrap">
  {head_block(s["kk"], s["faq_h"])}
  <div class="faq">{faq}</div>
</div></section>
"""
    write(path, head(L, s["title"], s["desc"], path, alt, nodes) + nav(L, "services", alt) + body + contact_section(L, path) + footer(L))


# ---------------------------------------------------------------- صفحه‌ی هر خدمت
def build_service(s, L):
    d, u = s[L], UI[L]
    slug = s["slug"]
    path, alt = url(slug, L), url(slug, OTHER[L])
    sp = SERVICES_PAGE[L]
    crumbs = [(u["home"], url("index", L)), (sp["kk"], url("services", L)), (d["nav"], path)]
    svc_node = {"@type": "Service", "@id": absu(path) + "#service", "name": plain(d["h1"]), "serviceType": plain(d["nav"]),
                "description": " ".join(plain(x) for x in d["lead"]), "url": absu(path), "provider": {"@id": ORG_ID},
                "areaServed": {"@type": "Country", "name": "Iran"}, "image": BASE + "/" + s["img"],
                "availableChannel": {"@type": "ServiceChannel", "servicePhone": {"@type": "ContactPoint", "telephone": PHONE}, "serviceUrl": absu(path) + "#contact"},
                "hasOfferCatalog": {"@type": "OfferCatalog", "name": plain(d["what_h"]), "itemListElement": [
                    {"@type": "Offer", "itemOffered": {"@type": "Service", "name": plain(n), "description": plain(x)}} for n, x in d["what"]]},
                "subjectOf": [{"@id": absu(url("project", L, sl)) + "#work"} for sl in dict.fromkeys(pp[0] for pp in d["projects"])]}
    nodes = [org_ref(), webpage(L, path, d["title"], d["desc"], about={"@id": absu(path) + "#service"}, primaryImageOfPage=BASE + "/" + s["img"]),
             breadcrumbs(path, crumbs), svc_node,
             {"@type": "FAQPage", "@id": absu(path) + "#faq", "inLanguage": L, "mainEntity": [
                 {"@type": "Question", "name": plain(q), "acceptedAnswer": {"@type": "Answer", "text": plain(a)}} for q, a in d["faq"]]}]
    facts = "".join(f"<div><dt>{a}</dt><dd>{b}</dd></div>" for a, b in d["facts"])
    what = "".join(f"<li><h3>{a}</h3><p>{b}</p></li>" for a, b in d["what"])
    steps = "".join(f"<li><h3>{a}</h3><p>{b}</p></li>" for a, b in d["steps"])
    pjs = "".join(f'<a class="sv-pj" href="{url("project", L, sl)}" data-project="{sl}" data-place="service-page">'
                  f'<img src="/{img}" alt="{esc(plain(t))}" loading="lazy" width="640" height="480"><div><h3>{t}</h3><p>{x}</p></div></a>'
                  for sl, img, t, x in d["projects"])
    why = "".join(f"<li>{w}</li>" for w in WHY[L]["why_list"])
    inds = "".join(f"<li>{x}</li>" for x in WHY[L]["industry_list"])
    team = "".join(f'<li><img src="/{PEOPLE[k]["av"]}" alt="{esc(PEOPLE[k]["name"][L])}" width="48" height="48" loading="lazy"><div>'
                   f'<a href="{url("about", L)}#member-{k}">{PEOPLE[k]["name"][L]}</a><span>{PEOPLE[k]["role"][L]}</span><small>{PEOPLE[k]["edu"][L]}</small></div></li>'
                   for k in ("h", "a", "m"))
    faq = "".join(f'<div class="qa"><h3>{q}</h3><p>{a}</p></div>' for q, a in d["faq"])
    related = "".join(f'<a href="{url(o["slug"], L)}" data-service="{o["slug"]}" data-place="related">{o[L]["nav"]} {ARROW[L]}</a>' for o in SERVICES if o is not s)
    upd = fa_num(TODAY.isoformat()) if L == "fa" else TODAY.isoformat()
    btns = (f'<div class="btns"><a class="btn btn-gold" href="#contact">{u["start"]}</a>'
            f'<a class="btn btn-ghost" href="tel:{PHONE}">{svg(ICON["phone"], 17)}<span class="ltr">{PHONE_TXT[L]}</span></a></div>')
    body = page_hero(L, sp["kk"], d["h1"], d["lead"], crumbs=[(n, p if i < 2 else None) for i, (n, p) in enumerate(crumbs)], btns=btns) + f"""
<div class="svp">
<section class="block"><div class="wrap">
  <h2 class="sv-h">{u["glance"]}</h2>
  <dl class="sv-facts">{facts}</dl>
</div></section>
<section class="block alt"><div class="wrap">
  <h2 class="sv-h">{d["what_h"]}</h2>
  <ul class="sv-what">{what}</ul>
</div></section>
<section class="block"><div class="wrap">
  <h2 class="sv-h">{u["process"]}</h2>
  <ol class="sv-steps">{steps}</ol>
</div></section>
<section class="block alt"><div class="wrap">
  <h2 class="sv-h">{u["work"]}</h2>
  <div class="sv-pjs">{pjs}</div>
  {more(L, url("projects", L), u["all_projects"])}
</div></section>
<section class="block"><div class="wrap sv-two">
  <div><h2 class="sv-h">{u["why"]}</h2><ul class="why-list">{why}</ul></div>
  <div><h2 class="sv-h">{u["industries"]}</h2><ul class="inds">{inds}</ul>
  <h2 class="sv-h mt">{u["team_h"]}</h2><ul class="sv-team">{team}</ul></div>
</div></section>
<section class="block alt" id="faq"><div class="wrap">
  <h2 class="sv-h">{u["faq"]}</h2>
  <div class="sv-faq">{faq}</div>
</div></section>
<section class="block"><div class="wrap">
  <h2 class="sv-h">{u["related"]}</h2>
  <div class="related">{related}</div>
  <p class="upd">{u["updated"]} <time datetime="{TODAY.isoformat()}">{upd}</time></p>
</div></section>
</div>
"""
    write(path, head(L, d["title"], d["desc"], path, alt, nodes, og_img=f"/og/service-{slug}.jpg") + nav(L, "services", alt) + body + contact_section(L, path) + footer(L))


# ---------------------------------------------------------------- نمونه‌کارها
def build_projects_index(L):
    s, u = PROJECTS_PAGE[L], UI[L]
    path, alt = url("projects", L), url("projects", OTHER[L])
    nodes = [org_ref(),
             webpage(L, path, s["title"], s["desc"], kind="CollectionPage", about={"@id": ORG_ID}, mainEntity={"@type": "ItemList", "itemListElement": [
                 {"@type": "ListItem", "position": i + 1, "url": absu(url("project", L, p["slug"])), "name": plain(p[L]["title"])} for i, p in enumerate(PROJECTS)]}),
             breadcrumbs(path, [(u["home"], url("index", L)), (s["h1"], path)])]
    rows = "".join(project_row(p, i, L, "projects") for i, p in enumerate(PROJECTS))
    body = page_hero(L, s["kk"], s["h1"], [s["lead"]], crumbs=[(u["home"], url("index", L)), (s["h1"], None)]) + f"""
<section class="block"><div class="wrap"><ol class="p-list reveal">{rows}</ol></div></section>
"""
    write(path, head(L, s["title"], s["desc"], path, alt, nodes) + nav(L, "projects", alt) + body + contact_section(L, path) + footer(L))


def build_project(p, i, L):
    d, u = p[L], UI[L]
    path, alt = url("project", L, p["slug"]), url("project", OTHER[L], p["slug"])
    title = f'{plain(d["title"])} | {NAME[L]}'
    desc = plain(d["short"]) + " " + plain(d["desc"][0])
    desc = desc if len(desc) < 300 else desc[:297].rsplit(" ", 1)[0] + "…"
    svc = SVC[p["service"]]
    work = {"@type": "CreativeWork", "@id": absu(path) + "#work", "name": plain(d["title"]), "headline": plain(d["title"]),
            "abstract": plain(d["short"]), "description": plain(" ".join(d["desc"])), "url": absu(path), "inLanguage": L,
            "keywords": ", ".join(plain(t) for t in d["tags"]), "image": [BASE + "/" + im[0] for im in p["imgs"]],
            "creator": [{"@id": person_node(k, L)["@id"], "@type": "Person", "name": PEOPLE[k]["name"]["en"]} for k in p["who"]],
            "producer": {"@id": ORG_ID}, "about": {"@id": absu(url(svc["slug"], L)) + "#service"}}
    if p["date"]: work["dateCreated"] = p["date"]
    nodes = [org_ref(), work,
             webpage(L, path, title, desc, mainEntity={"@id": absu(path) + "#work"}, primaryImageOfPage=BASE + "/" + p["imgs"][0][0]),
             breadcrumbs(path, [(u["home"], url("index", L)), (PROJECTS_PAGE[L]["h1"], url("projects", L)), (d["title"], path)])]
    cap = lambda im: im[3] if L == "fa" else im[4]
    alt_of = lambda im: plain(d["title"]) + ((" — " + cap(im)) if cap(im) else "")
    im0 = p["imgs"][0]
    main = (f'<button type="button" class="main" data-full="/{im0[0]}" data-alt="{esc(alt_of(im0))}" aria-label="{esc(alt_of(im0))}">'
            f'<img src="/{im0[0]}" alt="{esc(alt_of(im0))}" width="{im0[1]}" height="{im0[2]}" fetchpriority="high"></button>')
    thumbs = ""
    if len(p["imgs"]) > 1:
        thumbs = '<div class="thumbs">' + "".join(
            f'<button type="button" data-full="/{im[0]}" data-alt="{esc(alt_of(im))}" aria-label="{esc(alt_of(im))}">'
            f'<img src="/{thumb(im[0])}" alt="{esc(alt_of(im))}" loading="lazy"></button>' for im in p["imgs"]) + "</div>"
    capline = f'<div class="cap">{cap(im0)}</div>' if cap(im0) else ""
    who = "".join(f'<a href="{url("about", L)}#member-{k}"><img src="/{PEOPLE[k]["av"]}" alt="" width="30" height="30">{PEOPLE[k]["name"][L]}</a>' for k in p["who"])
    rows = []
    if p["year"][L]: rows.append((u["year"], p["year"][L]))
    rows.append((u["team_role"], f'<div class="pp-who">{who}</div>'))
    rows.append((u["field"], "، ".join(d["tags"]) if L == "fa" else ", ".join(d["tags"])))
    rows.append((u["service"], f'<a href="{url(svc["slug"], L)}" data-service="{svc["slug"]}" data-place="project">{svc[L]["nav"]}</a>'))
    facts = "".join(f"<tr><th>{a}</th><td>{b}</td></tr>" for a, b in rows)
    prev_p, next_p = PROJECTS[i - 1], PROJECTS[(i + 1) % len(PROJECTS)]
    meta = ([f'<span class="yr">{p["year"][L]}</span>'] if p["year"][L] else []) + [f"<span>{t}</span>" for t in d["tags"]]
    body = page_hero(L, PROJECTS_PAGE[L]["kk"], d["title"], [d["short"]],
                     crumbs=[(u["home"], url("index", L)), (PROJECTS_PAGE[L]["h1"], url("projects", L)), (d["title"], None)], meta=meta) + f"""
<section class="block"><div class="wrap">
  <div class="pp">
    <div class="reveal"><div class="pp-gal" data-lb>{main}{capline}{thumbs}</div></div>
    <div class="pp-txt reveal">
      {"".join(f"<p>{x}</p>" for x in d["desc"])}
      <div class="pp-box"><h2>{u["key_facts"]}</h2><table class="pp-facts">{facts}</table></div>
    </div>
  </div>
</div></section>
<section class="block" style="padding-top:10px"><div class="wrap">
  <div class="pp-cta reveal"><div><h2>{u["similar"]}</h2><p>{u["similar_p"]}</p></div>
    <div class="btns"><a class="btn btn-gold" href="#contact">{u["start"]}</a><a class="btn btn-ghost" href="{url(svc["slug"], L)}" data-service="{svc["slug"]}" data-place="project-cta">{svc[L]["nav"]}</a></div></div>
  <div class="pp-nav">
    <a href="{url("project", L, prev_p["slug"])}" data-project="{prev_p["slug"]}" data-place="prev"><small>{u["prev"]}</small>{prev_p[L]["title"]}</a>
    <a href="{url("project", L, next_p["slug"])}" data-project="{next_p["slug"]}" data-place="next"><small>{u["next"]}</small>{next_p[L]["title"]}</a>
  </div>
</div></section>
"""
    write(path, head(L, title, desc, path, alt, nodes, og_img=f"/og/{p['slug']}.jpg", og_type="article") + nav(L, "projects", alt) + body + contact_section(L, path) + footer(L))


# ---------------------------------------------------------------- درباره
def build_about(L):
    a, u = ABOUT_PAGE[L], UI[L]
    path, alt = url("about", L), url("about", OTHER[L])
    pm = PUB_MAIN
    paper = {"@type": "ScholarlyArticle", "@id": pm["doi"], "name": pm["title"], "headline": pm["title"], "url": pm["doi"], "sameAs": pm["doi"],
             "datePublished": pm["year"], "isPartOf": {"@type": "Periodical", "name": pm["journal"], "publisher": {"@type": "Organization", "name": pm["publisher"]}},
             "author": [{"@type": "Person", "name": n.strip()} for n in re.split(r",|&amp;|&", plain(pm["authors"])) if n.strip()]}
    nodes = [org_full(L), paper,
             webpage(L, path, a["title"], a["desc"], kind="AboutPage", about={"@id": ORG_ID}, mainEntity={"@id": ORG_ID}),
             breadcrumbs(path, [(u["home"], url("index", L)), (a["kk"], path)])]
    team = "".join(member_card(k, L) for k in ("h", "a", "m"))
    hons = "".join(honor_card(x, L) for x in HONORS)
    plist = "".join(f'<li><span class="who lg">{avs(x["who"], L)}</span><div class="body"><div class="pt">{x["title"]}</div><div class="pv">{x["venue"]}</div></div></li>' for x in PUBS)
    skills = "".join(f'<div class="skill-cat reveal"><h3>{s[L][0]}</h3><div class="chips">{"".join(f"<span class=chip>{c}</span>" for c in s[L][1])}</div></div>' for s in SKILLS)
    tl = "".join(f'<div class="tl reveal{" team" if e["team"] else ""}"><div class="row"><span class="when">{e[L][0]}</span><span class="who">{avs(e["who"], L)}</span></div>'
                 f'<h3>{e[L][1]}</h3><div class="org">{e[L][2]}</div><p class="d">{e[L][3]}</p></div>' for e in EXPERIENCE)
    yr = fa_num(pm["year"]) if L == "fa" else pm["year"]
    body = page_hero(L, a["kk"], a["h1"], crumbs=[(u["home"], url("index", L)), (a["kk"], None)]) + f"""
<section class="block" id="about"><div class="wrap">
  {about_block(L)}
</div></section>
<section class="block alt" id="team"><div class="wrap">
  {head_block(HOME[L]["team_kk"], a["team_h"], HOME[L]["team_p"])}
  <div class="t-grid">{team}</div>
</div></section>
<section class="block" id="honors"><div class="wrap">
  {head_block(HOME[L]["hon_kk"], a["hon_h"], HOME[L]["hon_p"])}
  <div class="h-grid">{hons}</div>
</div></section>
<section class="block alt" id="publications"><div class="wrap">
  {head_block(a["kk"], a["pub_h"], a["pub_p"])}
  <div class="pub reveal">
    <div class="top"><span class="jbadge">{pm["badge"]}</span><span class="who lg">{avs(pm["who"], L)}</span></div>
    <div class="ptitle">{pm["title"]}</div>
    <p class="psum">{pm[L]["summary"]}</p>
    <div class="authors">{pm["authors"]}</div>
    <div class="prole">{pm[L]["role"]}</div>
    <div class="pmeta"><span>{u["published"]}: <b>{yr}</b></span><span class="ltr">DOI: {pm["doi"].replace("https://doi.org/", "")}</span></div>
    <a class="plink" href="{pm["doi"]}" target="_blank" rel="noopener">{u["view_paper"]}</a>
  </div>
  <ul class="plist reveal">{plist}</ul>
</div></section>
<section class="block" id="skills"><div class="wrap">
  {head_block(a["kk"], a["skills_h"])}
  {skills}
</div></section>
<section class="block alt" id="experience"><div class="wrap">
  {head_block(a["kk"], a["exp_h"])}
  <div class="timeline">{tl}</div>
</div></section>
"""
    write(path, head(L, a["title"], a["desc"], path, alt, nodes) + nav(L, "about", alt) + body + contact_section(L, path) + footer(L))


# ---------------------------------------------------------------- فایل‌های جانبی
def redirect_stub(old, new):
    """صفحه‌ی کوچک برای آدرس‌های قدیمی؛ GitHub Pages ریدایرکت سروری ندارد."""
    fp = out_path(old)
    os.makedirs(os.path.dirname(fp), exist_ok=True)
    open(fp, "w", encoding="utf-8").write(
        f'<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>{NAME["en"]}</title>'
        f'<link rel="canonical" href="{absu(new)}"><meta name="robots" content="noindex, follow">'
        f'<meta http-equiv="refresh" content="0; url={new}"></head><body><a href="{new}">{absu(new)}</a></body></html>\n')


def build_extras():
    # آدرس‌های قدیمی انگلیسی (/en/…) به صفحه‌های انگلیسی جدید در ریشه
    for s in SERVICES:
        redirect_stub(f"/en/{s['slug']}.html", url(s["slug"], "en"))
    # 404
    u = UI["en"]
    open(os.path.join(ROOT, "404.html"), "w", encoding="utf-8").write(
        head("en", "Page not found | " + NAME["en"], "This page does not exist.", "/404.html", "/404.html", [org_ref()], robots="noindex")
        + nav("en", None, "/fa/") + page_hero("en", "404", "Page not found", ["The page you are looking for does not exist. / این صفحه پیدا نشد."])
        + '<section class="block"><div class="wrap"><div class="btns" style="justify-content:center">'
        + "".join(f'<a class="btn btn-gold" href="{h}">{t}</a>' for h, t in [
            ("/", "Home"), ("/services.html", "Services"), ("/projects.html", "Projects"), ("/fa/", "صفحه‌ی اصلی فارسی")])
        + "</div></div></section>" + footer("en"))
    # sitemap
    rows = []
    for pth in PAGES:
        if pth.startswith("/fa/"): fa_p, en_p = pth, (pth[3:] or "/")
        else: en_p, fa_p = pth, "/fa" + pth
        pri = "1.0" if pth in ("/", "/fa/") else ("0.9" if any(x in pth for x in ("services", "projects.html")) or pth.split("/")[-1][:-5] in SVC else "0.8")
        rows.append(f'  <url><loc>{absu(pth)}</loc><lastmod>{TODAY.isoformat()}</lastmod><priority>{pri}</priority>\n'
                    f'    <xhtml:link rel="alternate" hreflang="en" href="{absu(en_p)}"/><xhtml:link rel="alternate" hreflang="fa" href="{absu(fa_p)}"/>'
                    f'<xhtml:link rel="alternate" hreflang="x-default" href="{absu(en_p)}"/></url>')
    for f in RESUME.values():
        rows.append(f"  <url><loc>{BASE}/{f}</loc><priority>0.5</priority></url>")
    open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8").write(
        '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
        + "\n".join(rows) + "\n</urlset>\n")
    # robots
    bots = ["GPTBot", "OAI-SearchBot", "ChatGPT-User", "ClaudeBot", "Claude-User", "Claude-SearchBot", "PerplexityBot",
            "Perplexity-User", "Google-Extended", "Applebot-Extended", "Bingbot", "Googlebot"]
    open(os.path.join(ROOT, "robots.txt"), "w", encoding="utf-8").write(
        "User-agent: *\nAllow: /\n\n# AI search and assistant crawlers are welcome\n" + "".join(f"User-agent: {b}\n" for b in bots)
        + f"Allow: /\n\nSitemap: {BASE}/sitemap.xml\n")
    # llms.txt
    E = "en"
    L_ = [f"# {NAME['en']} ({NAME['fa']})", "",
          f"> {DISAMBIG['en']} It designs and builds special-purpose machines, test rigs and industrial robots, automates production lines, and manufactures industrial parts to drawing, for clients across Iran. One-off orders are accepted and quotes are free (usually within 1–2 weeks).", "",
          f"> {DISAMBIG['fa']}", "",
          "## Key facts", "",
          "- Based in Tehran and Isfahan, Iran; serves clients across Iran. Website: " + BASE + "/",
          "- Core team: Hassan Nasiri Khonsari (Technical & Design Director), Alireza Pirhaji (Manufacturing & Quality Lead), Seyed Mostafa Banihashemi (Project & R&D Lead); degrees from Sharif University of Technology, IUST, K. N. Toosi University and Tarbiat Modares University; plus a network of partner workshops and specialists.",
          "- Scope: requirements, concept and detailed design, engineering analysis (FEA), fabrication, assembly, quality control and commissioning. The engineer who designs a machine also supervises its fabrication and assembly.",
          "- Track record: 80 postal sorting robots built for Iran Post (50 for Tehran, 30 for Kermanshah, 2020–2025), with a third-generation design produced as a 200-unit series; a 6-DOF knee prosthesis test rig to ASTM F1223, the first of its kind in Iran (2021); five industrial FDM 3D printers up to 500 × 500 × 400 mm (2020–2023); a fleet of seven waiter robots (2021); a dual-purpose CNC with a ~100 × 100 cm bed (2023).",
          "- Past work ranges from machines of 10–250 kg to structures of about 1–2 tonnes.",
          "- Typical timelines: 1–2 weeks to about a year; a simple special-purpose machine takes 1–2 months of design and 1–2 months of fabrication. Quotes are free and take 1–2 weeks.",
          "- Automation: Delta and Siemens PLC, HMI, servo and stepper motion control, weighing and measurement, control cabinets, integration with existing equipment.",
          "- Parts: CNC machining, laser cutting, bending and rolling, welded structures in steel and 316 stainless, pressure vessels and enclosures, plastic injection moulds, dimensional and weld inspection (GD&T), reverse engineering; drawings accepted in any format.",
          "- Support: faults in machines Enteha designed and built are fixed for 2 months after delivery; longer warranty, repairs and upgrades by contract.",
          "- Industries: medical and dental devices, postal and logistics, additive manufacturing, universities and research centres, service robotics.",
          "- Awards: Laureate, 64th Alborz Elite Prize (2026); 2nd place, 26th Khwarizmi Youth Festival (2024); 2nd place, 24th Khwarizmi Youth Festival (2022); best design, 4th Iran Industrial Design Festival (2024); top startup, Sharif Science & Technology Park (2024).",
          f"- Publication: “{PUB_MAIN['title']}”, Scientific Reports, 2025 ({PUB_MAIN['doi']}).", "",
          "## Pages (English)", "",
          f"- [Home]({absu(url('index', E))}): overview", f"- [Services]({absu(url('services', E))}): service lines, process and FAQ"]
    L_ += [f"- [{plain(s['en']['h1'])}]({absu(url(s['slug'], E))}): {plain(s['en']['card_p'])}" for s in SERVICES]
    L_ += [f"- [Projects]({absu(url('projects', E))}): all projects", f"- [About]({absu(url('about', E))}): team, honors, publications, skills, experience", "",
           "## Projects", ""]
    L_ += [f"- [{plain(p['en']['title'])}]({absu(url('project', E, p['slug']))}): {plain(p['en']['short'])}" for p in PROJECTS]
    L_ += ["", "## صفحه‌ها (فارسی)", "", f"- [صفحه‌ی اصلی]({absu(url('index', 'fa'))})", f"- [خدمات]({absu(url('services', 'fa'))})"]
    L_ += [f"- [{plain(s['fa']['h1'])}]({absu(url(s['slug'], 'fa'))})" for s in SERVICES]
    L_ += [f"- [نمونه‌کارها]({absu(url('projects', 'fa'))})", f"- [درباره و تیم]({absu(url('about', 'fa'))})", "",
           "## Contact", "", f"- Phone: {PHONE_TXT['en']}", f"- Email: {EMAIL}", f"- Instagram: {INSTAGRAM}",
           f"- Contact form: {absu(url('index', E))}#contact", "", "## Optional", "",
           f"- [Company resume (English, PDF)]({BASE}/{RESUME['en']})", f"- [رزومه‌ی گروه (فارسی، PDF)]({BASE}/{RESUME['fa']})", ""]
    open(os.path.join(ROOT, "llms.txt"), "w", encoding="utf-8").write("\n".join(L_))
    # CNAME
    open(os.path.join(ROOT, "CNAME"), "w").write(BASE.split("://")[1] + "\n")


def build_og_images():
    try:
        from PIL import Image
    except ImportError:
        print("Pillow not installed: skipping preview images (pip install pillow)"); return
    def fit(src, dst, cover=False):
        if os.path.exists(dst) and os.path.getmtime(dst) >= os.path.getmtime(src): return
        im = Image.open(src).convert("RGB")
        W, H = 1200, 630
        if cover:
            r = max(W / im.width, H / im.height); im = im.resize((round(im.width * r), round(im.height * r)), Image.LANCZOS)
            x, y = (im.width - W) // 2, (im.height - H) // 2; out = im.crop((x, y, x + W, y + H))
        else:
            r = min(W / im.width, H / im.height); im = im.resize((round(im.width * r), round(im.height * r)), Image.LANCZOS)
            out = Image.new("RGB", (W, H), (255, 255, 255)); out.paste(im, ((W - im.width) // 2, (H - im.height) // 2))
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        out.save(dst, quality=82, optimize=True, progressive=True)
    fit(os.path.join(ROOT, "cover.jpg"), os.path.join(ROOT, "og-image.jpg"), cover=True)
    for p in PROJECTS:
        fit(os.path.join(ROOT, p["imgs"][0][0]), os.path.join(ROOT, "og", p["slug"] + ".jpg"))
    for s in SERVICES:
        fit(os.path.join(ROOT, s["img"]), os.path.join(ROOT, "og", "service-" + s["slug"] + ".jpg"))


def check():
    bad = {"ٔ": "همزه‌ی روی ه", "ۀ": "ۀ", "ي": "ي عربی", "ك": "ك عربی"}
    problems = []
    for pth in PAGES + ["/404.html"]:
        s = open(out_path(pth), encoding="utf-8").read()
        for ch, n in bad.items():
            if ch in s: problems.append(f"{pth}: forbidden character {n}")
        for ref in re.findall(r'(?:src|href|data-full|poster|srcset)="(/[^"#?\s]*)', s):
            if ref.endswith("/") or ref.startswith("//"): continue
            if not os.path.exists(os.path.join(ROOT, ref.lstrip("/"))): problems.append(f"{pth}: missing file {ref}")
        for m in re.findall(r'<script type="application/ld\+json">(.*?)</script>', s, re.S):
            json.loads(m)
        if "github.io" in s.replace("entehagroup.github.io", "") or "entehagroup.github.io" in s:
            problems.append(f"{pth}: old github.io address")
    for f in ("sitemap.xml", "robots.txt", "llms.txt"):
        if "github.io" in open(os.path.join(ROOT, f), encoding="utf-8").read(): problems.append(f"{f}: old github.io address")
    if problems:
        print("\n".join(problems)); sys.exit(1)


if __name__ == "__main__":
    os.makedirs(os.path.join(ROOT, "assets"), exist_ok=True)
    shutil.copy(os.path.join(SRC, "site.css"), os.path.join(ROOT, "assets", "site.css"))
    shutil.copy(os.path.join(SRC, "site.js"), os.path.join(ROOT, "assets", "site.js"))
    build_og_images()
    for L in LANGS:
        build_home(L); build_services(L); build_projects_index(L); build_about(L)
        for s in SERVICES: build_service(s, L)
        for i, p in enumerate(PROJECTS): build_project(p, i, L)
    build_extras()
    check()
    print(f"built {len(PAGES)} pages")
