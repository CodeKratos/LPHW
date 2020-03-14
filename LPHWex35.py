#Brenches an dfunction
from sys import exit
def gold_room():
    print("this room is full of gold take as much as you want")
    choice = input(">>>")
    if  "0" in choice or  "1" in choice:
        how_much = int(choice)     
    else:
        dead("man learn to type a number")
    if how_much < 50:
        print("danm nibba ! you are satisfied with life. May you find a loving, caring and cherishing wife who does not posts bikini pics on instagram")
    else:
        dead("Greed is not good")
def bear_room():
    print("there is a bear in front of you")
    print("bear has some honey")
    print("bear is in fornt of a door")
    print("how are you going to move the bear")
    while True:
        choice  = input(">>>")
        bear_moved = True
        if  "take the honey" in choice:
            dead("dude come on ! bears dont share honey. you are dead now")
        elif "taunt bear" in choice and not bear_moved:
            print("the bear moves and you an go through it")
            print("go through it !")
            
        elif "taunt bear" in choice and bear_moved:
            dead(" don't fight bears bro you dead nibba ")
        elif "open door" in choice and bear_moved:
            gold_room()
        else: 
            print("I got no idea what that means")

def juju_room():
    print(" you have came to the place of El Juju ")
    print("juju gets angry and runs towards you")
    print("run for your life or eat your head?") #statements asks for 'run' but choice accepts 'flee'
    choice = input(">>>")
    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("juju aint no joke nibba")
    else:
        juju_room()

def dead(why):
    print(why, "good job !")
    exit(0)

def start():
    print("you are in a drak room")
    print(" there is a door to your right and left,choose one")
    choice = input(">>>")
    if "left" in choice:
        bear_room()
    elif  "right" in choice:
        juju_room()
    else:
        dead("either walk left or right, learn to decide")

start()