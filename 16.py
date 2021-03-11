#! python3
"""
Wow, this code is poorly written
"""

def dictdiff(d1, d2):
    if d1 == d2:
        return {}
    else:
        diffDict = {}
        for k in d1:
            if d1.get(k) == d2.get(k):
                pass
            elif k in d1 and k not in d2:
                diffDict[k] = list((d1[k], None))
            else:
                diffDict[k] = list((d1[k], d2[k]))
        for k in d2:
            if d1.get(k) == d2.get(k):
                pass
            elif k not in d1 and k in d2:
                diffDict[k] = list((None, d2[k]))
            else:
                diffDict[k] = list((d1[k], d2[k]))
        return diffDict

d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {'a': 1, 'b': 2, 'c': 4}
d3 = {'a': 1, 'b': 2, 'd': 3}
d4 = {'a': 1, 'b': 2, 'c': 4}
d5 = {'a': 1, 'b': 2, 'd': 4}
print(dictdiff(d1, d5))
