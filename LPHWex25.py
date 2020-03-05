"""
Output is not being printed on this code. lets mark it and move forward to the controlls

"""

#ends on page 113
#this function will break stuff
print('Enter a sentence, it will be broken')
stuff = input('>>>')

def break_word(stuff):
    print("In function break_word")
    words = stuff.split(' ') # spliting the string whereever a whitespace is encountered
    #print('words:', words[0])
    for i in words:
        print(i)
    return words
#sorting the word using sorted
def sorty_word(words):
    print("In function sorty_word")
    swords = sorted(words)
    for i in swords:
        print(i)
    return sorted(swords)
#printing the first word only
def first_word(words):
    print("in function first_word")
    word = words.pop(0)
    #print(word)
    for i in word:
        print(i)
#printng the last word only
def last_word(words):
    print("in function last_word")
    lastWord = words.pop(-1)
    print(lastWord)
#taking in a full sentence and returning the sorted word

def sort_sentence(sentence):
    print("in function sort_sentence")
    word = break_word(sentence)
    return sorted(word)
#printing first and lst words of a sentence
def print_first_and_last(sentence):
    print("In function print_first_and_last")
    words = break_word(sentence)
    first_word(words) 
    last_word(words)
def first_and_last_sorted(sentence):
    print("In function first_and_last_sorted") #
    words = sort_sentence(sentence)
    first_word(words)
    last_word(words)

#dont waste too much time on one segment, seek help from Internet or share the file with a friend to get the file.

#lets practice controls...........
"""
Marking end of the half book. 
Its been quite a journey. Silicon vally is still far. Hustle hard. happy for us both.
"""