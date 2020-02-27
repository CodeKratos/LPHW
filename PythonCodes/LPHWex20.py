 # funcions and files
from sys  import argv
script, input_file = argv # input file being entered at the time of command prompt allocation
def print_all(f): #
    print(f.read())

def rewind(f):
    f.seek(0) #seeks sets the position of the flie back to 0

def print_a_line(line_count,f): #intakes the count of file and prints it
    print(line_count, f.readline()) 

current_file = open(input_file) # open the current file and store the content 
print("first print the whole file :\n ")

print_all(current_file)

print("now let's rewind, kind of like a tape.")

rewind(current_file)
print("lets print three lines")

current_line =1
print_a_line(current_line, current_file)

current_line = current_line+1
print_a_line(current_line, current_file)

current_line = current_line+1
print_a_line(current_line, current_file)

#basically we defined 3 functions for respectively reading the file, going to its begining and print the line.