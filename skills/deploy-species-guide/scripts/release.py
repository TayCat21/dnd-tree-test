"""Prepare content-addressed browser assets or verify the live release."""
import argparse
import hashlib
from pathlib import Path
import re
from urllib.request import Request, urlopen

SITE = Path(__file__).resolve().parents[3] / "species-guide"
LIVE = "https://ty-oustrich.github.io/dnd-tree-test/species-guide/"
SOURCES = ("styles.css", "data.js", "model.js", "app.js")


def digest(data):
    return hashlib.sha256(data).hexdigest()[:20]


def prepare():
    page = SITE / "index.html"
    html = page.read_text()
    release_dir = SITE / "releases"
    release_dir.mkdir(exist_ok=True)
    for name in SOURCES:
        source = SITE / name
        content = source.read_bytes()
        target = f"releases/{source.stem}.{digest(content)}{source.suffix}"
        pattern = r'((?:href|src)=")[^"\s]*' + re.escape(source.stem) + r'(?:\.[a-f0-9]+)?' + re.escape(source.suffix) + r'(?:\?[^"\s]*)?(\")'
        html, count = re.subn(pattern, lambda m: m[1] + target + m[2], html)
        if count != 1:
            raise ValueError(f"Expected one entrypoint reference for {name}; found {count}")
        (SITE / target).write_bytes(content)
    html = re.sub(r'<meta name="release" content="[a-f0-9]+">\n?', '', html)
    if 'http-equiv="Cache-Control"' not in html:
        html = html.replace('</head>', '<meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate">\n</head>')
    release = digest(html.encode())
    html = html.replace('</head>', f'<meta name="release" content="{release}">\n</head>')
    page.write_text(html)
    print(f"Prepared release {release}")
    print(f"{LIVE}?release={release}")


def fetch(url):
    request = Request(url, headers={"Cache-Control": "no-cache", "Pragma": "no-cache"})
    with urlopen(request, timeout=30) as response:
        return response.read()


def verify():
    expected = (SITE / "index.html").read_bytes()
    html = expected.decode()
    release = re.search(r'<meta name="release" content="([a-f0-9]+)">', html)[1]
    url = f"{LIVE}?release={release}"
    if fetch(url) != expected:
        raise ValueError("Live HTML does not match this release yet")
    assets = re.findall(r'(?:href|src)="(releases/[^"?]+)"', html)
    if len(assets) != len(SOURCES):
        raise ValueError("Release asset references are incomplete")
    for asset in assets:
        expected_asset = (SITE / asset).read_bytes()
        if fetch(f"{LIVE}{asset}?release={release}") != expected_asset:
            raise ValueError(f"Live asset does not match: {asset}")
    print(f"PASS: live HTML and all {len(assets)} release assets match local bytes")
    print(url)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=("prepare", "verify"))
    args = parser.parse_args()
    {"prepare": prepare, "verify": verify}[args.action]()
