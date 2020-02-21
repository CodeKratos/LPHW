#from(keyword) sys(library) import(keyword to import) argvs(module for arguments unpacking)
from sys import argv
script, filename = argv #unpacking the arguments
txt = open(filename)

print(f"your filename is {filename} ")
print(txt.read())

print("type the filename again:")
file_again = input(">>>>>>>")
txt_again = open(file_again)
print(txt_again.read())

txt.close(filename)
txt_again.close(file_again)