#! python3

def flatten(userList):
    return [j for i in userList for j in i]

print(flatten([[1,2], [3,4]]))
