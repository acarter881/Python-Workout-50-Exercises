# In freedonia.py
provinceAndRate = {'Chico': .50, 'Groucho': .70, 'Harpo': .50, 'Zeppo': .40}

def calculate_tax(amount, province, hour):
    return amount + (amount * provinceAndRate[province] * (hour/24))
 
# In use_freedonia.py
from freedonia import calculate_tax

print(calculate_tax(500, 'Harpo', 21))
