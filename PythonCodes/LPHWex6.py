type_of_people = 10
# format string
x = f"there are {type_of_people} type of people in the world."
binary = "binary"
do_not = "don't"
# string inside string 3 and 4
y = f"those who know {binary} and those who {do_not}"
print(x)
print(y)

# format string inside an print statement
print(f"I said : {x}")  # string inside sring 1
print(f"I also said : {y}")  # string inside a string 2


# format string with boolean

hiralrious = False
joke_evaluation = "Ins't that joke so funny ! {}"
print(joke_evaluation.format(hiralrious))  # string.format(binaryValue)

w = "this part of my life..."
e = "this little part.."
f = "is called Happyness !"
print(w + e + f)  # joining three little part to make complete meaning
