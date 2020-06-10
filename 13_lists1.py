# a list is a value that contains multiple values
# values in a list are also called items
# can access items with their interger index
# indexes start at 0, not 1
# can use negative indexes. -1st is last item, -2nd is second last item, etc
# can get multiple items from a list using a slice
# slice has two indexes. starts at first index and goes up to but doesn't include second index
# len() function, cancatenation, and replication work with lists the same as with strings
# can convert a value into a list by passing it to the list() function

# List data type, indexing, splicing
spam=['cat', 'bat', 'rat', 'elephant'] # defining a list value
print(spam) #printing a list
print(spam[0]) # indexing (single value) a list item (the first item starts at 0)
print(spam[1:3]) # slicing (list of values) a list. 1st number is starting item, 2nd number is ending item (up to but not including)
print(spam[-1]) # negative index, counts backwards. -1st is last item, -2nd is 2nd last item, etc
print(spam[::-1]) # 3rd number is step value.
                # a blank value in a slice assumes [start at value 0:continue until final value: count normally] ([:4],[2:],[2:4:],[::-1])

# Lists within lists
spam=[['cat','bat'], [10,20,30,40,50]]
print(spam[0]) # this index refers to the first list
print(spam[0][1]) # this index refers to the first list and first itme of that list
print(spam[0:2][1]) # this slices both lists then outputs index 1 of the master list (prints list 2)
print(spam[0:2][1][1]) # does as above but outputs index 1 of list 2 (prints 20)

# Changing a lists item
spam=[10,20,30]
print(spam)
spam[1]='hello' # assign a new index value by indicating an index of a variable.
print(spam)
spam[1:3]=['cat','dog','mouse'] # replace a slice like so. if there are more values than current indexes, this will add more indexes.
print(spam)
del spam[1] # use del statment to delete a value from a list (UNassignment statement)
print(spam)

# can use len() on a list to determine how many items are in the list
# can use concatination on lists (+)
# can use list replication (*)
# many things you can do with strings you can also do with lists

# list() function
list('hello') # use to list items in a string. similar to converting str(), int(), float(), etc

# in and not in operators
'howdy' in ['hello', 'hi', 'howdy', 'hiya']
42 in ['hello', 'hi', 'howdy', 'hiya']
'howdy' not in ['hello', 'hi', 'howdy', 'hiya']