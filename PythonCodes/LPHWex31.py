#Excercise 31  Making Decison 

print(""" You enter a dark room two doors. 
Do you go through the door #1 or door #2""")

door = input(">>>")
if door =="1":
    print("There is a giant bear here eating a cheese cake.")
    print("what do you do ?")
    print("1. Take the cake")
    print("2. Scream at the bear.")

    bear = input(">>>")
    if bear == "1":
        print("you the bear eats your face off. Good job!")
    elif bear == "2":
        print("you fought the bear like a brave man ! History will remember you with honour")
    else:
        print(f"""You are a man of commitment. You make your own path ! you Killed the bear.
        tales of your bravery will be told to the upcoming generations.""")

elif door == "2":
    print(""" A gaint ogre stares at you in anger. Choose your weapon
    1. Leviathan Axe : made by the dwarf of middlegard and used by th egod of thunder
    2. Blade of Chaos: You know hell is about to loose break. Be a brave spartan!
    3. Dagger of Time: powered by the sand of time time, you are the master of past, present and future
    
    Choose your weapon wsisely""")
    weapon = input(">>>")
    if weapon =="1":
        print("""with the burst of thuder and the flash of light,
        Ogre will taste wrath of your might """)
    elif weapon == "2":
        print("""Even Hades and Zeus couldn't stood the test of these blades,
        With Bath of blood, in bed of death the ogre gets laid""")
    elif weapon=="3":
        print("""Time tells the fate of the brave,
        Ogre rests peachefully in his grave""")
    else :
        print("You tried to kill ogre with pencil, but you are not Jhon Wick ! ")