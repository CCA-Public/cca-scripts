#!/usr/bin/env python

"""
Adds file extension based on MIME type
Useful for files without extensions (e.g. from HFS disks)

Requirements:
brew install libmagic
sudo pip install python-magic
(https://github.com/ahupp/python-magic)

Tim Walsh
February 2017

"""
import magic
import mimetypes
import os
import sys

def rename_on_mime(filename):
    mime = magic.from_file(filename, mime=True)
    ext = mimetypes.guess_extension(mime, strict=False)
    if ext is None:
        print filename + " - no extension found"
    else:
        filename_ext = filename + ext
        print filename_ext
        os.rename(filename, filename_ext)

walk_dir = sys.argv[1]

for root, directories, filenames in os.walk(walk_dir):
    for filename in filenames:
        p = os.path.abspath(os.path.join(root, filename))
        rename_on_mime(p)
