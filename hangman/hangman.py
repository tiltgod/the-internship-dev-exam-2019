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

life = 5
word_order = 0
point_max = 0
guesses = ""
word = ''

try: 
    category = int(input())
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
    word += "rabbit"
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
point_max += len(word) 
print(point_max)
print(word)

def areCharactersUnique(s): 
      
    # An integer to store presence/absence  
    # of 26 characters using its 32 bits 
    checker = 0
      
    for i in range(len(s)): 
          
        val = ord(s[i]) - ord('a') 
          
        # If bit corresponding to current  
        # character is already set 
        if (checker & (1 << val)) > 0: 
            return False
          
        # set bit in checker  
        checker |= (1 << val) 
          
    return True
      
# Driver code 
s = word
if areCharactersUnique(s): 
    print("Yes") 
else: 
    print("No") 

while life > 0:
    failed = 0
    turn = 0
    for char in word:
        if char in guesses:
            print(char, end = " ")
        else:
            print("_", end = " ")
        
    print(str(point) + "\n", end = " ")
    
    guess = input()
    guesses += guess

    if guess in word:
        point += 1
    else:
        life = life - 1
    if life == 0:
        print("wp")
        break
    if point == point_max:
        print("well played")
        print(point)
        break