#! python3

def transform_values(func, user_dict):
    return {k:func(v) for k,v in user_dict.items()}

# Goal is to return {'a': 1, 'b': 4, 'c': 9}
d = {'a':1, 'b':2, 'c':3}

print(transform_values(lambda x: x*x, d))
