from sys import argv
script  = argv

print("Enter the file name on which you want to perform operations")

filename = input('>>>>')
print(f"we are going to erase {filename}. ")
print("if you do not want that hit CTLR-C (^C).")
print("If you want that hit ENTER")

input("?")

print(f"opening the file {filename}")
target = open(filename,'w')

print("truncrating the file, say goodbye to yourfriend HA HA HA HA Goodbye! Adios! Sayonaraaaa!")
target.truncate()

print('you have to write the name of your 3 favourite movies')
movie1 = input("Movie 1:")
movie2 = input("Movie 2:")
movie3 = input("Movie 3:")

print("I am going to write that in the file.")
target.write(movie1)
target.write("\n")
target.write(movie2)
target.write("\n")
target.write(movie3)
target.write("\n")

print("thank you ! closing your file")
target.close()