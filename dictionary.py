# Project: Rhyming Tool
# Author: Ellie Day
# Date: 07/20/2022

# Purpose: Create a tool that can pull suggested rhymes from a "Dictionary" file to provide writing aid for memory/
#          language impaired

# To-do:
# * Make pyrhymer.py (type word + args -> get rhymes)
# * rewrite saving function

# Resources:
# https://docs.python.org/3/library/argparse.html
# https://pypi.org/project/easygui/
# https://programtalk.com/python-examples/plugins.easygui.fileopenbox/
# https://ohhla.com/
# https://en.wikipedia.org/wiki/International_Phonetic_Alphabet

import argparse
import easygui
import json


# RhymeDict Individual Entry (RhymeDict = List of Entries):
# Dictionary | "ID": ID         (Integer)
#              "Word": Word     (String)
#              "Soft Rhymes":   (List)
#              "Hard Rhymes":   (List)
class DictEntry:
    def __init__(self):
        self.rhymes = {'ID': int, 'Word': str, 'Soft Rhymes': list, 'Hard Rhymes': list}

    def create_entry(self, ID, word, softrhymes, hardrhymes):
        self.rhymes['ID'] = ID
        self.rhymes['Word'] = word
        self.rhymes['Soft Rhymes'] = softrhymes
        self.rhymes['Hard Rhymes'] = hardrhymes

    def get_ID(self):
        return self.rhymes.get('ID')

    def get_word(self):
        return self.rhymes.get('Word')

    def get_soft_rhymes(self):
        return self.rhymes.get('Soft Rhymes')

    def get_hard_rhymes(self):
        return self.rhymes.get('Hard Rhymes')

    def get_all_rhymes(self):
        return self.rhymes.get('Soft Rhymes'), self.rhymes.get('Hard Rhymes')


class RhymeDict:
    def __init__(self):
        self.entries: list[DictEntry] = []

    def importdict(self):
        path = easygui.fileopenbox(title='Open Dictionary File', default="*.dict", filetypes=["*.dict"])
        if path is None:
            return

        # Pass path to readtodict()
        self.readtodict(path)

    # Read file, populate new DictEntry objects and append to self.entries
    def readtodict(self, path):
        with open(path, 'r') as file:
            entry = DictEntry()
            temp = json.load(file)

            data = str(temp[0]).split(',')

            # Used to define new DictEntry object
            id = str(data[0]).lstrip('{')
            id = id.split(':')
            id = id[1].replace('\'', '')
            id = id.lstrip()

            int_id = int(id)

            # Used to define new DictEntry object
            word = str(data[1]).lstrip()
            word = word.split(':')
            word = word[1].replace('\'', '')
            word = word.lstrip()

            str_word = str(word)

            # Used to define new DictEntry object
            srhymes = str(data[2]).lstrip()
            srhymes = srhymes.split(':')
            srhymes = srhymes[1].replace('\'', '')
            srhymes = srhymes.replace(';', ',')
            srhymes = srhymes.replace(' ', '')

            list_srh: list[str] = srhymes.split(',')

            # Used to define new DictEntry object
            hrhymes = str(data[3]).rstrip('}')
            hrhymes = hrhymes.split(':')
            hrhymes = hrhymes[1].replace('\'', '')
            hrhymes = hrhymes.replace(';', ',')
            hrhymes = hrhymes.replace(' ', '')

            list_hrh: list[str] = hrhymes.split(',')

            entry.create_entry(int_id, str_word, list_srh, list_hrh)
            self.entries.append(entry)

    # Export self.entries to file
    def exportdict(self):
        with open('PyrhymerDictionary.dict', 'w') as file:
            for i in self.entries:
                # Serialize individual pieces of data
                ID = i.get_ID()
                Word = i.get_word()
                SoftRhymes: str = ''
                HardRhymes: str = ''

                # Convert List of SoftRhymes to Comma-Separated String
                for x in list(i.get_soft_rhymes()):
                    SoftRhymes = SoftRhymes + x

                # Convert List of HardRhymes to Comma-Separated String
                for x in list(i.get_hard_rhymes()):
                    HardRhymes = HardRhymes + x

                # Convert above data to new Dictionary
                newDict = {'ID': ID, 'Word': Word, 'Soft Rhymes': SoftRhymes, 'Hard Rhymes': HardRhymes}

                # Convert Dictionary to JSON
                json_object = json.dumps(newDict, indent=4)

                file.write(json_object + '\n')

    def addtodict(self, dictentry: DictEntry):
        self.entries.append(dictentry)

    # def removefromdict(self):

    # def create_reverse_entry(self):


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

rhymedict = RhymeDict()

rhymedict.importdict()
# x = DictEntry()
# y = DictEntry()
# x.create_entry(1, 'Word', ['Birth, Door, Wore'], ['Bird, Turd'])
# y.create_entry(2, 'Bird', ['Birth, Door, Wore'], ['Word, Turd'])
# rhymedict.addtodict(x)
# rhymedict.addtodict(y)
# rhymedict.exportdict()
