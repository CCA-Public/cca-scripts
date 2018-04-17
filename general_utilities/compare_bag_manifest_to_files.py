#!/usr/bin/env python

"""
Compare BagIt manifest vs. payload
Pass path to manifest as argument
"""

import os
import re
import sys

manifest = os.path.abspath(sys.argv[1])
data = os.path.join(os.path.dirname(manifest), 'data')

# create list of all filepaths in manifest
filepaths_manifest = list()
with open(manifest, 'r') as f:
	for line in f:
		path = line.split("  ", 1)[1] # ONLY SPLIT ON THE FIRST SPACE!
		path = path.replace("\n", "")
		filepaths_manifest.append(path)

# create list of all filepaths in data
filepaths_data = list()
for root, dirs, files in os.walk(data):
	for f in files:
		path_abs = os.path.join(root, f)
		path = re.sub(r'.*data', 'data', path_abs)
		filepaths_data.append(path)

# compare lists
only_in_manifest = list(set(filepaths_manifest) - set(filepaths_data))
only_in_payload = list(set(filepaths_data) - set(filepaths_manifest))

# print results
print("Files in manifest but not in payload")
print("---")
if not only_in_manifest:
	print("n/a")
for f in only_in_manifest:
	print(f)
print("\n")
print("Files in payload but not in manifest")
print("---")
if not only_in_payload:
	print("n/a")
for f in only_in_payload:
	print(f)