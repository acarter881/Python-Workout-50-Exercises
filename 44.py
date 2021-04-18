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
wolf = Wolf('gray')
snake = Snake('green')
parrot = Parrot('purple')

class Cage:
    def __init__(self, id):
        self.id = id
        self.cage = []
    
    def add_animals(self, *animals):
        for animal in animals:
            self.cage.append(animal)

    def __repr__(self):
        return f'{self.id}: {self.cage}'

c1 = Cage(1)
c1.add_animals(wolf, sheep)

c2 = Cage(2)
c2.add_animals(snake, parrot)

print(c1)
print(c2)
