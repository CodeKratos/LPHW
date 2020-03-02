# Page 97 Excercise Strings, Bytes and Character Encoding

import sys #importig system
script, encoding, error = sys.argv #getting arguments

def main(language_file, encoding, errors): # 2. defining main function readline() returns one line from language_file
    line = language_file.readline()  #3.

    if line:                                    #4. no specific condition 
        print_line(line, encoding, errors)       #5.           #calling print_line with custom parameters line, encodin and error
        return main(language_file, encoding, errors)

def print_line(line, encoding, errors):  # 6. function being executed
    next_lang = line.strip()            #7. removes all the spaces form the line
    raw_bytes = next_lang.encode(encoding, errors = errors) #8. 
    cooked_string = raw_bytes.decode(encoding, errors = errors)

    print(raw_bytes, "<====>", cooked_string)

language = open("language.txt", encoding ='utf-8')
main(language, encoding, error ) # 1. called main function with parameters that were passed during th ecode run