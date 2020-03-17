#dictionaries
#creating a mapping of the state to abbreviation
from operator import itemgetter
states = {
    'Uttar Pradesh' : 'UP',
    'Madhye Pradesh': 'MP',
    'Andhra Pradesh': 'AP',
    'Uttarakhand': 'UK',
    'Mizoram':'MI'
}
#cretae some basic set of states and some cities in them
cities ={
    'UP': 'Kanpur',
    'MP': 'Bhopal',
    'MI': 'Aizawal'
}
#adding some more cities : alternate way
cities['AP'] ='Amarvati'
cities['UK']='Dehradun' 

#priniting out some cities
print('~'*20)
print('UP has :',cities['UP'])
print('Mizoram has :',cities['MI'])

#printing out some abbriviation
print('__'*10)
print('Madhye Pradesh\'s abbriviation is : ', states['Madhye Pradesh'])
print('Uttarakhand\'s abbreviation is :', states["Uttarakhand"])

#pasisng the abbriviatoion from cities to states
print('++++'*5)
print("MP has",cities[states['Madhye Pradesh']])
print('Mizoram has: ', cities[states['Mizoram']])

#print every state's abbreviation
print('#####'*4)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")
    print(f" and it has a beautiful city called {cities[abbrev]}") # working in this loop then why not working in the loop below

#doing same for cities
print("%%%%%%%"*3)
for abbrev, cities in list(cities.items()):
    print(f" {cities} is in {abbrev}")

#now doing both at the same time
print('---'*40)
for st, ab in list(states.items()):
    #print(f"and	has	city	{cities[abbrev]}") need a little help on this one from internet
    print(f"{st} is abbreviated as {ab}")
    #print(f" and it has a beautiful city called {cities[ab]}") again not working
    #ab = abbrev
    #print(f" {state[ab]}") not working
     
print("--"*10)
#safely get abbreviation of a state that might not be there
state = states.get('Texas')
if not state:
    print("sorry no Texas   ")

#get a city with a default value
if 'TX' in cities:
    print("Indian texas is called Uttar Pradesh")
else:
    print("India does not has Texas but UP is quite similar")

#city = cities.get('TX','Does not exists')
#print(f"The city for the state 'TX' is : {city}")

def getList(cities):
    return list(cities)
    #print(" f", list(cities)) should print this return data in some other function 
