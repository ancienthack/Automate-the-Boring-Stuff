# This is a guessing game.
import sys
import random
import time

# i've added extra steps to practice defining function calls and returns
def playAgain():
    answer=input('Would you like to play again, '+playerName+'?\n')
    while True:
        if answer=='yes':
            guessingGame()
        elif answer=='no':
            sys.exit('Have a great fucking day!')
        else:
            answer=input('Yes or no, please.\n')

def guessingGame():
    secretNumber=random.randint(1, 20)
    for guessTaken in range(1,6):
        guess=int(input('Pick a number between 1 and 20.\n'))
        if guess<secretNumber:
            print('Your guess is too low.')
        elif guess>secretNumber:
            print('Your guess is too high.')
        else:
            break #This is the correct guess!

    if guess==secretNumber:
        print('That is the correct number, '+playerName+'!')
        print('You guessed in '+str(guessTaken)+' guesses!')
        playAgain()
    else:
        print('Nope. The number I was thinking of was '+str(secretNumber)+'.')
        playAgain()

playerName=input('Hello. What is your name?\n')
while True:
    if playerName.isalpha():
        break
    else:
        playerName=input('Please give me your name.\n')
playerAnswer=input('Okay, '+playerName+', would you like to play a game?\n')
while True:
    if playerAnswer=='yes':
        print('Great!\nWe are going to play a guessing game!')
        guessingGame()
    elif playerAnswer=='no':
        sys.exit('Well fuck you then!')
    else:
        playerAnswer=input('This is a yes or no question, '+playerName+'.\nSo, would you like to play a game?\n')