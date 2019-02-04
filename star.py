# File: star.py
# Purpose: To draw a five-sided star with internal angles of 36 degrees.

from myro import *

init()
    
def travelStraight(distance):
    inchesPerSec = 13
    forward(1, distance/inchesPerSec)

def degreeTurn(angle):
    turnRight(4, angle/185)

def star():
    for side in range(5):
        travelStraight(13.0)
        degreeTurn(165.0)
        
askQuestion("Click 'Yes' when you want to start", answers = ['yes'])

star()
