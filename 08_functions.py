# to use Standard Libaray modules and their functions, you must import the module.
# importing modules gives access to new functions

# import multiple modules by seperating with commas
import random, sys, os, math
# type module name followed by a period and then the function name. This tells Python to look at that module for the function call.
random.randint(1,10)
# can use a 'from module import' to avoid the above note.
from random import * # imports entire library to bypass identifier when calling function.

# can install third-party modules using the pip tool
# on windows: python -m pip install --user **name of module**
import pyperclip # has copy and paste functions for readung and writing text to the clipboard.

#print() print function
#input() input function
#len() length function

print('Hello.')
#sys.exit() # never goes beyond this point. exits the program at this point.
print('Goodbye.')
pyperclip.copy('General Kenobi')
print()

pyperclip.paste()
