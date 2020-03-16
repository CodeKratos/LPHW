#Basically excercise 36--- now I did find out after commiting this as New Game on github
#so before moving to the Lists and other datastructure it will be better to create a game (real reason : its fun)
import time

def bimla():
    print("do you wanna peek ?")
    choice = input(">>>")
    if "peek" in choice or "yes" in choice:
        print("oh fuck ! it the annoying neighbour -------- Aunty ji")
        print("what will you do now bro ? Go back or stay")
        choice = input(">>>")
        if "go back" in choice:
            print("right call buddy")
        elif "stay" in choice:
            print("so you've chosen death")
        exit(0) #function se nikalney ka yahi ek rasta hai
    else:
        print(" abey darta q h dekh na ....")
        bimla()

def suspense(sound): #before using a function it must be defined, earlier I had defined it beneath the call so it threw an error
    print(sound) 
    time.sleep(1) 
    print(sound)
    time.sleep(0.5) 
    print(sound)

def opening():
    print("You are a highschool student, bored at home after the board exams !")
    suspense(".")
    print("You hear some foot steps")
    suspense("tapp")
    print("you hear a knock on the door")
    suspense("Knock")
    print("who it could be ?")
    suspense("?")
    first_choice()

def best_friend():
    print("no bro ! you beated him so hard with Brock Lessner yesterday, he is not going to come anytime soon !")
    bimla()

def crush():
    print("yeah ! like that's ever going to happen. keep on dreaming romeo..")
    bimla()

def that_guy():
    print("Could be ! He did say that he was going to see you ")
    bimla()

def first_choice():    
    print("""who it could possibly be at this time of the day ? what do you think 
        1. Your best friend ? probably asking you to play Smack Down on PS2
        2. Your crush ? asking you to help her with summer assignment
        3. That guy from ? school whom you beated beause he was acting tough in fornt of girls""")

    choice = input(">>>") #here was an indentation error, i just typed an enter afte print ended and it took an extra tab. ~~~New Learning~~~
    if "best friend"  in choice: #deleted or condition 
        best_friend()
    elif "crush"  in choice:
        crush()
    elif "that guy"  in choice:
        that_guy()
    else:
        print("Hmmm.. let me think.. yeah it could be" + choice + "would you like to peek ?")


opening()
"""it is fun to create games but I shal not spend much time on the game only because I have many other tasks todo
and in this endeavour of mastering python a lot is yet to be done
so moving on to the next excercise
but dont worry, someday we will make a full fledge game ;) see i just used a terminator in python"""


