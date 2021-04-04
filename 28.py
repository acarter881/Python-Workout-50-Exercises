#! python3

def join_numbers(rangeOfIntegers):
    return ','.join([str(num) for num in rangeOfIntegers])

print(join_numbers(range(15)))
