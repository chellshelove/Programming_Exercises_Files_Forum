import os
os.chdir('/Users/chellshelove/Documents/GitHub/forum books')
loveyouforever = open("myBook1", "r") # open the file that has the text
forever = open("myBook2", "w") # open the file that has no text 

sntnc = loveyouforever.read().split('\n') # split is used to split each line so that the number would start at every line
counter = 0 # the starting point on where the code will start counting 
for sentence in sntnc:
    counter += 1 
    forever.write(str(counter) + " " + sentence + '\n') # str is used to identify that the number are also strings 
    # and \n is used to identify that it needs to go to a new line 

forever.close()