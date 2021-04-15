#! python3

class Scoop:
    def __init__(self, flavor):
        self.flavor = flavor

class Bowl:
    max_scoops = 3

    def __init__(self):
        self.scoops = []
        
    def add_scoops(self, *new_scoops):
        for one_scoop in new_scoops:
            if len(self.scoops) < self.max_scoops:
                self.scoops.append(one_scoop.flavor)
    
    def __repr__(self):
        return str(self.scoops)

class BigBowl(Bowl):
    max_scoops = 5
        
s1 = Scoop('chocolate')
s2 = Scoop('vanilla')
s3 = Scoop('persimmon')

b = BigBowl()
b.add_scoops(s1)
b.add_scoops(s2)
b.add_scoops(s1, s3)

print(b) # Returns "['chocolate', 'vanilla', 'chocolate', 'persimmon']"
