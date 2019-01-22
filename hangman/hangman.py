""" -*- coding: python(3.7.1) -*-
    author: Napasin Hongngern """
""" hangman """

print("Select Category")
print("1. Animals")
print("2. Famous games from various platform")
print("3. Netflix's original "+"\n")
print("Warning!!! : All hints are from urbandictionary.com. I'm not trolling but just wanna see your smile :) Please enjoy")

category = int(input())

if category == 1:
    wordlist_1 = open(animal_wordlist.txt, 'r')
    firstline_of_category_1 = wordlist_1.readline()
    answer_of_wordlist_1 = firstline_of_category_1.split('/')
    for i in range (len(answer_of_wordlist_1)):
        print(answer_of_wordlist_1[i])
    wordlist_1.close()
if category == 2:
    wordlist_2 = open(pcgames_wordlist.txt, 'r')
    firstline_of_category_2 = wordlist_2.readline()
    wordlist_2.close()
if category == 3:
    wordlist_3 = open(netflix_original_wordlist.txt, 'r')
    firstline_of_category_3 = wordlist_3.readline()
    wordlist_3.close()




    

