# File: stall.py
# Purpose:
#   To write a program that causes the robot to do something until it senses
#   a stall in it's behavior.

from myro import *

init()

while not getStall():
    forward(1.0)

stop()

speak("Ouch! I think I bumped into something!")
