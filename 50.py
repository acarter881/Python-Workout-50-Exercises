#! python3
import sys

def mychain(*args):
    for arg in args:
        for element in arg:
            try:
                yield element
            except StopIteration:
                sys.exit()

nextChain = mychain('abc', [1, 2, 3], {'a': 1, 'b': 2})
print(next(nextChain))
print(next(nextChain))
print(next(nextChain))
print(next(nextChain))

"""
EXAMPLE OUTPUT:
a
b
c
1
"""
