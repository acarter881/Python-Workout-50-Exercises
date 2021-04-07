#! python3

# Goal is to output a flip of the dictionary (i.e., all of the keys become the values, and vice versa)
d = {'a':1, 'b':2, 'c':3}

# Can do this with a dictionary comprehension, using the "items" method
print({v:k for k,v in d.items()})
