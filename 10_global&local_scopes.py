# scope is a container of variables or area of the source code. a variable cannot be both local and global.
# global scope is created when the program starts. destroyed when the program terminates.
# local scope is created when a function is called. when a value is returned the local scope is destroyed.
# 1. code in a global scope CAN NOT use local variables.
# 2. code in a local scope CAN access global variables.
# 3. code in one function's local scope CAN NOT use variables in another local scope.
# 4. you can use the same name for different variables if they're in different scopes.

# scopes seperate functions code from the rest of the program. easier for troubleshooting.
# treat functions as black boxes

spam=42 # global variable, anything outside of a local scope

def eggs(): # each function has its own local scope
    spam=42 # local variable, anything within a specific function

print('some code here.')
print('some more code.')

###
def spam():
    global eggs # tells python that local variable is always a global variable.
    eggs='hello' # locally prints hello
    #eggs=99 # local variable. adding local assignment statements causes function to ignore global assignment statement for eggs.
    #bacon()
    print(eggs) # prints eggs=99 because the bacon() functions eggs variable is a local variable.

def bacon():
    ham=101 # local variable
    eggs=0 # local variable

eggs=42 # global variable, usable by the spam() function.
spam()
#print(eggs) # returned error because local eggs variable in spam() function is not usable in global scope without a return value.
print(eggs) # globally prints 42