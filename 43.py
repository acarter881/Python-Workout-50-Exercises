#! python3

class Sheep:
    def __init__(self, color):
        self.color = color
        self.species = 'sheep'
        self.number_of_legs = 4
        
    def __repr__(self):
        return str([self.color, self.species, self.number_of_legs])

class Wolves(Sheep):
    def __init__(self, color):
        self.color = color
        self.species = 'wolf'
        self.number_of_legs = 4

class Snakes(Sheep):
    def __init__(self, color):
        self.color = color
        self.species = 'snake'
        self.number_of_legs = 0

class Parrots(Sheep):
    def __init__(self, color):
        self.color = color
        self.species = 'parrot'
        self.number_of_legs = 2

s = Sheep('white')
print(s)
w = Wolves('gray')
print(w)
k = Snakes('green')
print(k)
p = Parrots('purple')
print(p)
