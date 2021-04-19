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
        self.animals = []
    
    def add_animals(self, *animals):
        for one_animal in animals:
            self.animals.append(one_animal)

    def __repr__(self):
        output = f'Cage {self.id}:\n'
        output += '\n'.join('\t' + str(animal) for animal in self.animals)
        return output

c1 = Cage(1)
c1.add_animals(wolf, sheep)

c2 = Cage(2)
c2.add_animals(snake, parrot)

class Zoo:
    def __init__(self):
        self.cages = []

    def add_cages(self, *cages):
        for one_cage in cages:
            self.cages.append(one_cage)
    
    def __repr__(self):
        return '\n'.join(str(one_cage) for one_cage in self.cages)
      
    def animals_by_color(self, color):
        return [one_animal for one_cage in self.cages for one_animal in one_cage.animals if one_animal.color == color]

    def animals_by_legs(self, number_of_legs):
        return [one_animal for one_cage in self.cages for one_animal in one_cage.animals if one_animal.number_of_legs == number_of_legs]
    
    def number_of_legs(self):
        return sum(one_animal.number_of_legs for one_cage in self.cages for one_animal in one_cage.animals)

z = Zoo()
z.add_cages(c1, c2)

print(z)
print(z.animals_by_color('white'))
print(z.animals_by_legs(4))
print(z.number_of_legs())
