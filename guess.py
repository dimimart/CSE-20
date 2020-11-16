# assignment: programming assignment 2
# author: Diana Martinez
# date: 11/02/2020
# file: guess.py is an interactive game that asks the user to guess a number from 1 to 10
# input: only integers from 1 to 10
# output: interactive messages

import random

check = False #initializing boolean and counter index

print("Play a game: Guess My Number. \nYou have three attempts to guess my number.")

while not check: #while check == false simplified
    randomNumber = random.randint(1, 10)  # will generate random number between 1 & 10

    for index in range(3):
        guess = int(input("Please enter a number from 1 to 10: "))

        if guess == randomNumber:
            print("You guessed right. My number is " + str(guess) + ". Congratulations you won!")
            playAgain = input("Would you like to play again[Y/N]?")
            if playAgain in ("N", "n"):
                check = True
                #ends game after first try
            else:
                randomNumber = random.randint(1, 10)  # will generate random number between 1 & 10
                index = 0
                #restarts game

        else: #firstGuess != randomNumber
            if guess > randomNumber:
                print("You guessed wrong. Your number is bigger than mine.")
            elif guess < randomNumber:
                print("You guessed wrong. Your number is smaller than mine.")

        if guess != randomNumber and index == 2:
            print("Sorry, you lost. My number is ", randomNumber)
            playAgain = input("Would you like to play again[Y/N]?")
            if playAgain in ("N", "n"):
                check = True
                #ends game after first try
            else:
                randomNumber = random.randint(1, 10)  # will generate random number between 1 & 10
                index = 0
                #restarts game

print("Goodbye!")