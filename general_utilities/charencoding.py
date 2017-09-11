#!/usr/bin/python
# -*- coding: utf-8 -*-

# Prints likelihood of character encodings for files/directories in source

import argparse
import chardet
import os  

parser = argparse.ArgumentParser()
parser.add_argument("source", help="Path to folder to check out")
args = parser.parse_args()

for n in os.listdir(args.source):
    print("%s => %s (%s)" % (n, chardet.detect(n)['encoding'], chardet.detect(n)['confidence']))
