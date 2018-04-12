#!/usr/bin/env python

import json
import os
import sys
import urllib2

def main(transfer_path):
    dirname = os.path.basename(os.path.normpath(transfer_path))
    object_id = dirname.split('---')[0]
    object_id = object_id.replace('_', ':') # replace underscores with colons (e.g. for DR numbers)
    data = json.load(urllib2.urlopen("http://api.tms.cca.qc.ca/API/Object/" + object_id))

    # create dict for Dublin Core descriptive metadata
    dc_metadata = dict()
    dc_metadata['parts'] = 'objects'
    dc_metadata['dc.publisher'] = "Centre Canadien d'Architecture"
    dc_metadata['dc.identifier'] = object_id

    # save object metadata to dict
    title = data["tmsApiObject"]["ObjectTitle"].encode('utf-8')
    if not title is None:
        dc_metadata['dc.title'] = title
    
    description = data["tmsApiObject"]["Description"]
    if not description is None:
        description = description.encode('utf-8')
        dc_metadata['dc.description'] = description

    dcformat_list = [item["TextEntry1"] for item in data["tmsApiTextEntries"] if item["TextType"]["TextType1"] == "Collation"]
    if dcformat_list:
        dcformat = dcformat_list[0].encode('utf-8')
        dc_metadata['dc.format'] = dcformat

    date_begin = data["tmsApiObject"]["DateBegin"].encode('utf-8')
    date_end = data["tmsApiObject"]["DateEnd"].encode('utf-8')
    if date_begin == date_end:
        date = date_begin
    else:
        date = "%s/%s" % (date_begin, date_end)
    if not date is None:
        dc_metadata['dc.date'] = date

    creator_list = [item["DisplayName"] for item in data["tmsApiConstituentDetails"] if item["Role"] == "archive creator"]
    if creator_list:
        creator = creator_list[0].encode('utf-8')
        dc_metadata['dc.creator'] = creator
    
    accession_list = [item["Relationship"]["Relation1Object"]["ObjectNumber"] for item in data["tmsApiRelationships"] if item["Relationship"]["Relation1"] == "Provient de"]
    if accession_list:
        accession = accession_list[0].encode('utf-8')
        dc_metadata['dc.source'] = accession

    if not data["tmsApiAltNumbers"][0] is None:
        fonds_number_list = [item["AltNum1"] for item in data["tmsApiAltNumbers"] if item["Description"] == "fonds number"]
        if fonds_number_list:
            fonds_number = fonds_number_list[0].encode('utf-8')
            dc_metadata['dcterms.isPartOf'] = fonds_number

    # create metadata dir if doesn't already exist
    metadata_path = os.path.join(transfer_path, 'metadata')
    if not os.path.exists(metadata_path):
        os.makedirs(metadata_path)
    
    # dump metadata into metadata.json file
    json_path = os.path.join(metadata_path, 'metadata.json')
    metadata = [dc_metadata]
    with open(json_path, 'w') as f:
        json.dump(metadata, f)

    return 0


if __name__ == '__main__':
    transfer_path = sys.argv[1]
    sys.exit(main(transfer_path))
