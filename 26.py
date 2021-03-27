#! python3
import operator

def calc(mathString):
    operations = {'+': 'add', 
                  '-': 'sub',
                  '*': 'mul',
                  '/': 'truediv',
                  '%': 'mod',
                  '**': 'pow',
    }
    method_to_call = getattr(operator, operations[mathString[0:2].strip()])
    return method_to_call(int(mathString[2:4].strip()), int(mathString[4:].strip()))

print(calc('% 2 3'))
print(calc('** 4 3'))
print(calc('+ 2 3'))
