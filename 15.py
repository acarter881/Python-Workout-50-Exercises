#! python3

def get_rainfall():
    rainfall = {}
    while 1:
        city = input('Please enter the name of a city: ')
        if not city:
            break
        else:
            rainQuantity = int(input('How much rain has fallen? (in mm)\n'))
            try:
                rainfall[city] += rainQuantity
            except KeyError:
                rainfall[city] = rainQuantity
    for city in rainfall:
        print(f'{city}: {rainfall[city]}')
            
get_rainfall()
