# for loops technically iterate over the values in a list
# the range() function returns a list-like vakue, which can be passed to the list() function if you need an actual list value.
# variables can swap their values using multiple assignment.
# augmented assignment operators like += are used as shortcuts.

# For Loops with Lists
for i in range(4):
    print(i)

spam=list(range(0,100,2))
print(spam)

supplies=['pens', 'staplers', 'flame-throwers', 'binders', 'dudes', 'dudettes', 'dildos', 'pocket pussies']
for i in range(len(supplies)):
    print('Index '+str(i)+' in supplies is: '+supplies[i])

# Multiple Assignment
cat=['fat', 'orange', 'loud']
size=cat[0]
color=cat[1]
disposition=cat[2]

size, color, disposition=cat
print(size)
print(color)
print(disposition)

size, color, disposition='skinny', 'black', 'quiet'
print(size)
print(color)
print(disposition)

a='AAA'
b='BBB'
print(a,b)
a,b=b,a
print(a,b)

# Augmented Operators
spam=42
print(spam)
spam=spam+1
print(spam)
spam+=1 # can use +=, -=, *=, /=, %=
print(spam)