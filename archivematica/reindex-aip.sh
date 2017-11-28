#!/bin/bash
export DJANGO_SETTINGS_MODULE=settings.common
python /home/<user>/archivematica-devtools/tools/rebuild-elasticsearch-aip-index-from-files <path to aipstore> --uuid "$1"
