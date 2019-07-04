### Create an app that take user input of target words, open/read a pdf or text file, count target words, and create a visual of target words

### USER INPUT: TARGET WORDS
	# 1. User provides target words: If 0 given, move to option 2
	# 2. No target words. Just display top 10 words used
	# 3. Non-target words: Words to make exempt from count (Name of character or company abbreviation, non-important stuff)

### USER INPUT: FILE NAME (preferrably within same directory or absolute path)

### FILE HANDLING
	# Create a copy of the file called filenamecopy
	# Open and read-only on file
	# Close file
	# Delete copy of file from directory

### DATA ACQUISITION
	# Database of useless words: prepositions, etc. 
	# Extract words from figures and images --> This bit might be tricky? 
	# Count total words - variable totalwords
	# If target words provided, count those
	# Else, count words into dictionary 
		# key = word, value = count

### DATA HANDLING
	# Scale top 10 word count or target word count 
		# sum_of_counts
		# word_percentage = count_of_word / sum_of_counts
		# word_percentage will determine how large the word is displayed on the word cloud 

### CREATE IMAGE
	# Actually, how do you do this?

import PyPDF2
import re # regular expression # https://www.w3schools.com/python/python_regex.asp # 6/24/2019

def displayMenu():
	message = "Hello! \n 1. Input target words \n 2. Display top words \n 3. Non-target words (default: none) \n 4. Upload pdf or txt file \n XXX. Exit program"
	print(message)
	userChoice = str(input("Enter: 1-4 ")).strip()

	return userChoice

def getWordDict():
	# method that will get good_words and bad_words :-)

	# 6/15/2019 - should consider using text box and buttons for this
	# 6/15/2019 - should also consider regular expression to parse input for word, i.e., user inputs "cats! " -> strip punctuation and white space
	# 6/15/2019 - also, after word is added to dictionary, should display on screen a menu of added words
			# 	- example: after "terry" is added, the screen will display "terry", then "gigi" is added, the screen will display "terry" and "gigi"
	words = {} # empty dictionary; add words as key, value initial = 0
	
	while True:
		word = str(input("Please input one word at a time. Click next to continue. When finished, enter white space (temp).")).strip().upper()
		if word == "": # if input is nothing, then exit
			break
		words[word] = 0 # adding word to dictionary
		# 6/15/2019 - this should be a button: "Next word" or "No more words" # can also give option to upload a text file
	return words

	# how to handle words that user finds irrelevant: 
		# 1. create a list of these words
		# 2. at the end of the program, remove them from the dictionary (words) 

def fileHandling(filename):
	# 6/15/2019 - LEAVE OFF HERE. CONTINUE 6/16/2019
		# Reference this link: https://en.wikipedia.org/wiki/PDF --> Look under: Technical Overview: File Structure
	# 6/19/2019 - How to read PDF Files in python: https://automatetheboringstuff.com/chapter13/
	# using 3rd party module PyPDF2 (pip3 install PyPDF2 on 6/19/2019)
	pdfFileObj = open(filename, "rb")
	pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
	numpages = pdfReader.numPages
	# print(numpages)
	textFile = open("pdftoText.txt", "+w")
	
	# read through all pages
	for n in range(numpages):
		page = pdfReader.getPage(n)
		# extract text
		text = page.extractText() # data type of text: string
		# handle strings: split into list, use loop to strip white space/punctuation, regular expression to parse words
		textList = text.split() # a list of text in a given page 
		# write text to new text file
		for text in textList:
			textFile.write(text + "\n")
	textFile.close()
	pdfFileObj.close()

	return textFile

def parseWords(filename): 
	# 6/24/2019 takes text file as input
	# uses regular expression to parse through numbers, punctuation, and errors caused by PyPDF2
	# open text file, read and write
	textFile = open(filename, "r")
	textList = textFile.readlines() # reads all lines, returns each line as element in list
	words_only_TextFile = open("words.txt", "+w")
	# regular exp it up
	# remove punctuation
	# split up fused words, flyercat = flyer cat 
	# 6/25/2019 - maybe I should be working with a dictionary rather than a list?
	for t in range(len(textList)):
		word = textList[t].lower()

		# removing punctuation # replace punc with white space, split, append to list
		word = re.sub("[.#/!?+-=$]", " ", word) # I wonder if there's a way to not hard code this
		word = word.strip()
		tempList = word.split()

		# write words to file
		for w in tempList:
			words_only_TextFile.write(w + "\n")

		# 6/25/2019 - still needs to handle fused words!!!!

	# close file
	words_only_TextFile.close()
	textFile.close()

	return words_only_TextFile

def wordCounter(filename): 
	# use words.txt
	wordCountDict = {} # will add words to this dictionary, return this dictionary
	
	words = open(filename, "r")
	wordsList = words.readlines()
	
	for w in range(len(wordsList)):
		if wordsList[w] in wordCountDict: # word in dictionary
			wordCountDict[wordsList[w]] += 1 
		else:
			wordCountDict[wordsList[w]] = 1

	for k in wordCountDict.keys():
		print(k, wordCountDict[k])

	return wordCountDict # will return a dictionary

def sorter(wordDict):
	

def main():
	flag = True
	# while flag:
	# 	userChoice = displayMenu()
	# 	if userChoice == "1":
	# 		goodWords = getWordDict()
	# 		print(goodWords)

	# 	if userChoice == "2":
	# 		goodWords = {} # empty dictionary initialized

	# 	if userChoice == "3":
	# 		badWords = getWordDict()
	# 		print(badWords)

	# 	if userChoice == "4":
	# 		filename = str(input("Enter absolute path: ")).strip()

	# 	if userChoice == "XXX":
	# 		flag = False
	textFile = fileHandling("generalAviathonFlyerpdf.pdf") # textFile is file type object named pdftoText.txt in directory
	test = parseWords("pdftoText.txt") # test is file type object named words.txt in directory 
	wordDict = wordCounter("words.txt") # wordDict is dictionary type object 


main()