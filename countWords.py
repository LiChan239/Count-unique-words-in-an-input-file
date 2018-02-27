"""
Program: countWords.py
Author: Li Chan
Date: 2/26/2018

Inputs a text file, counts the unique words in the file and prints all of the unique words and their counts
in alphabetical order.

"""

import re

# Take the input of the file name
fileName = input("Please enter the file name: ")

# Open the input file
inputFile = open(fileName, "r")

# Initialize a dictionary for the unique words and their counts
counts = dict()

# Add the unique words in the file to the dictionary and count its occurrence
for line in inputFile:
	words = re.split('[\W_]', line.lower()) # creates a list of the words in the line
	for word in words:
		counts[word] = counts.get(word,0) + 1 # adds the new word, for the word already seen, increment its number

sortedList = sorted(counts.items())	
item = sortedList.pop(0)

# print heading
print('{:15}{:3}'.format('Word', 'Count'))
print('-' * 20)

# print the words and its occurrence
for (word, counts) in sortedList:
	print('{:15}{:3}'.format(word, counts))



