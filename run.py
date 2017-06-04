from sys import argv
import time

start_time = time.clock()

scores = {"A": 1, "C": 3, "B": 3, "E": 1, "D": 2, "G": 2,
          "F": 4, "I": 1, "H": 4, "K": 5, "J": 8, "M": 3,
          "L": 1, "O": 1, "N": 1, "Q": 10, "P": 3, "S": 1,
          "R": 1, "U": 1, "T": 1, "W": 4, "V": 4, "Y": 4,
          "X": 8, "Z": 10}


try:
	script,rack = argv                          #set second argument as rack
except ValueError:                              #handle error when rack isnt provided
        print "USAGE: python run.py RACK" 
	print "Enter Rack"
	exit(1)

if (rack.isalpha()) != True:                    #check whether rack is only alphabets
	print "Enter Only Alphabets "
	exit(1)

rack = rack.upper()                             #changing into uppercase 
rack = ''.join(sorted(rack))                    #sorting the rackletters for better performance

wordlist = []                                   #list of all words from sowpods.txt

try:
    with open("sowpods.txt", "r") as fp:
        for line in fp:
            wordlist.append(line.strip())       #add to wordslist
except EnvironmentError:                        #handle error when sowpods.txt is missing
    print "Cannot find sowpods.txt"
    exit(1)

valid_words = []                                #list of all valid words made from rack

for word in wordlist:                           #looping on each word in given database of words
    validity = True                             
    rack_letters = list(rack)
    
    for letter in word:                         #looping on each letter in a word from database
        if letter not in rack_letters:          #if the letter isnt found in input rack
            validity = False
            break                               # No need to keep checking letters.
        else:
            rack_letters.remove(letter)         #remove the letter to avoid repitition 
    if validity == True:                        #calculate score for valid words
        total = 0
        for letter in word:
            total = total + scores[letter]
        valid_words.append([total, word])


valid_words.sort()                              #sort by scrabble score.

for entry in valid_words:                       # Print the valid words
    score = entry[0]
    word = entry[1]
    print(str(score) + " " + word)
    
print time.clock() - start_time, "seconds"

