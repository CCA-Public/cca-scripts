#!/usr/bin/python

import subprocess

# Reindex Archival Storage index using only select AIPs

aip_list = [] # Add each UUID to add to index as string in this list

for aip in aip_list:
    index_command = "sudo /home/twalsh/reindex-aip.sh %s" % aip
    subprocess.call(index_command, shell=True)
