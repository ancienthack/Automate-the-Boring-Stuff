# a divide-by-zero error happpens when Python divides a number by zero.
# errors cause the program to crash.
# an error that occurs in a try block will cause code in the except block to execute. that code can handle the error or display a message to the user so that the program can keep going.

def div42by(divideBy):
    try:
        return 42/divideBy
    except ZeroDivisionError: # returns None data type and skips the error. you don't have to specify the type pf error; a simple except: will skip all errors.
        print('Error: You tried to divide by zero.')


print(div42by(2))
print(div42by(12))
print(div42by(0)) # dividing by zero is what causes the error in this example
print(div42by(1))


print('How many cats do you have?')
while True:
    numCats=input()
    try:
            if int(numCats)>=4:
                print('That is a lot of cats')
                break
            elif int(numCats)<0:
                print('Does that mean you have killed cats?')
                break
            else:
                print('That is not that many cats.')
                break
    except ValueError:
        print('You did not enter a number.')
