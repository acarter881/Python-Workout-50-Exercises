#! python3
import os

def find_longest_word(fileName):
    maxLength = 0
    theWord = ''
    with open(fileName, 'r') as f:
        for row in f:
            for word in row.split():
                if len(word) > maxLength:
                    maxLength = len(word)
                    theWord = word
    return theWord

def find_all_longest_words(directory):
    AYO = {}
    for fileName in os.listdir(directory):
        AYO[fileName] = find_longest_word(fileName)
    return AYO

print(find_all_longest_words('.'))
