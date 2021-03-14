#! python3

def wordcount(fileName):
    numberOfCharacters = 0
    numberOfWords = 0
    numberOfLines = 0
    numberOfUniqueWords = 0

    with open(fileName, 'r') as f:
        eL = []
        for row in f:
            numberOfCharacters += len(row)
            numberOfWords += len(row.split())
            numberOfLines += 1
            for word in row.split():
                if word not in eL:
                    eL.append(word)
                    numberOfUniqueWords += 1
     
    return numberOfCharacters, numberOfWords, numberOfLines, numberOfUniqueWords

print(wordcount('./Python/unixStyle.txt'))
