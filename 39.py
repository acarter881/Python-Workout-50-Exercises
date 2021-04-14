#! python3

class Scoop:
    def __init__(self, flavor):
        self.flavor = flavor

class Bowl:
    def __init__(self):
        self.scoops = []
        
    def add_scoops(self, *args):
        for arg in args:
            self.scoops.append(arg.flavor)
    
    def __repr__(self):
        return str(self.scoops)
        
s1 = Scoop('chocolate')
s2 = Scoop('vanilla')
s3 = Scoop('persimmon')

b = Bowl()
b.add_scoops(s1, s2)
b.add_scoops(s3)

print(b)
