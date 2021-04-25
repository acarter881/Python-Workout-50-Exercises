#! python3
from time import perf_counter, sleep

def myGen(userIter):
    for i in range(len(userIter)):
        if i == 0:
            yield (0, userIter[i])
            new_start = perf_counter()
            old_start = 0
        else:
            yield (new_start - old_start, userIter[i])
            old_start = new_start
            new_start = perf_counter()

nextGen = myGen(['hello', 'how', 'many', 'exercises', 'are', 'there?'])
print(next(nextGen))
sleep(2)
print(next(nextGen))
sleep(4)
print(next(nextGen))
sleep(8)
print(next(nextGen))

"""
EXAMPLE OUTPUT:
(0, 'hello')
(2.0229995, 'how')
(4.003119, 'many')
(8.014791500000001, 'exercises')
"""
