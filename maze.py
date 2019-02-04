# File: maze.py
# Chris Eckert
# This program guides the robot to a stage, dances to a song, then sings a song.

from myro import *
init()
from random import *
# program settings

cruiseSpeed = -0.7
turnSpeed = -0.5
lightThresh = 3000

def cruise():
    return [True, cruiseSpeed, 0]

def avoid():
    L, R = getIR()
    L = 1-L
    R = 1-R
    if L:
        return [True, 0, -turnSpeed]
    elif R:
        return [True, 0, turnSpeed]
    else:
        return [False, 0, 0]

def reverse():
    if getStall():
        # I am stalled, turn
        return [True, 0, turnSpeed]
    else:
        return [False, cruiseSpeed, 0]

behaviors = [avoid, reverse, cruise]

def arbitrate():
    for behavior in behaviors:
        output, T, R = behavior()
        if output:
            return [T, R]

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

def dance():
    spin(1,9)
    shuffle(0.8,.1)
    spin2(1.0,4)
    shuffle(0.8,.1)
    beep(0.3, 600)
    beep(0.3, 650)

def song():
    beep(.5,500)
    beep(.5,500)
    beep(.5,550)
    beep(.5,600)
    beep(.5,500)
    beep(.5,600)
    beep(.5,550)
    beep(.5,400)
    beep(.5,500)
    beep(.5,500)
    beep(.5,550)
    beep(.5,600)
    beep(1.0,500)
    beep(.5,450)
    
def main():
    while timeRemaining(9):
        T, R = arbitrate()
        move(T, R)
    while timeRemaining(30):
        song()
    dance()

main()

