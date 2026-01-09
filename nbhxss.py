#!/usr/bin/env python3
"""
NBHXSS - Advanced XSS Hunting Framework
Author: NBH-BD
Version: 2.1.0
"""

import argparse
import sys
import subprocess
import os

def update_tool():
    print("[*] Checking for updates...")

    if not os.path.isdir(".git"):
        print("[!] Git repository not found.")
        print("[!] Please install NBHXSS using git clone to enable auto-update.")
        return

    try:
        subprocess.run(["git", "pull"], check=True)
        print("[+] NBHXSS updated successfully!")
    except subprocess.CalledProcessError:
        print("[!] Update failed. Please update manually.")


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

        parser.add_argument(
        "--update",
        action="store_true",
        help="Update NBHXSS to the latest version"
    )

    args = parser.parse_args()
    if args.update:
        update_tool()
        sys.exit(0)


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



