# methods are functions that are "called on" values.
# the index() list method returns the index of an item in the list
# the append() list method adds a value to the end of the list
# the insert() list method adds a value anywhere in the list
# the remove() list method removes an item, specified by the value, from a list
# the sort() list method sorts the items in a list
# the sort() methods reverse=True keyword argument can make the sort() method sort in reverse
# sorting happens in ASCII-betical order. To sort normally, pass key=str.lower
# These list methods operate on the list "in place", rather than returning a new list
# methods are a function which is a member of a class
# methods belong to a single datatype, the methods here can only be used with the list() values. for instance, the str() function does not have an append() method, so it would return an AttributeError if used.

spam=['hello', 'hi', 'howdy', 'hiya']
print(spam.index('hello')) # this returns index 0

#index('hello') # returns a NameError. will not work without defining which list to use by using a period between list and method ^^^

print(spam.index('hiya')) # returns index 3
#print(spam.index('kdslfjh')) # returns a ValueError. will return error as it does not exist in the list

spam=['Zophie', 'Pooka', 'Fat-Tail', 'Pooka'] # duplicate values in list
print(spam.index('Pooka')) # will return the first instance of the duplicate

# add values to list using append() and insert() methods
spam=['cat', 'dog', 'bat']
print(spam)
spam.append('moose') # adds the value to the end of the list
print(spam)

spam=['cat', 'dog', 'bat']
print(spam)
spam.insert(1, 'chicken') # inserts the new value at index 1, everything else gets bumped up
print(spam)

# remove() method to remove and item from a list.
# differs from the del statement in that it removes a specific value instead of a specific index.
spam=['cat', 'bat', 'rat', 'elephant']
spam.remove('bat') # specify a list value to remove from the list. removing an item that does not exist in the list, it will return a ValueError
print(spam)

spam=['cat', 'bat', 'rat', 'cat', 'elephant']
spam.remove('cat') # will remove the first instance of duplicate values
print(spam)

# the sort() method will sort lists with string values or number values.
# lists with mixed numbers and strings cannot be sorted. returns a TypeError
# sort() uses ASCII-betical order, not alphabetical order. Which means uppercase letters come before lowercase letters.
spam=[2,5,3.14,1,-7]
spam.sort()
print(spam)
spam=['ants', 'cats', 'badgers', 'dogs', 'elephants']
spam.sort()
print(spam)
spam.sort(reverse=True) # use reverse keyword argument with bool True to reverse sort the list
print(spam)
spam=['Alice', 'Bob', 'ants', 'badgers', 'Carol', 'cats']
spam.sort() # will sort in ASCII-betical order (A,B,C,a,b,c)
print(spam)
spam=['a', 'z', 'A', 'Z']
spam.sort()
print(spam)
spam.sort(key=str.lower) # will sort traditional (A,a,B,b,C,c)