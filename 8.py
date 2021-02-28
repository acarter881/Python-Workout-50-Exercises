#! python3

def strsort(word):
    newStr = []
    for letter in word:
        newStr.append(letter)
    newStr.sort()
    return ''.join(newStr)

print(strsort('cba'))
