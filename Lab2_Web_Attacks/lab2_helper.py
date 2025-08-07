#!/usr/bin/env python3
"""
lab2_helper.py
Automates Lab 2 tasks: web vuln scanning, online brute force, offline password cracking
Author: Your Name
"""

import subprocess
import argparse
import os
import datetime
from colorama import Fore, Style


def run_command(command, output_file=None):
    """Run a shell command and optionally save output to file."""
    try:
        print(f"{Fore.CYAN}[*] Running: {command}{Style.RESET_ALL}")
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if output_file:
            with open(output_file, "w") as f:
                f.write(result.stdout)
        print(result.stdout)
        if result.stderr:
            print(f"{Fore.YELLOW}[!] stderr: {result.stderr}{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}[!] Error running command: {e}{Style.RESET_ALL}")


def nikto_scan(targets_file, output_dir):
    """Run Nikto against all targets in file."""
    os.makedirs(output_dir, exist_ok=True)
    with open(targets_file) as f:
        targets = [line.strip() for line in f if line.strip()]
    for target in targets:
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        outfile = os.path.join(output_dir, f"nikto_{target.replace(':','_')}_{timestamp}.txt")
        run_command(f"nikto -h {target} -output {outfile}")


def online_bruteforce(target_ip, user_list, pass_list, output_dir):
    """Run Hydra, Medusa, and Ncrack SSH brute force."""
    os.makedirs(output_dir, exist_ok=True)
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    # Hydra
    run_command(
        f"hydra -L {user_list} -P {pass_list} ssh://{target_ip}",
        os.path.join(output_dir, f"hydra_{timestamp}.txt")
    )

    # Medusa
    run_command(
        f"medusa -h {target_ip} -U {user_list} -P {pass_list} -M ssh",
        os.path.join(output_dir, f"medusa_{timestamp}.txt")
    )

    # Ncrack
    run_command(
        f"ncrack -p 22 -U {user_list} -P {pass_list} {target_ip}",
        os.path.join(output_dir, f"ncrack_{timestamp}.txt")
    )


def offline_crack(hash_file, wordlist, output_dir):
    """Run Hashcat and John for offline password cracking."""
    os.makedirs(output_dir, exist_ok=True)
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    # Hashcat (MD5 example)
    run_command(
        f"hashcat -m 0 -a 0 {hash_file} {wordlist} --quiet",
        os.path.join(output_dir, f"hashcat_{timestamp}.txt")
    )

    # John
    run_command(
        f"john --wordlist={wordlist} {hash_file}",
        os.path.join(output_dir, f"john_{timestamp}.txt")
    )


def main():
    parser = argparse.ArgumentParser(description="Lab 2 Web Exploitation Helper Script")
    subparsers = parser.add_subparsers(dest="mode", help="Mode of operation")

    # Nikto scan mode
    parser_nikto = subparsers.add_parser("nikto", help="Run Nikto against targets from file")
    parser_nikto.add_argument("targets", help="File containing targets (one per line)")
    parser_nikto.add_argument("output", help="Directory to store Nikto results")

    # Online brute force mode
    parser_online = subparsers.add_parser("online", help="Run online brute force attacks")
    parser_online.add_argument("ip", help="Target IP address")
    parser_online.add_argument("users", help="Username list file")
    parser_online.add_argument("passwords", help="Password list file")
    parser_online.add_argument("output", help="Directory to store brute force results")

    # Offline cracking mode
    parser_offline = subparsers.add_parser("offline", help="Run offline password cracking")
    parser_offline.add_argument("hashes", help="File containing password hashes")
    parser_offline.add_argument("wordlist", help="Wordlist for cracking")
    parser_offline.add_argument("output", help="Directory to store offline cracking results")

    args = parser.parse_args()

    if args.mode == "nikto":
        nikto_scan(args.targets, args.output)
    elif args.mode == "online":
        online_bruteforce(args.ip, args.users, args.passwords, args.output)
    elif args.mode == "offline":
        offline_crack(args.hashes, args.wordlist, args.output)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
