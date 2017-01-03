#!/usr/bin/env python

import json
import os
import sys
import urllib2

def main(transfer_path):
    object_id = os.path.basename(os.path.normpath(transfer_path))
    data = json.load(urllib2.urlopen("http://api.tms.cca.qc.ca/API/Object/" + object_id))

    # save object metadata
    title = data["tmsApiObject"]["ObjectTitle"].encode('utf-8')
    if title is None:
        title = ''
    
    description = data["tmsApiObject"]["Description"]
    if description is None:
        description = ''
    else:
        description = description.encode('utf-8')

    date_begin = data["tmsApiObject"]["DateBegin"].encode('utf-8')
    date_end = data["tmsApiObject"]["DateEnd"].encode('utf-8')

    if date_begin == date_end:
        date = date_begin
    else:
        date = "%s/%s" % (date_begin, date_end)

    creator_list = [item["DisplayName"] for item in data["tmsApiConstituentDetails"] if item["Role"] == "archive creator"]
    if creator_list:
        creator = creator_list[0].encode('utf-8')
    else:
        creator = ''
   
    parent_id_list = [item["Relationship"]["Relation1Object"]["ObjectNumber"] for item in data["tmsApiRelationships"] if item["Relationship"]["Relation1"] == "Est inclus dans"]
    if parent_id_list:
        parent_id = parent_id_list[0].encode('utf-8')
    else:
        parent_id = ''
    
    accession_list = [item["Relationship"]["Relation1Object"]["ObjectNumber"] for item in data["tmsApiRelationships"] if item["Relationship"]["Relation1"] == "Provient de"]
    if accession_list:
        accession = accession_list[0].encode('utf-8')
    else:
        accession = ''

    if data["tmsApiAltNumbers"][0] is None:
        fonds_number = ''
    else:
        fonds_number_list = [item["AltNum1"] for item in data["tmsApiAltNumbers"] if item["Description"] == "fonds number"]
        if fonds_number_list:
            fonds_number = fonds_number_list[0].encode('utf-8')
        else:
            fonds_number = ''

    # write object metadata to metadata.json
    metadata = [
        {
            'parts': 'objects',
            'dc.title': title,
            'dc.description': description,
            'dc.creator': creator,
            'dc.publisher': "Centre Canadien d'Architecture",
            'dc.date': date,
            'dc.identifier': object_id,
            'dc.source': accession,
            'dcterms.isPartOf': fonds_number,
            'dc.coverage': parent_id
        }
    ]

    # create metadata dir if doesn't already exist
    metadata_path = os.path.join(transfer_path, 'metadata')
    if not os.path.exists(metadata_path):
        os.makedirs(metadata_path)
    
    # dump json into metadata.json file
    json_path = os.path.join(metadata_path, 'metadata.json')
    with open(json_path, 'w') as f:
        json.dump(metadata, f)

    return 0

if __name__ == '__main__':
    transfer_path = sys.argv[1]
    sys.exit(main(transfer_path))
