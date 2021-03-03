#! python3
MENU = {'sandwich': 9.99,
        'steak': 24.99,
        'hot dog': 4.99,
        'tuna': 14.00,
        'water': 0.75,
        'orange juice': 2.50,
        'chicken noodle soup': 7.00,
        'chow mein': 8.99
}

def restaurant():
    total = 0
    while 1:
        order = input('Order: ')
        if not order:
            print(f'Your total is ${total:.2f} dollars.')
            break
        if order in MENU:
            total += MENU[order]
            print(f'{order} costs ${MENU[order]:.2f} dollars; total is ${total:.2f} dollars.\n')
        else:
            print(f'Sorry, we are fresh out of {order} today.\n')
    
restaurant()
