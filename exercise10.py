#! python3

def mysum(*args):
  if not args:
    return args
  output = args[0]
  for arg in args[1:]:
    output += arg
  return output

print(mysum())
print(mysum(1,2,3,4))
print(mysum('a','b','c','d'))
print(mysum([1,2,3],[4,5,6],[7,8,9]))
