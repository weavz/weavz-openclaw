#!/usr/bin/env bash
set -euo pipefail
root="$(cd "$(dirname "$0")/.." && pwd)"
cd "$root"
python3 -m unittest discover -s tests -v
echo "PASS: static setup contract only; this does not prove live OAuth or tool execution."
