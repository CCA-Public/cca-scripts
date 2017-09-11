#!/bin/bash

# get input
echo "Absolute path of source directory: "
read input_dir
echo "Bag identifer: "
read input_id
echo "Versement: "
read input_versement
echo "Your name: "
read input_name

# copy files to home dir for processing, excluding .DS_Stores and Thumbs.dbs
rsync -av --stats --exclude=".DS_Store*" --exclude="Thumbs.db" $input_dir/ /Users/twalsh/$input_id/

# create bag
bagit.py --processes 4 --internal-sender-identifier="$input_id" --internal-sender-description="$input_versement" --contact-name="$input_name" --source-organization='Canadian Centre for Architecture' /Users/twalsh/$input_id

# change bag permissions recursively
find /Users/twalsh/$input_id -type d -exec chmod 755 {} \;
find /Users/twalsh/$input_id -type f -exec chmod 644 {} \;

# validate bag
bagit.py --validate --processes 4 /Users/twalsh/$input_id

# send bag to /mnt/incoming - change user and IP address prior to using!
if rsync -ave ssh /Users/twalsh/$input_id/ user@xxx.xxx.xxx.xxx:/mnt/incoming/$input_id/ ; then
	echo "Bag copied successfully to /mnt/incoming"
	rm -rf /Users/twalsh/$input_id # delete copy from home dir
else
	echo "Rsync failed"
fi
