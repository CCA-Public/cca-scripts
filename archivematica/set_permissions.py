#!/usr/bin/env python

from __future__ import print_function, unicode_literals

import grp
import os
import pwd
import sys

def main(transfer_path):
	"""
	Reset owner and group for files and folders in transfer
	to archivematica
	"""
	uid = pwd.getpwnam("archivematica").pw_uid
	gid = grp.getgrnam("archivematica").gr_gid
	os.chown(transfer_path, uid, gid)

if __name__ == '__main__':
	transfer_path = sys.argv[1]
	main(transfer_path)