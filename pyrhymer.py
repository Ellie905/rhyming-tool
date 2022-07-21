# Project: Rhyming Tool
# Author: Ellie Day
# Date: 07/20/2022

# Purpose: Create a tool that can pull suggested rhymes from a "Dictionary" file to provide writing aid for memory/
#          language impaired

# Resources:
# https://docs.python.org/3/library/argparse.html
# https://ohhla.com/
# https://en.wikipedia.org/wiki/International_Phonetic_Alphabet

import argparse
import easygui
from sortedcontainers import sorteddict
from sortedcontainers import sortedlist


class RhymeDict:
    def __init__(self):
        self.entries: sortedlist(DictEntry)

    def importdict(self):
        path = easygui.fileopenbox(title='Open Dictionary File', filetypes='.dict')
        self.__openfile(path)


    # def exportdict(self):

    # def addtodict(self):

    # def removefromdict(self):


# RhymeDict Individual Entry (RhymeDict = List of Entries):
# Map | (Integer) ID paired to (String) Word
# Dictionary | "ID": ID         (Integer)
#              "Word": Word     (String)
#              "Soft Rhymes":   (List)
#              "Hard Rhymes":   (List)
class DictEntry:
    def __init__(self):
        self.ID = sorteddict('ID', 'Word')
        self.rhymes = sorteddict('ID', 'Word', 'Soft Rhymes', 'Hard Rhymes')



def __main__():
    print('hello world')
    # argparser
    # -h -help
    # -a -add (word to dictionary)
    # -all <word to rhyme with> (select all words in dictionary that rhyme with word, soft or hard rhyme)
    # -e -exit (close program, code 0)
    # -hard <word to rhyme with> (select all hard rhymes in dictionary)
    # -n -new (select new dictionary file)
    # -r -remove (word from dictionary)
    # -s -save (save dictionary)
    # -soft <word to rhyme with> (select all soft rhymes in dictionary)
