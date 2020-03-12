#Brenches an dfunction
from sys import exit
def gold_room():
    print("this room is full of gold take as uch as you want")
    choice = input(">>>")
    if choice == 0 or choice == 1:
        how_much = int(choice)     
    else:
        dead("man learn to type a number")
    if how_much < 50:
        print("danm nibba ! you are satisfied with life")
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
        if choice  == "take the honey":
            dead("dude come on ! bears dont share honey. you are dead now")
        elif   choice == "taunt bear" and not bear_moved:
            print("the bear moves and you an go through it")
            print("go through it !")
            
        elif  choice == "taunt bear" and bear_moved:
            dead(" don't fight bears bro you dead nibba ")
        elif choice == "open door" and bear_moved:
            gold_room()
        else: 
            print("I got no idea what that means")

def juju_room():
    print(" you have came to the place of El Juju ")
    print("juju gets angry and runs towards you")
    print("run for your life or eat your head?")
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
        dead("Took too much time to decide")

start()