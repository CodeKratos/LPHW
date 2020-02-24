# in this excersise : copying data from one file to other file

from sys import argv
from os.path import exists
script = argv
print("enter the source file, from which data has to be taken")
from_file = input('>>>')
print("Enter the destination file name, to which data has to be copied")
to_file =  input('>>>')

print(f"copying data of {from_file} to {to_file}")

#attempt to open file and copy data in one line
infiledata = open(from_file).read()

outfiledata = open(to_file,'w+').write(infiledata) #also done in one line 


print("task done")


