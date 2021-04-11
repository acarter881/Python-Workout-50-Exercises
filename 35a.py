#! python3

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

my_dict = {letter:value for value, letter in enumerate(letters, start=1)}
print(my_dict)
