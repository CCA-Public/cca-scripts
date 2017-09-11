#!/bin/bash
echo "Path of directory to bag: "
read input_dir
echo "Bag identifer: "
read input_id
echo "Versement: "
read input_versement
echo "Your name: "
read input_name

echo "Files identified for deletion pre-bagging: "

#find thumbs.db and .DS_Store files
find $input_dir -name '.DS_Store'
find $input_dir -name '._.DS_Store'
find $input_dir -name 'Thumbs.db'

#check if okay
echo "Proceed?"
select yn in "Yes" "No"; do
	case $yn in
		Yes ) break;;
		No ) exit;;
	esac
done

#delete thumbs.db and .DS_Store files
find $input_dir -name '.DS_Store' -delete
find $input_dir - name '._.DS_Store' -delete
find $input_dir -name 'Thumbs.db' -delete

# create bag
bagit.py --processes 4 --internal-sender-identifier="$input_id" --internal-sender-description="$input_versement" --contact-name="$input_name" --source-organization='Canadian Centre for Architecture' $input_dir

# change bag permissions recursively
find $input_dir -type d -exec chmod 755 {} \;
find $input_dir -type f -exec chmod 644 {} \;

# validate bag
bagit.py --validate --processes 4 $input_dir
