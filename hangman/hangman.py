""" -*- coding: python(3.7.1) -*-
    author: Napasin Hongngern """
""" hangman """

import os
import sys
from random import randint


print("Select Category by 1,2,3 as integer."+"\n")
print("1. Animals")
print("2. Famous games from various platform")
print("3. Netflix's original "+"\n")
print("Warning!!! : All hints are from urbandictionary.com. Honestly I'm not trolling but just wanna see your smile :) Please enjoy"+"\n")

absolute_path = os.path.dirname(os.path.abspath(__file__))

file_path_1 = absolute_path + "/animal_wordlist.txt"
file_path_2 = absolute_path + "/pcgames_wordlist.txt"
file_path_3 = absolute_path + "/netflix_original_wordlist.txt"

life = 10
word_order = 0
point_max = 0
guesses = ""
word = ''
while life == 10:
    try: 
        category = int(input())
        break
        sys.exit(0)
    except:
        category = 0
        print("That's not valid option!! Exit the game.")
        sys.exit(0)

if category == 1:
    wordlist_1 = open(file_path_1, 'r')
    firstline_of_category_1 = wordlist_1.readline()
    secondline_of_category_1 = wordlist_1.readline()
    answer = firstline_of_category_1.split('/')
    hint = secondline_of_category_1.split('/')
    wordlist_1.close()
    word_order += randint(0,4)
    word += answer[word_order]
    print("Hint: "+ hint[word_order])
    #print(answer[word_order])
elif category == 2:
    wordlist_2 = open(file_path_2, 'r')
    firstline_of_category_2 = wordlist_2.readline()
    secondline_of_category_2 = wordlist_2.readline()
    answer = firstline_of_category_2.split('/')
    hint = secondline_of_category_2.split('/')
    wordlist_2.close()
    word_order += randint(0,4)
    word += answer[word_order]
    print("Hint: "+ hint[word_order])
    #print(answer[word_order])
elif category == 3:
    wordlist_3 = open(file_path_3, 'r')
    firstline_of_category_3 = wordlist_3.readline()
    secondline_of_category_3 = wordlist_3.readline()
    answer = firstline_of_category_3.split('/')
    hint = secondline_of_category_3.split('/')
    wordlist_3.close()
    word_order += randint(0,4)
    word += answer[word_order]
    print("Hint: "+ hint[word_order])
    #print(answer[word_order])
else:
    print("That is not an option!! exit the game.")
    sys.exit(0)
    
point = 0
point_max += len(word) * 10
print(word)

while life > 0:
    guess = input()
    guesses += guess
    for char in word:
        if char in guess:
            print(char)
        else:
            print(point)



    

