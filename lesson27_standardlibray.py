# Use an import statement at the top

import random
import os.path


data_file = os.path.join("/Users/elena/", "words.txt")

word_file = "words.txt"
word_list = []
## word_file
#fill up the word_list
with open(data_file,'r') as words:
	for line in words:
		# remove white space and make everything lowercase
		word = line.strip().lower()
		# don't include words that are too long or too short
		if 3 < len(word) < 8:
			word_list.append(word)

# Add your function generate_password here
# It should return a string consisting of three random words
# concatenated together without spaces
def generate_password():
    password=""
    for i in range(3):
        #index_of_word = secrets.randbelow(len(word_list))
        index_of_word = random.randrange(len(word_list))
        password+=word_list[index_of_word]
    return password





# test your function
print(generate_password())
