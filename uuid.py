#!/bin/python
"""
Created By:
Shubham Vasaikar (vasaikar)
Sanket Jagtap (sjagtap)
"""

import uuid
import os
import sys
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("-f", "--filename", help="filepath")
args = parser.parse_args()
newname = args.filename +".bak"
os.rename(args.filename, newname)
print args.filename

with open(newname, 'r') as f:
	content = f.readlines()

with open(args.filename, 'w') as f1:
	for line in content:
		index = line.find('@id:', 0, len(line))
		if  index != -1 and len(line) < 20:
			uid = uuid.uuid4()
			line = line.split(':')[0]
			line += ": "+str(uid)+"\n"
			f1.write(line)
			
		else:
			f1.write(line)

os.remove(newname)
