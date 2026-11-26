#!/usr/bin/env python3
"""news-image-20261125 entrypoint: place the poster at /output/entry.png.

The poster itself (entry.png, 1024x1024) was drawn programmatically during
the build session and ships in this repository; this program only copies it
to the directory the harness reads.
"""

import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    src = os.path.join(HERE, "entry.png")
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    if os.path.getsize(dst) != os.path.getsize(src):
        raise SystemExit("copy incomplete: size mismatch")
    print(f"wrote {dst} ({os.path.getsize(dst)} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
