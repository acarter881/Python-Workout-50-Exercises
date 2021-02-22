#! python3

def pig_latin(string):
    if string[0] in ['a', 'e', 'i', 'o', 'u']:
        print(f'{string} in Pig Latin is: ' + string + 'way')
    else:
        print(f'{string} in Pig Latin is: ' + string[1:] + string[0] + 'ay')

pig_latin('python')
