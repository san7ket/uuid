"""
Created By:
Shubham Vasaikar (vasaikar)
Sanket Jagtap (sjagtap)
"""

import uuid
import os
import sys


newname = sys.argv[1]+".bak"
os.rename(sys.argv[1], newname)
print sys.argv[1]

with open(newname, 'r') as f:
	content = f.readlines()
	
with open(sys.argv[1], 'w') as f1:
	for line in content:
		index = line.find('@id:', 0, len(line))
		if  index != -1:
			uid = uuid.uuid4()
			line = line.split(':')[0]
			line += ": "+str(uid)+"\n"
			f1.write(line)
			
		else:
			f1.write(line)

os.remove(newname)
