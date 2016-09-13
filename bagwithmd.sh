#!/bin/bash

# get input
echo "Package to bag: "
read input_dir
echo "Bag identifer: "
read input_id
echo "Versement: "
read input_versement
echo "Your name: "
read input_name

# create bag
bagit.py --processes 4 --internal-sender-identifier="$input_id" --internal-sender-description="$input_versement" --contact-name="$input_name" --source-organization='Canadian Centre for Architecture' $input_dir

# validate bag
bagit.py --validate --processes 4 $input_dir

# change bag permissions recursively
find $input_dir -type d -exec chmod 755 {} \;
find $input_dir -type f -exec chmod 644 {} \;

echo "Process complete."