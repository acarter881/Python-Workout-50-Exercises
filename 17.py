#! python3

def how_many_different_numbers(l):
    total = 0
    eL = []
    for i in range(len(l)):
        if l[i] not in eL:
            eL.append(l[i])
            total += 1
    return total

print(how_many_different_numbers([1, 2, 3, 1, 2, 3, 4, 1]))
