#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("destination", help="Path to destination for new directory")
parser.add_argument("dir_name", help="Name of directory to create")
args = parser.parse_args()

dest = os.path.abspath(args.destination)

# paths for dirs to make
target = os.path.join(dest, args.dir_name)
objects = os.path.join(target, 'objects')
metadata = os.path.join(target, 'metadata')
subdoc = os.path.join(metadata, subdoc)

# make dirs
for directory in target, objects, metadata, subdoc:
	if not os.path.isdir(directory):
		os.makedirs(directory)
