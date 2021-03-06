#! python3

class Animal():
    def __init__(self, color, number_of_legs):
        self.species = self.__class__.__name__
        self.color = color
        self.number_of_legs = number_of_legs

    def __repr__(self):
        return f'{self.color} {str(self.species).lower()}, {self.number_of_legs} legs'

class Sheep(Animal):
    def __init__(self, color):
        super().__init__(color, 4)

class Wolf(Animal):
    def __init__(self, color):
        super().__init__(color, 4)

class Snake(Animal):
    def __init__(self, color):
        super().__init__(color, 0)

class Parrot(Animal):
    def __init__(self, color):
        super().__init__(color, 2)

sheep = Sheep('white')
print(sheep)
wolf = Wolf('gray')
print(wolf)
snake = Snake('green')
print(snake)
parrot = Parrot('purple')
print(parrot)

"""
white sheep, 4 legs
gray wolf, 4 legs
green snake, 0 legs
purple parrot, 2 legs
"""
