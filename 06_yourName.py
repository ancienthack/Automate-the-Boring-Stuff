name=''
while name != 'your name': # while loop continually checks until the condition is met. jumps back to start to re-check the condition.
    print('Please type your name.')
    name=input()
print('Thank you!')

while True:
    print('Please type your name.')
    name=input()
    if name=='your name':
        break # if the break statement is executed it jumps out of the while loop and continues with the rest of the code.
print('Thank you!')

spam=0
while spam<5:
    spam+=1
    if spam==3:
        continue # when continue statment is executed it immediately jump back to the start of the while loop to re-check condition.
                 # this skips over the print function for the iteration of the loop.
    print('spam is '+str(spam))