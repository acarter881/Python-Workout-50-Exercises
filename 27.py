#! python3
import random

def create_password_generator(userStr):
    def innerFunc(userInt):
        return ''.join([random.choice(userStr) for i in range(userInt)])
    return innerFunc

alpha_password = create_password_generator('abcdef')
symbol_password = create_password_generator('!@#$%')

print(alpha_password(5))    # efeaa
print(alpha_password(10))   # cacdacbada
print(symbol_password(5))   # %#@%@
print(symbol_password(10))  # @!%%$%$%%#
