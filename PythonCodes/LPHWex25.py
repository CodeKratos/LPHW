#this function will break stuff
print('Enter a sentence, it will be broken')
stuff = input('>>>')

def break_word(stuff):
    words = stuff.split(' ') # spliting the string whereever a whitespace is encountered
    #print('words:', words[0])
    return words
#sorting the word using sorted
def sorty_word(words):
    print('word:', words)
    return sorted(words)
#printing the first word only
def first_word(words):
    word = words.pop(0)
    print(word)
#printng the last word only
def last_word(words):
    lastWord = words.pop(-1)
    print(lastWord)
#taking in a full sentence and returning the sorted word
break_word(stuff)
sentence = input('>>>')
def sort_sentence(sentence):
    word = break_word(sentence)
    return sorted(word)
#printing first and lst words of a sentence
def print_first_and_last(sentence):
    words = break_word(sentence)
    first_word(words)
    last_word(words)
def first_and_last_sorted(sentence):
    words = sort_sentence(sentence)
    first_word(words)
    last_word(words)


