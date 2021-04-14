#! python3

class Scoop:
    def __init__(self, flavor):
        self.flavor = flavor

class Bowl:
    def __init__(self):
        self.scoops = []
        
    def add_scoops(self, *args):
        for arg in args:
            if len(self.scoops) == 3:
                pass
            else:
                self.scoops.append(arg.flavor)
    
    def __repr__(self):
        return str(self.scoops)
        
s1 = Scoop('chocolate')
s2 = Scoop('vanilla')
s3 = Scoop('persimmon')

b = Bowl()
b.add_scoops(s1, s1)
b.add_scoops(s3)
b.add_scoops(s3)
b.add_scoops(s1, s2)

print(b) # Returns "['chocolate', 'chocolate', 'persimmon']", ignoring the extra scoops we've tried to add to the bowl
