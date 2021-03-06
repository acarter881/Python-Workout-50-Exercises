#! python3
import os

"""
Takes a file in the current working directory and writes the reverse of each line to a new text file
The input:
abc def
ghi jkl

The desired output:
fed cba
lkj ihg
"""

def reverse_lines(inFile, outFile):
    with open(inFile, 'r') as f1, open(outFile, 'w') as f2:
        for row in f1:
            f2.write((row[::-1].strip()+'\n'))

reverse_lines('nameOfInFile.txt', 'nameOfOutFile.txt')
