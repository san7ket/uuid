"""
CreatedBy:
Sanket Jagtap
Abhijeet Kasurde
"""
#!/bin/python

import uuid
import fileinput, sys
import re


filenm = sys.argv[1]
print sys.argv[1]
for line in fileinput.input([filenm], inplace=True):
	uid = str(uuid.uuid4())
	line = re.sub(r'^@id:\s*(.*)$', '@id: ' + uid, line)
	#ine = line.replace("@id:", "@id: "+uid)
	sys.stdout.write(line)
