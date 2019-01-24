""" -*- coding: python(3.7.1) -*-
    author: Napasin Hongngern """
""" hangman """

import os
import sys
from random import randint

# declare variables
life = 5
order = randint(0,4)
point = 0
point_max = 0
word = ""
hint = ""
guesses = ""

def get_word_and_hint(category, order): # get a word and hint from file
    category -= 1
    global word
    global hint
    absolute_path = os.path.dirname(os.path.abspath(__file__))
    fullname_1 = absolute_path + "/animal_wordlist.txt"
    fullname_2 = absolute_path + "/food_wordlist.txt"
    fullname_3 = absolute_path + "/meme_wordlist.txt"
    filebox = [fullname_1,fullname_2,fullname_3]
    open_wordlist = open(filebox[category], 'r')
    words = open_wordlist.readline().split('/')
    word = words[order].strip()
    hints = open_wordlist.readline().split('/')
    hint = hints[order]
    return word, hint

def check_unique(word): # if a word has double characters, We count as 1 from https://www.geeksforgeeks.org/efficiently-check-string-duplicates-without-using-additional-data-structure/
    # An integer to store presence/absence  
    # of 26 characters using its 32 bits
    check = 0
    for i in range(len(word)): 
        val = ord(word[i]) - ord('a')
        # If bit corresponding to current  
        # character is already set 
        if (check & (1 << val)) > 0: 
            return False
        # set bit in checker  
        check |= (1 << val) 
    return True
# display part
print("Select Category by 1,2,3 as integer."+"\n")
print("1. Animals")
print("2. Food")
print("3. Memes "+"\n")
print("You have 10 chance(life) to guess."+"\n")
print("Warning!!! : All hints are from urbandictionary.com. Honestly I'm not trolling but just wanna see your smile :) Please enjoy"+"\n")

try: 
    category = int(input())
except:
    print("That's not valid option!! Exit the game.")
    sys.exit(0)

if category < 1 and category > 2:
    print("That's not valid option!! Exit the game.")
    sys.exit(0)
else:
    get_word_and_hint(category, order)

print("Hint: " + hint + "\n") # show hint
point_max = len(word) # calculate point from lenght of word

if check_unique(word): # if word has double characters, we count as 1
    pass
else:
    point_max -= 1

while life > 0: # strat a game
    # printing blank and character that user just guessed
    for char in word:
        if char in guesses:
            print(char, end = " ")
        else:
            print("_", end = " ")
    # display status
    print("Score: " + str(point) + " " + "Life: " + str(life) + " " + "guessed: " +(guesses), end = " ")
    print("\n")
    print("You guess: ", end = " ")
    # only get a character input 
    guess = input().lower()
    if guess.isalpha() and len(guess) == 1:
        guesses += guess
        if guess in word:
            point += 1
        else:
            life -= 1
    else:
        print("\n"+"Please guess only 1 alphabet."+"\n")
        life -= 1
    # conclusion of game
    if point == point_max:
        for j in word:
            print(j, end = " ")
        print("Score: " +str(point) + " " + "Life: " + str(life) + " " + "guessed: " +(guesses) +"\n")
        print("You won, Good game well played."+"\n")
        break
    if life == 0:
        print("\n"+"Sorry not today. " + "Life: " + str(life) + " Answer is " + word + ".")
        break
    

    




