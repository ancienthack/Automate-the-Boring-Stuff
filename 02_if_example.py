name='Alice'
if name=='Alice':
    print('Hi Alice')
print('Done')

print('Enter a name. ')
name=input()
if name: # doesn't contain boolean operators, a blank string returns a "falsey" value. This is considered bad code
    # change the above line to something like (if name != '':)
    print('Thank you for entering a name.')
else: # all others are "truthy" values
    print('You did not enter a name.')

# 0 is falsey, all others are truthy
# 0.0 is falsey, all others are truthy

bool(0) #false
bool(1) #true
bool('') #false
bool('Hello') #true