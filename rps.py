# File: rps.py
# Purpose:
#   To write a program that allows a user to play a single game or multiple
#   games of rock, paper, scissors with the computer.

def rps():
    from myro import *
    from random import *
    variable = ["Yes", "No"]

    playagain = "Yes"
    while(playagain == "Yes"):
        choices = ["Rock", "Paper", "Scissors"]
        computerChoice = choices[randint(0,2)]
        humanChoice = askQuestion("Make your choice:", choices)

        speak("You picked " + humanChoice)
        speak("I picked " + computerChoice)
    # To find out the winner

        computerChoice == "Paper" and humanChoice == "Rock"
        computerChoice == "Scissors" and humanChoice == "Paper"
        computerChoice == "Rock" and humanChoice == "Scissors"
    
        if (computerChoice == humanChoice):
            speak("We tied. You're off the hook this time human, but next time I'll win.")
        elif ((computerChoice == "Paper" and humanChoice == "Rock") or
              (computerChoice == "Scissors" and humanChoice == "Paper") or
              (computerChoice == "Rock" and humanChoice == "Scissors")):
            speak("I win human. You will never beat me.")
        else:
            speak("You win human. You must have gotten lucky.")

        speak("Thanks for playing. It was fun.")

        playagain = askQuestion("Care to try your luck again?", variable)

rps()
