#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Go through files in source directory and copy
to either "AP184-FTK" or "AP184-DIP" depending
on where basename is in list.

Python3

Tim Walsh 2017
MIT License
"""

import argparse
import os
import shutil

# create list of disks that should go to 'AP184-FTK'
disks_to_ftk = ['ARCH268232', 'ARCH268233', 'ARCH268234', 'ARCH268235', 
'ARCH268236', 'ARCH268238', 'ARCH268239', 'ARCH268240', 'ARCH268241', 
'ARCH268242', 'ARCH268243', 'ARCH268244', 'ARCH268245', 'ARCH268247', 
'ARCH268249', 'ARCH268250', 'ARCH268251', 'ARCH268255', 'ARCH268256', 
'ARCH268257', 'ARCH268258', 'ARCH268259', 'ARCH268260', 'ARCH268261', 
'ARCH268262', 'ARCH268263', 'ARCH268266', 'ARCH268268', 'ARCH268269', 
'ARCH268270', 'ARCH268271', 'ARCH268274', 'ARCH268277', 'ARCH268285', 
'ARCH268286', 'ARCH268287', 'ARCH268288', 'ARCH268289', 'ARCH268292', 
'ARCH268293', 'ARCH268294', 'ARCH268295', 'ARCH268299', 'ARCH268300', 
'ARCH268302', 'ARCH268303', 'ARCH268305', 'ARCH268306', 'ARCH268307', 
'ARCH268308']

# parse arguments
parser = argparse.ArgumentParser()
parser.add_argument("source", help="Directory containing source disk images")
parser.add_argument("destination", help="New directory for separated copies")
args = parser.parse_args()

# create destination directories
destination = os.path.abspath(args.destination)
ftk_dir = os.path.join(destination, 'AP184-FTK')
dip_dir = os.path.join(destination, 'AP184-DIP')

for newdir in destination, ftk_dir, dip_dir:
	os.mkdir(newdir)

for f in os.listdir(args.source):
	disk_id = os.path.basename(f)[:10]
	if disk_id in disks_to_ftk:
		shutil.copy2(os.path.join(args.source, f), ftk_dir)
		print(f, "copied to FTK dir")
	else:
		shutil.copy2(os.path.join(args.source, f), dip_dir)
		print(f, "copied to DIP dir")