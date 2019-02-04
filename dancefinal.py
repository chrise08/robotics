# Dance for end of final presentation

from myro import *
init()

def spin(speed, waitTime):
    turnRight(speed, waitTime)
    stop()

def shuffle(speed, waitTime):
    turnLeft(speed, waitTime)
    forward(speed, waitTime)
    backward(speed, waitTime)
    forward(speed, waitTime)
    backward(speed, waitTime)
    turnRight(speed, waitTime)
    forward(speed, waitTime)
    backward(speed, waitTime)
    forward(speed, waitTime)
    backward(speed, waitTime)
    turnRight(speed, waitTime)
    forward(speed, waitTime)
    backward(speed, waitTime)
    forward(speed, waitTime)
    backward(speed, waitTime)
    turnLeft(speed, waitTime)
    forward(speed, waitTime)
    backward(speed, waitTime)
    forward(speed, waitTime)
    backward(speed, waitTime)
    turnLeft(speed, waitTime)
    forward(speed, waitTime)
    backward(speed, waitTime)
    forward(speed, waitTime)
    backward(speed, waitTime)
    turnRight(speed, waitTime)
    forward(speed, waitTime)
    backward(speed, waitTime)
    forward(speed, waitTime)
    backward(speed, waitTime)
    stop()

def spin2(speed, waitTime):
    turnLeft(speed, waitTime)
    stop()

# Define a function to utilize these behaviors
def dance():
    spin(1,9)
    shuffle(.8,.5)
    spin2(.5,4)
    shuffle(.8,.5)
    beep(0.3, 600)
    beep(0.3, 650)
dance()

