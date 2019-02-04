# File: moves.py
# Purpose: To make robot dance to Apache.

from myro import *
init()


# Define the new behaviors
def hold(speed, waitTime):
    forward(speed, waitTime)
    stop()

def spin(speed, waitTime):
    turnRight(speed, waitTime)
    stop()

def shuffle(speed, waitTime):
    turnLeft(speed, waitTime)
    turnRight(speed, waitTime)
    turnRight(speed, waitTime)
    turnLeft(speed, waitTime)
    turnLeft(speed, waitTime)
    turnRight(speed, waitTime)
    stop()

def spin2(speed, waitTime):
    turnLeft(speed, waitTime)
    stop()

# Define a function to utilize these behaviors
def dance():
    hold(0,16)
    spin(1,9)
    shuffle(.8,.5)
    spin2(.5,4)
    shuffle(.8,.5)
    spin2(.5,4)
    shuffle(.8,.5)
    spin2(.5,4)
    shuffle(.8,.5)
    spin2(.5,4)

