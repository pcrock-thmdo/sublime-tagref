#!/usr/bin/env bash
set -Eeuo pipefail

output_zip="${1}"

panic() {
    echo "FATAL: ${*}" >&2
    exit 1
}

test ! -f "${output_zip}" || panic "already exists: ${output_zip}"
git ls-files --cached --modified | xargs zip --recurse-paths "${output_zip}"
