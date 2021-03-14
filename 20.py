#! python3

def wordcount(fileName):
    with open(fileName, 'r') as f:
        numberOfCharacters = len(f.read())
    with open(fileName, 'r') as f:
        numberOfWords = len(f.read().split())
    with open(fileName, 'r') as f:
        numberOfLines = len(f.readlines())
    with open(fileName, 'r') as f:
        eL = []
        for word in f.read().split():
            if word not in eL:
                eL.append(word)
        numberOfUniqueWords = len(eL)
    return numberOfCharacters, numberOfWords, numberOfLines, numberOfUniqueWords

print(wordcount('./Python/unixStyle.txt'))
