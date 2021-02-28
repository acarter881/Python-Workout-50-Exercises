#! python3

def run_timing():
    time = 0
    numRuns = 0
    while 1:
        x = input('Enter 10 km run time (in minutes) [press Enter to break]: ')
        if x == '':
            break
        else:
            time += float(x)
            numRuns += 1
    return print(f'Your average 10 km time is {time/numRuns} minutes.')

run_timing()
