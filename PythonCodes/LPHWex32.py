#loops and list page number 131

count = [1,2,3,4,5]
fruits = ['Cherry','Apple','Mangoes','Grapes']
mixed = ['Banana',1,'Potato',2,'Whey',3,'Oats']

#the first kind of for loop goes  through a list
for number in count: # extra space gave an error in this line || Beware of whitespace
     print(f"count {number}")

# same as above
for fruits in fruits:
    print(f"{fruits}")
#now for mixed
for i in mixed:
    print(f"I = {i}")
#we can build a list then allocate elements

elements = []
#then use the range function to do 0 to 5 
for i in range(0,6):
    print(F"adding {i} to the list ")
    elements.append(i)
#now we can print them out too

for i in elements:
    print(f"Element was: {i}")