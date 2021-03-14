#! python3
import os

def find_longest_word(fileName):
    theWord = ''
    with open(fileName, 'r') as f:
        for row in f:
            for word in row.split():
                if len(word) > len(theWord):
                    theWord = word
    return theWord

def find_all_longest_words(directory):
    return {fileName:find_longest_word(fileName) for fileName in os.listdir(directory)}

print(find_all_longest_words('.'))
