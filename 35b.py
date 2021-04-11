#! python3
import string

def gematria_for(singleWord):
    total = 0
    big_dict = {v:k for k,v in dict(enumerate(string.ascii_lowercase, start=1)).items()}
    for char in singleWord:
        try:
            if char == char.lower():
                total += big_dict[char]
        except KeyError:
            continue
    return total

def gematria_equal_words(singleWord):
    compareValue = gematria_for(singleWord)
    return [word.strip() 
           for word in open('C:\\Users\\Alex\\Desktop\\hello\\Python\\words.txt', 'r')
           if gematria_for(word) == compareValue]

print(gematria_equal_words('cat'))
