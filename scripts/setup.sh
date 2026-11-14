#!/usr/bin/env bash
set -euo pipefail
root="$(cd "$(dirname "$0")/.." && pwd)"
cd "$root"
openclaw --profile weavz-example agents add weavz-example --workspace "$root" --non-interactive
openclaw --profile weavz-example mcp add weavz --url https://platform.weavz.io/mcp/weavz --transport streamable-http
openclaw --profile weavz-example mcp login weavz
openclaw --profile weavz-example mcp doctor weavz --probe
