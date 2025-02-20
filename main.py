#!/usr/bin/env python3
'''
    Rio Hondo College
    CIT 128: Python Programming II
    Student Directed Project
'''
import random
from Rename import Rename

class ScrambleX:
    def __init__(self,name):
        self.name = name
    
    def get_name(self):
        return self.name
    
    def set_name(self,name):
        if not name.isalpha():
            raise ValueError()
        self.name = name

    def is_valid_name(self) -> bool:

        #.isalpha() returns True if all symbols in a string are letters of the alphabet
        if self.name.isalpha() == True:
            return self.name
        else:
            raise ValueError("Please enter a name with English letters only.")
    
    def scramble(self) -> str:

        #turns name into a list of its individual letters and adds the letter 'x'
        name_list = list(self.name + 'x')

        #shuffles the letters in the list

        random.shuffle(name_list)

        scrambled_word = ''.join(name_list)
        #Makes sure the first letter of the name is Capital and that the rest of the letters are lower case
        scrambled_word = scrambled_word[0].upper() + scrambled_word[1:].lower()
        return scrambled_word

def main():
    while True:
        name = input("Welcome to the KH Nobody Name Generator, We have been waiting for you\nNow enter your name:\n")
        scrambled_name = ScrambleX(name)
        try:
            scrambled_name.is_valid_name()
            scrambled_name = scrambled_name.scramble()
            rename_me = Rename(scrambled_name)
            rename_me.ask()
            break
        except ValueError as e:
            print(e)
            anotherTry = input("Wanna start over? (y/n):\n")
            if anotherTry.lower() == 'y':
                continue
            elif anotherTry.lower() == 'n':
                print("see ya later")
                break
            else:
                print("Lets start this over....")
            anotherTry = input("Wanna start over? (y/n):\n")

if __name__ == "__main__":
    main()