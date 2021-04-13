#! python3

class Scoop:
    def __init__(self, flavor):
        self.flavor = flavor

def create_scoops(userList):
    for i in range(len(userList)):
        Scoop(userList[i])
        print(f'The flavor is {Scoop(userList[i]).flavor}')

print(create_scoops(['chocolate', 'vanilla', 'persimmon']))
