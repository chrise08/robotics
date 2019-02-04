# File: game.py
# Purpose:
# To write a program that allows a user to play a guessing game with the
# computer.

from myro import *

from random import *

def game():
    askQuestion("Click 'Play' when you are ready", answers = ['play'])
    
    print("I'm thinking of a number between 1 and 20. Can you guess what it is?")
   
    humanNumber = input("Enter your guess: ")
    computerNumber = randint(1,20)
   
    while humanNumber != computerNumber:
        if (humanNumber < computerNumber):
            speak("Your guess was too low")
        else:
            speak("Your guess was too high")
       
        humanNumber = input("Enter your guess: ")

    if humanNumber == computerNumber:
        speak("Congratulations! You win!")
        askQuestion("Would you like to play again?")
        True = game()

game()
