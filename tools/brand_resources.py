"""Copy GregRobin.com resource pages into the PA site with light Productivity Advisors branding.

Usage: python3 -I brand_resources.py <source_repo_dir> <site_dir>
Re-run any time a source page changes. To add a resource: add a row to PAGES (or
call brand(...) with your own file), then add a card to RESOURCES in index.html.
"""
import re, sys, pathlib

SRC, SITE = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])

PAGES = [  # (source file, output name, title)
    ("blueprinting.html", "blueprinting.html", "The Blueprinting Process"),
    ("revops.html", "revops-foundations.html", "RevOps Foundations for Emerging Teams"),
    ("cpq-deck.html", "cpq-discovery.html", "CPQ Discovery to Build"),
]

BAR = """<!-- Productivity Advisors brand bar (hidden when the page is shown inside the site's viewer) -->
<style>
html.pa-framed .pa-bar{display:none}
html:not(.pa-framed) body{padding-top:0!important}
.pa-bar{width:100vw;margin-left:calc(50% - 50vw);background:#FFFFFF;font-family:"Google Sans","Product Sans",-apple-system,"Segoe UI",sans-serif;position:relative;z-index:5;margin-bottom:24px}
.pa-bar .pa-stripe{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));height:3px}
.pa-bar .pa-row{display:flex;align-items:center;gap:12px;padding:10px max(16px,env(safe-area-inset-right,0px)) 10px max(16px,env(safe-area-inset-left,0px));border-bottom:1px solid #ECEDE8}
.pa-bar a{color:#3B3B3D;text-decoration:none;font-size:14px;line-height:1.2}
.pa-bar .pa-home{display:flex;align-items:center;gap:10px;font-weight:500}
.pa-bar .pa-home img{height:24px;width:auto;display:block}
.pa-bar .pa-home b{color:#5D8A25;font-weight:600}
.pa-bar .pa-back{margin-left:auto;font-size:13px;color:#55574F;border:1px solid #E6E7E1;border-radius:20px;padding:6px 14px}
.pa-bar .pa-back:hover{border-color:#A9C584;color:#3F6118}
.pa-bar a:focus-visible{outline:2px solid #5D8A25;outline-offset:2px;border-radius:6px}
</style>
<script>if(window.self!==window.top)document.documentElement.classList.add('pa-framed');</script>
<div class="pa-bar"><div class="pa-stripe" aria-hidden="true"><span style="background:#5D8A25"></span><span style="background:#CA4F2E"></span><span style="background:#3B3B3D"></span><span style="background:#D4B42B"></span></div>
<div class="pa-row"><a class="pa-home" href="../index.html"><img src="../assets/pa-wordmark.png" alt="Productivity Advisors"></a><a class="pa-back" href="../index.html#resources">All resources</a></div></div>
"""

HEAD_EXTRA = '<link rel="icon" type="image/png" sizes="32x32" href="../assets/favicon-32.png">\n<meta name="author" content="Productivity Advisors">\n'


def brand(html: str, title: str) -> str:
    html = re.sub(r'<meta name="author"[^>]*>\s*', "", html)
    html = re.sub(r"<title>.*?</title>", f"<title>{title} · Productivity Advisors</title>", html, count=1, flags=re.S)
    html = html.replace("Greg Robin · greg@productivityadvisors.com · Productivity Advisors",
                        "Productivity Advisors · productivityadvisors.com")
    html = re.sub(r"Greg Robin · ", "Productivity Advisors · ", html)
    if not re.match(r"\s*<!doctype", html, re.I):  # fragments published as artifacts have no document shell
        html = ('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
                '<meta name="viewport" content="width=device-width, initial-scale=1">\n' + html)
    html = html.replace("</title>", "</title>\n" + HEAD_EXTRA, 1)
    m = re.search(r"<body[^>]*>", html)
    if m:
        return html[: m.end()] + "\n" + BAR + html[m.end():]
    m = re.search(r"<main\b", html)
    return html[: m.start()] + BAR + html[m.start():]


for src, out, title in PAGES:
    text = (SRC / src).read_text(encoding="utf-8")
    (SITE / "resources" / out).write_text(brand(text, title), encoding="utf-8")
    print("wrote", out)
