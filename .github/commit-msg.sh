#!/bin/bash

PATTERNS=(
    "solution\((leetcode|hackerrank)\):"
    "(add|update|remove)"
    "(recursive|iterative)"
    "'[^']*'"
)

REGEX=$(IFS=' '; echo "${PATTERNS[*]}")

if [[ ! "$1" =~ ^solution ]]; then
  echo "Commit is not a solution, skipping regex matching..."
  exit 0
fi

echo "Parsing commit: $(cat "$1")"

if ! grep -Eq "$REGEX" "$1"; then
  for part in "${PATTERNS[@]}"; do
    if ! grep -Eq "$part" "$1"; then
      echo "Commit message doesn't match the following expression: ${part#*=}"
    fi
  done
  exit 1
fi
exit 0
