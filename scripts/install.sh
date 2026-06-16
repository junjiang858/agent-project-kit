#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TARGET_DIR="${1:-${CODEX_HOME:-$HOME/.codex}/skills/agent-project-kit}"

mkdir -p "$TARGET_DIR"

copy_file() {
  local src="$1"
  local dest="$2"
  mkdir -p "$(dirname "$dest")"
  cp "$src" "$dest"
}

copy_dir() {
  local src="$1"
  local dest="$2"
  mkdir -p "$dest"
  cp -R "$src"/. "$dest"/
}

copy_file "$ROOT_DIR/SKILL.md" "$TARGET_DIR/SKILL.md"
copy_dir "$ROOT_DIR/agents" "$TARGET_DIR/agents"
copy_dir "$ROOT_DIR/references" "$TARGET_DIR/references"
copy_dir "$ROOT_DIR/templates" "$TARGET_DIR/templates"

printf 'Installed Agent Project Kit to %s\n' "$TARGET_DIR"
printf 'Invoke it with: Use $agent-project-kit ...\n'
