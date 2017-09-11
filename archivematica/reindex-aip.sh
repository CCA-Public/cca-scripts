#!/bin/bash
export DJANGO_SETTINGS_MODULE=settings.common
python /home/twalsh/archivematica-devtools/tools/rebuild-elasticsearch-aip-index-from-files /mnt/dark_archive/aips --uuid "$1"
