#! python3

# The function from Exercise 6
def pl_sentence(string):
    newString = ''
    for word in string.split():
        if word[0] in 'aeiou':
            newString += word + 'way' + ' '
        else:
            newString += word[1:] + word[0] + 'ay' + ' '
    return newString

# The function we're creating in Exercise 31
def pigFromFile(fileName):
    with open(fileName, 'r') as f:
        return ''.join([word for word in map(pl_sentence, ''.join(f.readlines()).split())])

print(pigFromFile('C:\\Users\\Alex\\Desktop\\hello\\Python\\randomTextFile.txt'))
