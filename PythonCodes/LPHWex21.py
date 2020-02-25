#page 93 exercise 21 : Function Can Return Something

def add(a,b):
    print(f"adding {a} and {b}")
    return a+b
def sub(a,b):
    print(f"substractig {a} and {b}")
    return a-b
def mul(a,b):
    print(a,b)
    return a*b
def div(a,b):
    print(f"dividing {a} and {b}")
    return a/b

print("now applying the following methods and assigning values to the variables")

age = add(20,5)
height = sub(7,1)
weight = mul(8,10)
iq = div(290,2)

print(f"age : {age}, height : {height}, weight : {weight}, iq : {iq}")

# a puzzle for the extra  credit, type it in anyway
print("here is the puzzle.")

what = add(age, sub(height, mul(weight, div(iq,2))))
print("what has a value", what,"do it here")