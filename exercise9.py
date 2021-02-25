#! python3
# A program that returns the first element and last element of a sequence (i.e., a string, list, or tuple)
from operator import itemgetter

def firstlast(sequence):
    if type(sequence) == list or type(sequence) == tuple:
        return type(sequence)(itemgetter(0,-1)(sequence))
    else:
        return sequence[0] + sequence[-1]

print(firstlast('abcdefg'))       # String
print(firstlast([1,2,3,4,5,'a'])) # List
print(firstlast((1,2,5,'w')))     # Tuple
