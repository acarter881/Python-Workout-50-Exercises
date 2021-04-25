#! python3

def mychain(*args):
    for arg in args:
        for element in arg:
            yield element
            
nextChain = mychain('abc', [1, 2, 3], {'a': 1, 'b': 2})
for item in nextChain:
    print(item)
