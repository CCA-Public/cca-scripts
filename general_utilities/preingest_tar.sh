#!/bin/bash

# get input
echo "Absolute path of source directory: "
read input_dir
echo "Identifer: "
read input_id

# make directories
sudo mkdir /Users/twalsh/$input_id
sudo mkdir /Users/twalsh/$input_id/objects
sudo mkdir /Users/twalsh/$input_id/objects/$input_id
sudo mkdir /Users/twalsh/$input_id/metadata

# change ownership of new dirs
sudo chown -R twalsh /Users/twalsh/$input_id

# copy files to home dir for processing, excluding .DS_Stores and Thumbs.dbs
rsync -av --stats --exclude=".DS_Store*" --exclude="._.DS_Store*" --exclude="Thumbs.db" $input_dir/ /Users/twalsh/$input_id/objects/$input_id

# change bag permissions recursively
find /Users/twalsh/$input_id/ -type d -exec chmod 755 {} \;
find /Users/twalsh/$input_id -type f -exec chmod 644 {} \;

# cd to objects dir and create tar
cd /Users/twalsh/$input_id/objects && tar -cvf $input_id.tar $input_id

# delete tar source directory
sudo rm -rf /Users/twalsh/$input_id/objects/$input_id

# create checksum.md5
cd /Users/twalsh/$input_id/metadata && md5deep -rl ../objects > checksum.md5