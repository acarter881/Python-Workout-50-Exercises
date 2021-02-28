#! python3

def pl_sentence(string):
    newString = ''
    for word in string.split():
        if word[0] in 'aeiou':
            newString += word + 'way' + ' '
        else:
            newString += word[1:] + word[0] + 'ay' + ' '
    return newString

print(pl_sentence('this is a test translation'))
