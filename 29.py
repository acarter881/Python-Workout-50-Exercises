#! python3

def sum_numbers():
    userStr = input('Please enter your list of integers:\n')
    return sum([int(item) for item in userStr.split() if item.isdigit()])

print(sum_numbers())
