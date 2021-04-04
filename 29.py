#! python3

def sum_numbers(userStr):
    return sum([int(item) for item in userStr.split() if item.isdigit()])

print(sum_numbers('10 abc 20 de44 30 55fg 40'))
