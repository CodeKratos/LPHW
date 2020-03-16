#dictionaries
#creating a mapping of the state to abbreviation
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

#doing same for cities
print("%%%%%%%"*3)
for abbrev, cities in list(cities.items()):
    print(f" {cities} is in {abbrev}")

#now doing both at the same time
print('---'*40)
for state, abbrev in list(states.items()):
    #print(f"and	has	city	{cities[abbrev]}") need a little help on this one from internet
    print(f"{state} is abbreviated as {abbrev}")
    #ab = abbrev
    #print(f" {state[ab]}") not working
     
    