#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import os
import shutil

# parse arguments
parser = argparse.ArgumentParser()
parser.add_argument("source", help="Directory containing disk images and related files")
args = parser.parse_args()

source = os.path.abspath(args.source)

# find split ISO images in source directory
for target in sorted(os.listdir(source)):
	if target.endswith(".iso01"):
		# record file basename
		basename = os.path.splitext(target)[0]
		# create list for split file parts and add .iso, .iso01
		split_iso_parts = []
		split_iso_parts.append(os.path.join(source, basename + '.iso'))
		split_iso_parts.append(os.path.join(source, target))
		# check for further parts
		for n in range(2, 10):
			file_to_test = os.path.join(source, basename + '.iso0' + str(n))
			# if part exists, add to list
			if os.path.isfile(file_to_test):
				split_iso_parts.append(file_to_test)
		# move split ISO image parts to new dir
		split_parts_dir = os.path.join(source, basename + '_split')
		os.mkdir(split_parts_dir)
		for split_part in split_iso_parts:
			shutil.move(split_part, split_parts_dir)
		# concatenate parts and write whole ISO to source dir
		with open(os.path.join(source, basename + '.iso'), 'w') as outfile:
			for filepart in sorted(os.listdir(split_parts_dir)):
				with open(os.path.join(split_parts_dir, filepart), 'rb') as infile:
					shutil.copyfileobj(infile, outfile, 1024*1024*10)
		
