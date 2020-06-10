def playerName():
    playerName=input('Hello. What is your name?\n')
    while True:
        if playerName.isalpha():
            return playerName
        else:
            playerName=input('Please give me your name.\n')

playerName=playerName()
print('Your name is '+playerName+'.')