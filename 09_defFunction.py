# a function is a mini-program within a program
# main purpose of a function is to group code that gets used multiple times.
# when something needs adjusted you only have to change it in one place. avoid duplicating code.
# every function has a return value but not all functions have a return statement. default return value is None.

#def hello(): # def statement used to define a new function. in this case the hello function
   #print('Howdy!') # everything nested is the body of the function
   #print('Howdy!!!')
   #print('Hello there.')

#hello(#arguments go here) # this is a function call. when called it moves to line 3 to run the function.
#hello()
#hello()

def hello(name): # (parameter - the variable inside the def statement brackets)
    print('Hello '+name) # (return - the output value of a function)

hello('Alice') # (argument - input value to the function)
hello('Bob')       

def plusOne(number):
    return number+1 # (return statement - specifies a return value)

newNumber=plusOne(5)
print(newNumber) # print returns a None value, similar to True and False, but is it's own data type

# keyword arguments are usually optional arguments.
print('Hello', end='') # end is a keyword argument for print function. causes the print return to not start a new line character.
print('World')         # end sets the character string at the end of a print function return.

print('cat', 'dog', 'mouse', sep='') # when passing multiple arguments to print, the function auto spaces the strings.
# the sep (seperate) keyword argument sets the spacing between returns in a multi argument print function return.