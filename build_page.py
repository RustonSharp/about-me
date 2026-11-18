"""Build the static site into _site/ (the only directory deployed to GitHub Pages)."""

import shutil
from pathlib import Path

ROOT = Path(__file__).parent
OUT = ROOT / "_site"


def main():
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir()

    shutil.copyfile(ROOT / "templates" / "template.html", OUT / "index.html")
    shutil.copytree(ROOT / "assets", OUT / "assets")
    print(f"Site built in {OUT}")


if __name__ == "__main__":
    main()
