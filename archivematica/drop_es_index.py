#!/usr/bin/env python

import sys
sys.path.append("/home/demo/archivematica/src/archivematicaCommon/lib/externals")
from pyes import *
conn = ES('xxx.xx.xx.xx:9200')

try:
    conn.delete_index('aips')
except:
    print("Error deleting index or index already deleted.")