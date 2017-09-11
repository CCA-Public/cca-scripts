#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Move first 10 SIPs from transfer staging to auto-transfers for ingest.
# Must be run on Archiematica pipeline server with sudo privileges.

import os
import shutil
import sys

transfers = "/mnt/incoming/transfers"

# get alphanumerically sorted list of directories in transfers
current_dirs = [f for f in sorted(os.listdir(transfers)) if os.path.isdir(os.path.join(transfers, f))]

# exempt NOT_READY dir
exempted_dir = "/mnt/incoming/transfers/NOT_READY_FOR_INGEST"
if exempted_dir in current_dirs:
    current_dirs = current_dirs.remove(exempted_dir)

# move 10 SIPs
counter = 0
while counter < 10:
    current_dir = os.path.join(transfers, current_dirs[counter])
    try:
        shutil.move(current_dir, "/mnt/incoming/auto-transfers")
        print("Successfully moved " + current_dir + " to auto-transfers for ingest.")
    except:
        print("ERROR!: Could not move " + current_dir + " to auto-transfers for ingest.")
    counter += 1
