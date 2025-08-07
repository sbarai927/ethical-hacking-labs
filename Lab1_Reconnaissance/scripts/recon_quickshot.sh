#!/usr/bin/env bash
set -euo pipefail

# recon_quickshot.sh
# Quick passive + light active recon for a domain or IP.
# Usage:
#   ./recon_quickshot.sh example.com
#   ./recon_quickshot.sh 10.6.6.23
#
# Outputs under: Scripts/outputs/<target>/<YYYYmmdd_HHMMSS>/
#
# Requires: bash, dig, whois, nslookup, nmap (dnsrecon & shodan optional)

target="${1:-}"
if [[ -z "$target" ]]; then
  echo "Usage: $0 <domain-or-ip>"
  exit 1
fi

# Resolve repo root (run from anywhere)
ROOT="$(git rev-parse --show-toplevel 2>/dev/null || echo "$(pwd)")"
OUTDIR="$ROOT/Lab1_Reconnaissance/Scripts/outputs/${target}/$(date +%Y%m%d_%H%M%S)"
mkdir -p "$OUTDIR/scans" "$OUTDIR/dns" "$OUTDIR/http" "$OUTDIR/notes"

log() { printf "[%s] %s\n" "$(date +%H:%M:%S)" "$*"; }

# Helper to check deps
need() {
  command -v "$1" >/dev/null 2>&1 || { echo "Missing dependency: $1"; exit 1; }
}

need dig
need whois
need nslookup
need nmap

log "Target: $target"
echo "$target" > "$OUTDIR/target.txt"

############################################
# PASSIVE / DNS
############################################
log "DNS: A/AAAA/MX/TXT/NS/SOA/CAA via dig @8.8.8.8"
for rr in A AAAA MX TXT NS SOA CAA; do
  dig "$target" @"8.8.8.8" "$rr" +noall +answer > "$OUTDIR/dns/${rr}.txt" 2>&1 || true
done

log "DNS: brute basics (www,dev,stage,mail,vpn,test) if domain-like"
if [[ "$target" =~ [a-zA-Z] && "$target" == *.* ]]; then
  wordlist=(www dev stage mail vpn test admin beta api app intranet portal)
  : > "$OUTDIR/dns/subs_basic.txt"
  for sub in "${wordlist[@]}"; do
    fqdn="${sub}.${target}"
    if dig +short "$fqdn" @"8.8.8.8" > /dev/null; then
      ip=$(dig +short "$fqdn" @"8.8.8.8" | tr '\n' ' ')
      printf "%-25s => %s\n" "$fqdn" "$ip" | tee -a "$OUTDIR/dns/subs_basic.txt"
    fi
  done
fi

log "WHOIS (if domain)"
if [[ "$target" =~ [a-zA-Z] && "$target" == *.* ]]; then
  whois "$target" > "$OUTDIR/dns/whois.txt" 2>&1 || true
fi

log "Reverse DNS (if IP)"
if [[ "$target" =~ ^([0-9]{1,3}\.){3}[0-9]{1,3}$ ]]; then
  dig -x "$target" +noall +answer > "$OUTDIR/dns/reverse_dns.txt" 2>&1 || true
fi

# Optional tools
if command -v dnsrecon >/dev/null 2>&1 && [[ "$target" == *.* ]]; then
  log "dnsrecon brute (short) – optional"
  dnsrecon -d "$target" -t brt -D /usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt \
    > "$OUTDIR/dns/dnsrecon_brt.txt" 2>&1 || true
fi

############################################
# ACTIVE / NMAP (safe defaults)
############################################
log "Nmap top-1000 TCP (-sT -sV -sC) – this may take a bit"
sudo true >/dev/null 2>&1 || { echo "You may be prompted for sudo for OS/service scripts"; }
nmap -sT -T4 --top-ports 1000 -sV -sC "$target" -oN "$OUTDIR/scans/nmap_top1k.txt" -oX "$OUTDIR/scans/nmap_top1k.xml" || true

log "Nmap quick UDP top-100 (non-intrusive)"
nmap -sU --top-ports 100 -T3 "$target" -oN "$OUTDIR/scans/nmap_udp_top100.txt" || true

# Conditional SMB/FTP checks if the ports look open
open_tcp=$(awk '/^[0-9]+\/tcp/ && /open/{print $1}' "$OUTDIR/scans/nmap_top1k.txt" | cut -d/ -f1 || true)

has_port() { echo "$open_tcp" | tr ' ' '\n' | grep -qx "$1"; }

if has_port 21; then
  log "FTP anon check (nmap script)"
  nmap -p21 --script ftp-anon "$target" -oN "$OUTDIR/scans/nmap_ftp_anon.txt" || true
fi

if has_port 139 || has_port 445; then
  log "SMB enum (nmap NSE)"
  nmap -p139,445 --script smb-enum-shares,smb-enum-users "$target" -oN "$OUTDIR/scans/nmap_smb_enum.txt" || true
fi

############################################
# MINI MARKDOWN REPORT
############################################
REPORT="$OUTDIR/notes/REPORT.md"
log "Writing mini report → $REPORT"
cat > "$REPORT" <<MD
# Quick Recon Report – $target

**Timestamp:** $(date -Iseconds)  
**Output dir:** \`$OUTDIR\`

## DNS Summary
- A/AAAA/MX/TXT/NS/SOA/CAA: see \`dns/*.txt\`
- Subdomain probe: \`dns/subs_basic.txt\`

## WHOIS / PTR
- WHOIS: \`dns/whois.txt\`
- rDNS: \`dns/reverse_dns.txt\`

## Nmap
- TCP top1k (-sC -sV): \`scans/nmap_top1k.txt\`
- UDP top100: \`scans/nmap_udp_top100.txt\`
- Conditional:
  - FTP anon: \`scans/nmap_ftp_anon.txt\`
  - SMB enum: \`scans/nmap_smb_enum.txt\`

## Next Steps
- Validate high‑value services from TCP scan.
- If web service present, move to Nikto/ZAP (Lab 2).
- Add screenshots to \`Screenshots/\` and link here.

MD

log "Done. Outputs in: $OUTDIR"
