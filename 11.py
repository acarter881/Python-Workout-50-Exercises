#! python3

PEOPLE = [
{'first':'Reuven', 'last':'Lerner',
'email':'reuven@lerner.co.il'},
{'first':'Donald', 'last':'Trump',
'email':'president@whitehouse.gov'},
{'first':'Vladimir', 'last':'Putin',
'email':'president@kremvax.ru'},
{'first':'Alex', 'last':'Carter',
'email':'lulzsNotRealEmail@gmail.com'},
{'first':'Grubs', 'last':'Carter',
'email':'lulzsNotRealEmail@gmail.com'}
]

def alphabetize_names():
    return sorted(PEOPLE, key=lambda item:(item['last'], item['first']))
print(alphabetize_names())
