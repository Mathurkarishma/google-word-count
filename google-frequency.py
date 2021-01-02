# Starter Code -
# Based on Toby Donaldson's Python: Visual QuickStart Guide
# function print_file_stats (location 5347)

# Modified for UMUC DATA 620 by Karishma Mathur
# Last updated:  12/15/19
# Program to open a text file named 'Google_Mar2009.txt'
# Used to open other text files for this particular project for years 1999 and 2019
# This program will give a word count of all the words in the file
# and give the top 50 words.
# It has not been modified to do any stop wording 

# Open the input file
#s = open('//Users//Karishma//Google Drive//UMGC//Data 620//Google_Mar2009.txt').read()


s = open('Google_Mar2009.txt', encoding="utf8").read()
# Take out unnecessary symbols
s = s.replace(",","")
s = s.replace(".","")
s = s.replace("”","")
s = s.replace("“","")
s = s.replace(":","")
s = s.replace("’","")
s = s.replace("•","")
s = s.replace("–","")

# count characters
num_chars = len(s)

# count lines
num_lines = s.count('\n')

words = s.split()

d = {}
for w in words:
    if w in d:    # seen w before?
        d[w] += 1
    else:
        d[w] = 1

num_words = sum(d[w] for w in d)

lst = [(d[w], w) for w in d]
lst.sort()
lst.reverse()

print('Your input file has characters = ' + str(num_chars))
print('Your input file has num_lines = ' + str(num_lines))
print('Your input file has num_words = ' + str(num_words))
# Added function for only unique words
print('Unique words = ' + str(len(d)))

print('\n The 50 most frequent words are \n')

i = 1
for count, word in lst[:50]:
    print('%2s.  %4s %s' % (i, count, word))
    i += 1

# End of script
