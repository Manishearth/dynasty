"""Print rulebook.html to PDF at several page sizes and report layout problems.

For each size it prints the page count, the pages that end with a heading (a heading
cut off from its text), and the pages that hold only a few lines (stranded fragments).
Needs Microsoft Edge (headless printing) and pdftotext (shipped with Git for Windows).

  python tools/print_check.py                     # letter, a4, a4-wide, letter-tall
  python tools/print_check.py --sizes letter      # just one
  python tools/print_check.py --out C:/tmp/pdfs   # where the PDFs go (default: %TEMP%/rbpdf)

The page size lives in style/rulebook.css (@page). Each size other than letter is
printed from a temporary copy of rulebook.html, next to it so images/ and style/
resolve, with an @page override added after the stylesheets; the copy is deleted
afterwards.
"""
import argparse, html, os, re, subprocess

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
EDGE = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
PDFTOTEXT = r"C:\Program Files\Git\mingw64\bin\pdftotext.exe"
SIZES = {
    "letter": None,                                   # as style/rulebook.css has it
    "a4": "@page{size:A4;margin:12mm 12mm}",
    "a4-wide": "@page{size:A4;margin:25mm 20mm}",
    "letter-tall": "@page{size:letter;margin:10mm 15mm}",
}

def headings(text):
    heads = set()
    for m in re.finditer(r"<(h[234]|caption)[^>]*>(.*?)</\1>", text, re.S):
        t = re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", "", m.group(2)))).strip()
        if t: heads.add(t.upper())
    return heads

def pages_of(pdf):
    out = subprocess.run([PDFTOTEXT, "-layout", pdf, "-"], capture_output=True).stdout.decode("utf-8", "replace")
    return out.split("\f")[:-1]

def check(src, size, outdir, few):
    with open(src, encoding="utf-8") as f:
        text = f.read()
    rule = SIZES[size]
    copy = os.path.join(os.path.dirname(src), f"_print_{size}.html")
    page = text if rule is None else text.replace("</head>", f"<style>@media print{{{rule}}}</style>\n</head>", 1)
    pdf = os.path.join(outdir, f"rulebook_{size}.pdf")
    with open(copy, "w", encoding="utf-8", newline="\n") as f:
        f.write(page)
    try:
        subprocess.run([EDGE, "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
                        "--user-data-dir=" + os.path.join(outdir, "edge-profile"),
                        f"--print-to-pdf={pdf}", "file:///" + copy.replace("\\", "/")],
                       check=True, capture_output=True, timeout=300)
    finally:
        os.remove(copy)
    heads, pages = headings(text), pages_of(pdf)
    print(f"== {size}: {len(pages)} pages ({pdf})")
    for i, p in enumerate(pages, 1):
        lines = [" ".join(l.split()) for l in p.splitlines() if l.strip()]
        if not lines: continue
        last = lines[-1].upper()
        if any(last.endswith(h) or (len(last) > 6 and h.endswith(last)) for h in heads):
            print(f"  page {i}: ends with heading {lines[-1]!r}")
        if len(lines) <= few:
            print(f"  page {i}: only {len(lines)} lines | {lines[0][:60]} ... {lines[-1][:60]}")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--sizes", default=",".join(SIZES))
    ap.add_argument("--out", default=os.path.join(os.environ.get("TEMP", "."), "rbpdf"))
    ap.add_argument("--few", type=int, default=8, help="flag pages with at most this many lines")
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    src = os.path.abspath(os.path.join(ROOT, "rulebook.html"))
    for size in a.sizes.split(","):
        check(src, size, a.out, a.few)

if __name__ == "__main__":
    main()
