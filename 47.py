#! python3

class CircleIterator:
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.index = 0

    def __next__(self):
        if self.index >= self.number:
            raise StopIteration

        value = self.sequence[self.index % len(self.sequence)]
        self.index += 1
        return value

class Circle:
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
    
    def __iter__(self):
        return CircleIterator(self.sequence, self.number)
    
c = Circle('abc', 6)
print(list(c))
print(list(c))
