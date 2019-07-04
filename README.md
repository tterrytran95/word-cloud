# word-cloud
    
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
