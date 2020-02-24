# Name, Varialbe, Code & Function

"""this one is like script with argv
multiple argumnets can be entered
but only the defined number of arguments will go in the function 
"""
def print_two(*args):
    arg1, arg2 = args #to check if we define 3 argumnts in this one
    print(f"Character 1 : {arg1} Character 2 : {arg2} \n\n")

#passing two arguments in paranthesis, we can just do this
def print_three(arg1, arg2, arg3):
    print(f"Character 1 : {arg1} Character 2 : {arg2} Character 3 : {arg3}\n\n")

#this fucntion just takes one argument
def print_one(arg1):
    print(f"Character 1 : {arg1}\n\n ")

#this one takes no argumnets
def print_with_no_args():
    print("Hope is a good thing Red, and like anyother good it never dies.")

print_one("Red")
print_two("Rick","Morty")
print_three("Red","Andy","Rita Hayworth")

#so basically what I learned in this is how to assign functions and pass argumnets in the 