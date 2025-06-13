#!/usr/bin/python
#Usage: dupe.py "/folder/to/scan/for/duplicates" <options>
#Options: -d (delete duplicate files)
import sys
import os
bytes = filenames = []
x = d = delete = fd = 0
darg = 'null'
try:
    darg = str(sys.argv[2])
except IndexError:
    darg = 'null'
if darg == "-d":
    print ("OPTIONS: -d (deletion) is enabled")
    delete = 1
    print ("")
for root, dirs, files in os.walk(str(sys.argv[1])):
    for file in files:
        p = os.path.join(root,file)
        currfile = os.path.abspath(p)
        filesize = os.path.getsize(currfile)
        if filesize in bytes:
            print ("%s - Duplicate > Matching: %s" % (file, filenames[bytes.index(filesize)]))
            d += 1
            if delete == 1:
                os.remove(currfile)
                print ("ACTION: Removed %s" % (file))
        else:
            bytes.append(filesize)
            filenames.append(file)
        x += 1
print ("")
if delete == 1:
    print ("DONE: Scanned %s file(s) and deleted %s duplicate(s)" % (x, d))
else:
    print ("DONE: Scanned %s file(s) and found %s duplicate(s)" % (x, d))