#!/usr/bin/env bash
cd "$1"
for f in *; do
    if [ -d ${f} ]; then
        # Will not run if no directories are available
        bagit.py --validate --processes 4 $f
    fi
done