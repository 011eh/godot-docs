#!/usr/bin/env python
"""One-click Markdown docs build pipeline.

Run from the `godot-docs` conda env:

    python markdown_doc_build/build_all.py

Steps:
    1. Sphinx markdown build            -> markdown_docs/*.md (+ scattered img/)
    2. clean_md.py                      -> strip HTML comments & <a id> anchors
    3. migrate_images.py                -> flatten images into markdown_docs/img/
                                           and rewrite every image reference
    4. verify.py                        -> assert 0 broken / 0 stray / 0 orphan

Options:
    --skip-build   reuse the existing markdown_docs/ output (steps 2-4 only)

Everything runs with the SAME interpreter that launched this script, so make
sure it is the `godot-docs` env's python.
"""
import os
import sys
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)          # project root (one level up)
OUT = "markdown_docs"
LOG = os.path.join("markdown_doc_build", "build.log")

PY = sys.executable                    # the env that runs this script

SPHINX_CMD = [
    PY, "-m", "sphinx",
    "-T", "-j", "auto",
    "-b", "markdown",
    "-d", "_build/doctrees",
    "-D", "language=en",
    ".", OUT,
]


def banner(n, total, title):
    print(f"\n{'=' * 60}\n[{n}/{total}] {title}\n{'=' * 60}", flush=True)


def run(cmd, **kw):
    print("$ " + " ".join(cmd), flush=True)
    subprocess.run(cmd, cwd=ROOT, check=True, **kw)


def sphinx_build():
    print(f"Sphinx build -> {OUT}/  (full output: {LOG})", flush=True)
    with open(os.path.join(ROOT, LOG), "w", encoding="utf-8") as log:
        proc = subprocess.run(SPHINX_CMD, cwd=ROOT, stdout=log,
                              stderr=subprocess.STDOUT)
    # surface the tail regardless of outcome
    with open(os.path.join(ROOT, LOG), encoding="utf-8", errors="replace") as f:
        tail = f.read().splitlines()[-3:]
    for line in tail:
        print("  " + line, flush=True)
    if proc.returncode != 0:
        sys.exit(f"Sphinx build FAILED (exit {proc.returncode}); see {LOG}")


def main():
    skip_build = "--skip-build" in sys.argv
    steps = 3 if skip_build else 4
    n = 0

    if not skip_build:
        n += 1
        banner(n, steps, "Sphinx markdown build")
        sphinx_build()
    else:
        print("--skip-build: reusing existing markdown_docs/ output")

    n += 1
    banner(n, steps, "Clean .md (HTML comments + <a id> anchors)")
    run([PY, os.path.join("markdown_doc_build", "clean_md.py")])

    n += 1
    banner(n, steps, "Flatten images -> img/ and rewrite references")
    run([PY, os.path.join("markdown_doc_build", "migrate_images.py")])

    n += 1
    banner(n, steps, "Verify references")
    run([PY, os.path.join("markdown_doc_build", "verify.py")])

    print(f"\n{'=' * 60}\nDONE. Output in {OUT}/\n{'=' * 60}", flush=True)


if __name__ == "__main__":
    main()
