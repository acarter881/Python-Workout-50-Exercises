#! python3

def flatten(userList):
    newList = []
    [newList.append(j) for i in userList for j in i]
    return newList

print(flatten([[1,2], [3,4]]))
