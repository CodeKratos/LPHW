#Module, Classes and Objective
#first class example

class Song():
    def __init__(self, lyrics):
        self.lyrics = lyrics
    
    def sing_song(self):
        for line in self.lyrics:
            print(line)
HBD = Song(["""have a fantastic coding session on python 3
"""])

BeatIt = Song(["""They'll tell you better not come around here
dont wanna see your face you better disappear
the fire in their eyes and their words are really clear
so beat it just beat it
"""])

HBD.sing_song()
BeatIt.sing_song()