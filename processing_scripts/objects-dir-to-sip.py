#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Script for turning a bunch of directories structured as:

<target_dir>
   objects
       <files>

or

<target_dir>
    objects
       diskimage
           <files>
       files
           <files>

into Archivematica-ready SIPs with accompanying submissionDocumentation,
hashes, and archival description.

Python3

Tim Walsh 2017
MIT License
"""

import argparse
import csv
import itertools
import math
import os
import shutil
import subprocess
import sys

#import Objects.py from python dfxml tools
sys.path.append('/usr/share/dfxml/python')
import Objects

def convert_size(size):
    # convert size to human-readable form
    if size == 0:
        return '0 bytes'
    size_name = ("bytes", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size,1024)))
    p = math.pow(1024,i)
    s = round(size/p)
    s = str(s)
    s = s.replace('.0', '')
    return '%s %s' % (s,size_name[i])

def create_sip(target_dir, filesdir):
    """
    Create complete SIP from target with only objects dir
    """
        
    # set paths and create dirs
    object_dir = os.path.join(target_dir, 'objects')
    metadata_dir = os.path.join(target_dir, 'metadata')
    subdoc_dir = os.path.join(metadata_dir, 'submissionDocumentation')
    
    for newfolder in metadata_dir, subdoc_dir:
        os.makedirs(newfolder)

    # write brunnhilde and dfxml reports to submissionDocumentation
    if filesdir == True:
        files = os.path.abspath(os.path.join(object_dir, 'files'))
        subprocess.call("brunnhilde.py -zw '%s' '%s' brunnhilde" % (files, subdoc_dir), shell=True)
        subprocess.call("cd '%s' && python3 /usr/share/dfxml/python/walk_to_dfxml.py > '%s'" % (files, os.path.join(subdoc_dir, 'dfxml.xml')), shell=True)
    else:
        subprocess.call("brunnhilde.py -zw '%s' '%s' brunnhilde" % (object_dir, subdoc_dir), shell=True)
        subprocess.call("cd '%s' && python3 /usr/share/dfxml/python/walk_to_dfxml.py > '%s'" % (object_dir, os.path.join(subdoc_dir, 'dfxml.xml')), shell=True)

    # write checksums
    subprocess.call("cd '%s' && md5deep -rl ../objects > checksum.md5" % metadata_dir, shell=True)

def write_to_spreadsheet(target_dir, spreadsheet_path):
    """
    Write line about current SIP to description CSV.
    """

    # open description spreadsheet
    spreadsheet = open(spreadsheet_path, 'a')
    writer = csv.writer(spreadsheet, quoting=csv.QUOTE_NONNUMERIC)

    # intialize values
    number_files = 0
    total_bytes = 0
    mtimes = []

    # parse dfxml file
    dfxml_file = os.path.abspath(os.path.join(target_dir, 'metadata', 'submissionDocumentation', 'dfxml.xml'))

    # gather info for each FileObject
    for (event, obj) in Objects.iterparse(dfxml_file):
        
        # only work on FileObjects
        if not isinstance(obj, Objects.FileObject):
            continue
        
        # gather info
        number_files += 1

        mtime = obj.mtime
        if not mtime:
            mtime = ''
        mtime = str(mtime)
        mtimes.append(mtime)
        
        total_bytes += obj.filesize

    # build extent statement
    size_readable = convert_size(total_bytes)
    if number_files == 1:
        extent = "1 digital file (%s)" % size_readable
    elif number_files == 0:
        extent = "EMPTY"
    else:
        extent = "%d digital files (%s)" % (number_files, size_readable)

    # build date statement TODO: utilize all MAC dates, not just modified
    if mtimes:
        date_earliest = min(mtimes)[:10]
        date_latest = max(mtimes)[:10]
    else:
        date_earliest = 'N/A'
        date_latest = 'N/A'
    if date_earliest[:4] == date_latest[:4]:
        date_statement = '%s' % date_earliest[:4]
    else:
        date_statement = '%s - %s' % (date_earliest[:4], date_latest[:4])

    # gather info from brunnhilde & write scope and content note
    if extent == 'EMPTY':
        scopecontent = ''
    else:
        fileformats = []
        fileformat_csv = os.path.join(target_dir, 'metadata', 'submissionDocumentation', 'brunnhilde', 'csv_reports', 'formats.csv')
        with open(fileformat_csv, 'r') as f:
            reader = csv.reader(f)
            next(reader)
            for row in itertools.islice(reader, 5):
                fileformats.append(row[0])
        fileformats = [element or 'Unidentified' for element in fileformats] # replace empty elements with 'Unidentified'
        formatlist = ', '.join(fileformats) # format list of top file formats as human-readable
        
        # create scope and content note
        scopecontent = 'Complete contents of CD-R %s. File includes an .iso disk image of the dual-formatted ISO-9660/HFS disk and digital files exported from the disk image using FTK Imager. Most common file formats: %s' % (os.path.basename(target_dir), formatlist)
    # write csv row
    writer.writerow(['', os.path.basename(target_dir), '', '', date_statement, date_earliest, date_latest, 'File', extent, 
        scopecontent, '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''])

    # close spreadsheet
    spreadsheet.close()



## MAIN FLOW

# parse arguments
parser = argparse.ArgumentParser()
parser.add_argument("sips_dir", help="Directory containing dirs to turn into SIPs")
parser.add_argument("destination", help="Destination dir for spreadsheet")
parser.add_argument("-f", "--filesdir", help="Use if SIP contains both diskimage and files directories", action="store_true")
args = parser.parse_args()

sips_dir = os.path.abspath(args.sips_dir)

# create sips
for target in sorted(os.listdir(sips_dir)):
    create_sip(os.path.join(sips_dir, target), args.filesdir)

# make description spreadsheet
spreadsheet_path = os.path.join(os.path.abspath(args.destination), 'description.csv')
spreadsheet = open(spreadsheet_path, 'w')
writer = csv.writer(spreadsheet, quoting=csv.QUOTE_NONNUMERIC)
header_list = ['Parent ID', 'Identifier', 'Title', 'Archive Creator', 'Date expression', 'Date start', 'Date end', 
                'Level of description', 'Extent and medium', 'Scope and content', 'Arrangement (optional)', 'Accession number', 
                'Appraisal, destruction, and scheduling information (optional)', 'Name access points (optional)', 
                'Geographic access points (optional)', 'Conditions governing access (optional)', 'Conditions governing reproduction (optional)', 
                'Language of material (optional)', 'Physical characteristics & technical requirements affecting use (optional)', 
                'Finding aids (optional)', 'Related units of description (optional)', 'Archival history (optional)', 
                'Immediate source of acquisition or transfer (optional)', "Archivists' note (optional)", 'General note (optional)', 
                'Description status']
writer.writerow(header_list)
spreadsheet.close()

# populate description spreadsheet
for sip in sorted(os.listdir(sips_dir)):
    write_to_spreadsheet(os.path.join(sips_dir, sip), spreadsheet_path)