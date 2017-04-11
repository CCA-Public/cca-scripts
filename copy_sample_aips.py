#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import os
import shutil

aips_to_copy = ['AR2012_0034_raw-9414d2f1-c42f-416f-8a6c-3f9b5df6789f.7z', 'AR2012_0065_raw-2ea36919-d5b6-41be-b586-4244d8236583.7z', 
'AR2013_0027_raw-701a3f87-6252-4aff-9891-093fe145b94d.7z', 'AR2013_0045_raw-8d0730b0-e30e-435f-ad32-d04141a17747.7z', 
'AR2013_0079_raw-3fa8c365-da5d-4e9e-bb2a-477a16227344.7z', 'AR2014_0074_raw-a4616a9b-b98e-4c61-aa30-0f59b2e10785.7z', 
'AR2015_0028_raw-3a4d4a1d-be21-406d-9c56-4e560d2714c3.7z', 'AR2015_0112_raw-38ddd634-f5ca-49c6-a3b5-105d89c91a51.7z', 
'AR2015_0114_raw-030f4519-0dac-490f-ad08-c46fbe6c53b8.7z', 'AR2016_0003_raw-014bdbbd-4110-49b5-8b52-b259d8c11a7c.7z', 
'AR2016_0008_raw-7c28a43b-6a8d-432e-9e57-9300f38ec5ca.7z', 'DR2008_0016_543_raw-1514e8e0-8041-47b5-91dd-c1daf09e1b95.7z', 
'AP154.S1.1973.PR01.SS2.026---AR2007.0102-4afb2c94-7a61-4ab7-a2ef-f07b714e1d87.7z', 'AP174.S1.1999.D1.001-6160ea5a-ac85-4f61-bf1e-7ba23650c072.7z', 
'AP174.S1.2001.D1.001-34e72944-5cfe-4b23-8662-335f831e1b35.7z', 'AP174.S1.2001.D1.002-c98b5637-7604-4694-b855-debaf84adef2.7z', 
'AP174.S1.2001.D1.003-d0d17e4e-005d-4cdb-b6c9-e0f17dc1b2cd.7z', 'AP174.S1.2001.D1.004-e7a2015d-0b1d-47e5-aa25-3a3c65f705ce.7z', 
'AP174.S1.2001.D1.005-749101d6-2492-484e-b7bc-e1b5d50ab74d.7z', 'AP174.S1.2001.D1.006-994c9b87-d7c3-486e-9eea-e165bfc7c909.7z', 
'AP174.S1.2001.D1.007-77317c58-5c6e-4fb1-a814-c77c92a22cac.7z', 'AP174.S1.2001.D1.008-3354d44e-789d-4a42-b7b8-d8c744a27c87.7z', 
'AP174.S1.2001.D1.009-3df1dc41-ffec-4873-b6bf-3cfb9b9adc27.7z', 'AP174.S1.2001.D1.010-e8d9056c-cf9a-499e-b85d-add5e3114aab.7z', 
'ARCH275092---AR2013.0052-1a9f269c-f344-43ed-bf15-b4d673c36974.7z', 'ARCH269334---AR2013.0052-80730505-a986-49f6-8aad-d272f99183ac.7z', 
'ARCH274546---AR2013.0052-7afd06d2-abfb-4310-a173-d4fd920f425f.7z', 'ARCH274548---AR2013.0052-c2fb3cdc-e5f4-4b6d-bb97-99e11b85bfb6.7z', 
'ARCH274552---AR2013.0052-99ed5a00-91ce-4a29-b3fe-0b4e077e236a.7z', 'ARCH274547---AR2013.0052-13c3fd7a-9a44-4378-a4db-11b39b2ef4f7.7z', 
'ARCH274666---AR2013.0052-4354f11e-41ca-4734-b5bc-3e5d9265dd47.7z', 'ARCH274672---AR2013.0052-ee3cd7fe-ab16-48b3-bb83-a5554f76d21d.7z', 
'ARCH274882---AR2013.0052-7ef511a6-80b4-4f5c-a3a3-1ababd2f179c.7z', 'ARCH274879---AR2013.0052-cb8e60cf-0783-48a9-bb4c-b1538672c79d.7z', 
'ARCH274888---AR2013.0052-ebd682e5-7f44-45e2-ad1e-c4d517fbbc4e.7z', 'ARCH275297---AR2013.0052-2e0dcff9-66a9-4a9a-9632-988cc9eefbbd.7z', 
'ARCH276308---AR2013.0052-d6736dd3-a085-425d-80cc-7a3701d8f469.7z', 'CD033.04-5d4e14c6-87da-40a3-bdcd-c5e1bd9088fa.7z', 
'CD033.05-1f5fef5c-7132-4fb9-bbb6-a6d158478c56.7z', 'CD033.06-c271081f-e2d8-443e-aa7f-011ffc779594.7z', 
'ARCH276283---AR2013.0052-066eb9a6-8e85-4914-bda1-6faf69925b65.7z', 'ARCH276230---AR2013.0052-2fbf93bb-8fd9-4f3a-87c9-70d20b3ffd5e.7z', 
'ARCH276204---AR2013.0052-7f7163af-88e6-4662-be95-5f2105f556bb.7z', 'ARCH275969---AR2013.0052-09fff3fb-f98e-4684-8d20-d78d5dcddc2a.7z', 
'ARCH275973---AR2013.0052-f63e9f6d-e719-48f7-b2c0-f57003b35141.7z', 'ARCH275977---AR2013.0052-93b35675-ec37-46a8-87b6-eb2d1a16a846.7z', 
'ARCH275989---AR2013.0052-b1ad21ef-43b7-43d0-aed8-d9495e31c6b3.7z', 'ARCH275998---AR2013.0052-299136d7-4085-45ab-a364-21b8d3b508f2.7z', 
'ARCH276002---AR2013.0052-fe89e22f-45f8-4fe7-ba4e-227eb692858a.7z']

# parse args
parser = argparse.ArgumentParser()
parser.add_argument("source", help="Root dir of where to find AIPs")
parser.add_argument("destination", help="Where to send AIPs")
args = parser.parse_args()

for root, dirs, filenames in os.walk(args.source):
	for filename in filenames:
		if os.path.basename(filename) in aips_to_copy:
			print("Copying file: %s" % (os.path.join(root, filename)))
			shutil.copy(os.path.join(root, filename), args.destination)