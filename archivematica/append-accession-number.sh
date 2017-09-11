#!/bin/bash

# Takes path to target directory as first argument, string (accession number) as second
# Appends ---accession number to end of each immediate subdirectory of target

cd "$1"
for f in *; do
	if [ -d ${f} ]; then
		mv "$f" "$f"---"$2"
	fi
done