#! python3
import operator

"""
addition (add)
subtraction (sub)
multiplication (mul)
division (truediv)
modulus (mod)
exponentiation (pow)
"""

def calc(mathString):
    operations = {'+': 'add', 
                  '-': 'sub',
                  '*': 'mul',
                  '/': 'truediv',
                  '%': 'mod',
                  '**': 'pow',
    }
    method_to_call = getattr(operator, operations[mathString[0:2].strip()])
    res = method_to_call(int(mathString[2:4].strip()),int(mathString[4:].strip()))
    return res

print(calc('% 2 3'))
print(calc('** 4 3'))
print(calc('+ 2 3'))
