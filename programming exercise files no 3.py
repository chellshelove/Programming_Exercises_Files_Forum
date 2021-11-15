import os
os.chdir('/Users/chellshelove/Documents/GitHub/forum 2') 
myBook = open("66737-0.txt", "r") 

import re

def avg_word_length(filepath):
    file = open(filepath)
    words = re.findall('\w+', file.read())
    return sum([len(word) for word in words]) / len(words)

print(avg_word_length('66737-0.txt'))
myBook.close