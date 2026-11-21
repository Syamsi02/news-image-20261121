#!/usr/bin/env python3
"""Entry for the news-image-20261121 bounty.

The repository holds the finished front page as entry.png; this program
copies it to /output/entry.png. Pure standard library, no network, and
the copy is byte for byte identical on every run.
"""

import os
import shutil


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    out = "/output/entry.png"
    os.makedirs(os.path.dirname(out), exist_ok=True)
    shutil.copyfile(src, out)
    print("wrote %s (%d bytes)" % (out, os.path.getsize(out)))


if __name__ == "__main__":
    main()
