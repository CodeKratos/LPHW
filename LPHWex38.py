ten_things = "Coke Fallakka Acid DMT Meth Cocain Weed"
print("there are not ten things in the list. lest add some")
stuff = ten_things.split(' ')
more_stuff = ['Money', 'Power','Politics','Control','Religion','War','Slavery','Tobacco']

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Adding",next_one)
    stuff.append(next_one)
    print(f"lenght of the stuff is {len(stuff)}")

print("stuff in stuff", stuff)
print("let's do some thing with stuff")
print("at firts index",stuff[1])
print('at negative first index',stuff[-1])
print(stuff.pop())
print(" ".join(stuff))
print("#".join(stuff[3:5]))