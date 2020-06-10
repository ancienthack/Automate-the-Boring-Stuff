# dictionary data type

myCat={'size': 'fat', 'color': 'gray', 'disposition': 'loud'} # dictionary={key: value}
print(myCat['size'])
print('My cat has ' + myCat['color'] + ' fur.')

spam={12345: 'Luggage combination', 42: 'The Answer'} # dictionaries are not ordered like lists
print([1,2,3]==[3,2,1]) # this is false in a list
eggs={'name': 'Zophie', 'species': 'cat', 'age': 8}
ham={'species': 'cat', 'name': 'Zophie', 'age': 8}
print(eggs==ham) # this is true in a dictionary

# dictionary is more about defining (values) words (keys)

#eggs['color'] # this causes a KeyError because color does not exist in eggs.

# in or not in operators
print('name' in eggs) # True, name is in eggs
print('name' not in eggs) # False
# disctionaries are mutable like lists, they are kept in a reference
# keys(), values(), and items() Dictioanry methods
print(list(eggs.keys())) # returns a list of keys in the dictionary
print(list(eggs.values())) # returns a list of values in the dictionary
print(list(eggs.items())) # prints two item tuples containing the key and its value.

for k in eggs.keys():
    print(k)
for v in eggs.values():
    print(v)
for k, v in eggs.items(): # use this to not return the tuple
    print(k, v)
for i in eggs.items():
    print(i)
print('cat' in eggs.values()) # returns True