#! python3

def ubbi_dubbi(string):
    ubDub = []
    for letter in string:
        if letter in 'aeiou':
            ubDub.append('ub' + letter)
        else:
            ubDub.append(letter)
    return ''.join(ubDub)

print(ubbi_dubbi('soap'))
