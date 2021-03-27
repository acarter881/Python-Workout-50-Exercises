#! python3

"""
Desired output:
<foo></foo>
<foo>bar</foo>
<foo a="1" b="2" c="3">bar</foo>
"""

def myxml(arg1, arg2='', **kwargs):
    bigXML = ''
    bigXML += '<'+arg1+' '
    for kwarg in kwargs:
        bigXML += kwarg+'='+'"'+str(kwargs[kwarg])+'"'+' '
    bigXML = bigXML.rstrip()
    bigXML += '>'+arg2+'</'+arg1+'>'
    return bigXML

print(myxml('foo'))
print(myxml('foo', 'bar'))
print(myxml('foo', 'bar', a=1, b=2, c=3))
