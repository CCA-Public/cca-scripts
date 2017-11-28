#!/bin/bash
export DJANGO_SETTINGS_MODULE=settings.common
cd <path>/archivematica-devtools/tools
/usr/share/python/archivematica-dashboard/bin/python rebuild-elasticsearch-aip-index-from-files <path to aipstore> --uuid "$1"
