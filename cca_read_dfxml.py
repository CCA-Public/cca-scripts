#!/usr/bin/python
# make readable txt report of dates for fileobjects in a dfxml file
# script must be run from /usr/share/dfxml/python

import argparse
import Objects
import sys

def _make_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--allocated", help="Process allocated files only", 
        action="store_true")
    parser.add_argument("dfxml", help="DFXML file to read")
    parser.add_argument("txt", help="txt file to create")

    return parser

def main():

    parser = _make_parser()
    args = parser.parse_args()

    txt = open(args.txt, 'w')
    
    num_files = int()
    num_files == 0
    mtimes = []
    crtimes = []
    atimes = []

    # gather info for each FileObject
    for (event, obj) in Objects.iterparse( args.dfxml ):
        #Only work on FileObjects
        if not isinstance(obj, Objects.FileObject):
            continue
        
        #If allocated argument passed, skip unallocated files
        if args.allocated == True:
            if obj.alloc == 0:
                continue
        
        # gather info
        num_files += 1

        mtime = obj.mtime
        if not mtime:
            mtime = ''
        mtime = str(mtime)
        mtimes.append(mtime)

        crtime = obj.crtime
        if not crtime:
            crtime = ''
        crtime = str(crtime)
        crtimes.append(crtime)

        atime = obj.atime
        if not atime:
            atime = ''
        atime = str(atime)
        atimes.append(atime)

        fname = obj.filename
        fsize = obj.filesize
        fsize = str(fsize)
        alloc = obj.alloc # 1 = allocated file

        txt.write('\n\n---File---')
        txt.write('\nFile name: ' + fname)
        txt.write('\nFile size (bytes): ' + fsize)
        if alloc == 1:
            txt.write('\nAllocated file: Yes')
        elif alloc == 0:
            txt.write('\nAllocated file: No')
        elif alloc is None:
            txt.write('\nAllocated file: n/a')
        txt.write('\nModified date: ' + mtime)
        txt.write('\nAccessed date: ' + atime)
        txt.write('\nCreated date: ' + crtime)

    # txt.write aggregate info
    txt.write('\n\n---OVERALL STATS---')
    
    txt.write('\nNumber of files: ' + str(num_files))
    
    mtimes_first = min(mtimes)
    if mtimes_first == '':
        mtimes_first = 'undated'
    mtimes_last = max(mtimes)
    if mtimes_last == '':
        mtimes_last = 'undated'
    if mtimes_first == mtimes_last:
        mtimes_range = "%s" % str(mtimes_first)
    else:
        mtimes_range = "%s - %s" % (str(mtimes_first), str(mtimes_last))
    txt.write('\nDate range (modified): ' + mtimes_range)
    
    atimes_first = min(atimes)
    if atimes_first == '':
        atimes_first = 'undated'
    atimes_last = max(atimes)
    if atimes_last == '':
        atimes_last = 'undated'
    if atimes_first == atimes_last:
        atimes_range = "%s" % str(atimes_first)
    else:
        atimes_range = "%s - %s" % (str(atimes_first), str(atimes_last))
    txt.write('\nDate range (accessed): ' + atimes_range)
    
    crtimes_first = min(crtimes)
    if crtimes_first == '':
        crtimes_first = 'undated'
    crtimes_last = max(crtimes)
    if crtimes_last == '':
        crtimes_last = 'undated'
    if crtimes_first == crtimes_last:
        crtimes_range = "%s" % str(crtimes_first)
    else:
        crtimes_range = "%s - %s" % (str(crtimes_first), str(crtimes_last))
    txt.write('\nDate range (created): ' + crtimes_range)

    txt.close()

if __name__ == "__main__":
    main()
