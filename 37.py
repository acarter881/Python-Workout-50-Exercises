#! python3

def menu(**kwargs):
    while 1:
        userStr = input('Please enter your string: \n')
        if userStr in kwargs:
            return kwargs[userStr]()
            break
        else:
            print('Wrong. Please try again.')
            continue
        
def func_a():
    return "A"
def func_b():
    return "B"

return_value = menu(a=func_a, b=func_b)

print(f'Result is {return_value}')
