from sys import argv
from os.path import exists
script, from_file, to_file = argv

print(f"copying data of {from_file} to {to_file}")

#attempt to open file and copy data in one line
infiledata = open(from_file).read()

outfiledata = open(to_file,'w+').write(infiledata) #also done in one line 


print("task done")

from_file.close()
to_file.close()