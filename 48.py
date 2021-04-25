#! python3
import os

def daGenerator(dirName):
    for textFile in os.listdir(dirName):
        for row in open(os.path.join(dirName, textFile), 'r'):
            yield row.split('\n')[0]

nextGen = daGenerator('C:\\Users\\Alex\\Desktop\\Test')
print(next(nextGen))
print(next(nextGen))
print(next(nextGen))
print(next(nextGen))
print(next(nextGen))
print(next(nextGen))
print(next(nextGen))
