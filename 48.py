#! python3
import os

def daGenerator(dirName):
    os.chdir(dirName)
    for textFile in os.listdir(dirName):
        for row in open(textFile, 'r'):
            yield row.split('\n')[0]

nextGen = daGenerator('C:\\Users\\Alex\\Desktop\\Test')
print(next(nextGen))
print(next(nextGen))
print(next(nextGen))
print(next(nextGen))
print(next(nextGen))
print(next(nextGen))
print(next(nextGen))
print(next(nextGen))
