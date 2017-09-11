#!/usr/bin/env bash
cd "$1"
for f in *; do
    if [ -d ${f} ]; then
        # Will not run if no directories are available
        bagit.py --validate --fast $f
    fi
done