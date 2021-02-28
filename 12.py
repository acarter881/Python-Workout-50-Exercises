#! python3
from collections import Counter

def most_repeating_word(words):
    highScore = 0
    theWord = ''
    for word in words:
        if Counter(word).most_common(1)[0][1] > highScore:
            highScore = Counter(word).most_common(1)[0][1]
            theWord = word
    return theWord

print(most_repeating_word(['this', 'is', 'an', 'elementary', 'test', 'example', 'mississippi']))
