#!/usr/bin/env python3
"""
NBHXSS - Advanced XSS Hunting Framework
Author: NBH-BD
Version: 2.1.0
"""

import argparse
import sys

BANNER = "NBHXSS v2.1.0 | Author: NBH-BD\nAdvanced XSS Hunting Framework"

# ===== YOUR EXISTING / FUTURE LOGIC GOES HERE =====
def scan_url(url):
    print(f"[+] Scanning URL: {url}")
    # XSS logic here


def scan_list(file):
    with open(file, "r") as f:
        for line in f:
            scan_url(line.strip())


# ===== CLI ENTRY POINT =====
def main():
    parser = argparse.ArgumentParser(
        description="Advanced XSS Hunting Framework for Bug Bounty & Authorized Testing",
        formatter_class=argparse.RawTextHelpFormatter
    )

    parser.add_argument("-u", "--url", help="Target URL to scan")
    parser.add_argument("-l", "--list", help="File containing URLs")
    parser.add_argument("--skip-static", action="store_true", help="Skip static files")
    parser.add_argument("--threads", type=int, default=10, help="Threads (default: 10)")
    parser.add_argument("--headless", action="store_true", help="Enable headless browser")

    args = parser.parse_args()

    print(BANNER)

    if not args.url and not args.list:
        parser.print_help()
        sys.exit(0)

    if args.url:
        scan_url(args.url)

    if args.list:
        scan_list(args.list)


if __name__ == "__main__":
    main()


