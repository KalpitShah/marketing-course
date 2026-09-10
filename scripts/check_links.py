#!/usr/bin/env python3
"""Check every URL and local image reference in the program's markdown files.

Usage:
    python3 scripts/check_links.py marketing-program [--timeout 20] [--workers 8]

Exit code is 1 if any link fails. Needs normal outbound internet access.
Only the standard library is used.
"""
from __future__ import annotations

import argparse
import concurrent.futures as cf
import os
import re
import sys
import urllib.error
import urllib.request

URL_RE = re.compile(r"https?://[^\s<>()\"'\]]+")
LOCAL_IMG_RE = re.compile(r"!\[[^\]]*\]\((?!https?://)([^)\s]+)\)")
UA = "Mozilla/5.0 (compatible; marketing-program-link-check/1.0)"


def collect(root: str):
    urls: dict[str, set[str]] = {}
    local: list[tuple[str, str]] = []
    for dirpath, _, files in os.walk(root):
        for fn in sorted(files):
            if not fn.endswith(".md"):
                continue
            path = os.path.join(dirpath, fn)
            with open(path, encoding="utf-8") as f:
                text = f.read()
            for u in URL_RE.findall(text):
                u = u.rstrip(".,;:*")
                urls.setdefault(u, set()).add(fn)
            for rel in LOCAL_IMG_RE.findall(text):
                local.append((fn, os.path.normpath(os.path.join(dirpath, rel))))
    return urls, local


def fetch(url: str, timeout: int) -> tuple[str, int | str]:
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "*/*"}, method="GET")
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return url, resp.status
    except urllib.error.HTTPError as e:
        return url, e.code
    except Exception as e:  # noqa: BLE001
        return url, type(e).__name__


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("root")
    ap.add_argument("--timeout", type=int, default=20)
    ap.add_argument("--workers", type=int, default=8)
    args = ap.parse_args()

    urls, local = collect(args.root)
    failures = 0

    for fn, path in local:
        if not os.path.exists(path):
            print(f"MISSING local image  {path}  (in {fn})")
            failures += 1
    print(f"checked {len(local)} local image references")

    print(f"checking {len(urls)} unique URLs ...")
    with cf.ThreadPoolExecutor(max_workers=args.workers) as ex:
        for url, status in ex.map(lambda u: fetch(u, args.timeout), sorted(urls)):
            ok = isinstance(status, int) and status < 400
            # 403 and 429 usually mean bot blocking, not a dead page; flag them separately
            soft = status in (403, 429, 405)
            if ok:
                continue
            tag = "BLOCKED?" if soft else "FAIL"
            print(f"{tag:9} {status!s:>16}  {url}  (in {', '.join(sorted(urls[url]))})")
            if not soft:
                failures += 1
    print(f"done: {failures} hard failure(s)")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
