#! python3

def mysum(*args):
    total = 0
    for arg in args:
        total += arg
    return total

print(mysum(10,20,30,40,50))
