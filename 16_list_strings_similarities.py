# strings can do a lot of the same things lists can do, but strngs are immutable.
# immutable values like strings and tuples cannot be modified "in place".
# mutable values, like lists, can be modified in place
# variables don't contain lists, they contain references to lists
# when passing a list argument to a function, you are actually passing a list reference.
# changes made to a list in a function will affect the list outside the function.
# the '\' line continuation character can be used to stretch Python instructions across multiple lines.

# strings and lists are similar
print(list('Hello'))
name='Zophie'
print(name[0])
print(name[1:3])
print(name[-2])
print('Zo' in name)
print('xxx' in name)
for letter in name:
    print(letter)

# the list datatype is mutable. the string datatype is immutable

name='Zophie the cat'
print(name[7])
#name[7]='x' # this returns TypeError as strings are immutable

name='Zophie a cat'
newName=name[0:7]+'the'+name[8:12]
print(newName)

spam=[0,1,2,3,4,5] # this actually store a reference to spam, not the actual list.
cheese=spam # since we made this equal, it created two lists with the same reference.
cheese[1]='Hello!' # therefore; this changes the reference and so both lists change
print(cheese)
print(spam)
# immutable values don't share this problem because they can't be modified "in place". They can only be replaced by new values.

# passing lists in function calls
def eggs(cheese):
    cheese.append('Hello') # the operation of this function should be contained to its local scope.

spam=[1,2,3]
eggs(spam) # this changes the value of spam outside the functions local scope because the list applied to spam is actually that global reference.
print(spam)

import copy
spam=['A','B','C','D']
cheese=copy.deepcopy(spam) # use this to make a new reference by copying a list.
cheese[1]=42
print(cheese)
print(spam)

#line continuation
spam=['apples', # can makes lists continue on lines within the bracket
'oranges',
'bananas',
'cats']
print(spam)
print('Four score and seven'+\
    ' years ago.') # using the "\" line concatination operator to concatinate a string to the next line.