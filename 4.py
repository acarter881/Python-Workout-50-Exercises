#! python3

def hex_output():
    decimalValue = 0
    hex = input('Enter a hexidecimal number to convert to a decimal:\n')
    for index, digit in enumerate(reversed(hex)):
        decimalValue += (int(digit) * 16 ** index)
    print(f'{hex} converted from hexidecimal to decimal is {decimalValue}.')

hex_output()
