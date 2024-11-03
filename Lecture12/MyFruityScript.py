#!/usr/bin/python3
# Script to compare fruit
import os
import sys
# Allow for two fruit
# Error traps here for wrong input format

if len(sys.argv) != 3:
	print("Correct usage: python3 MyFruityScript.py <fruit1> <fruit2>\nTo compare two furits of your choice")
	sys.exit(1)

first_fruit  = sys.argv[1].lower()
second_fruit = sys.argv[2].lower()

# Standard unchanging answer output
# NOTE_incomplete: a lot more could be done here...!
print(first_fruit.upper() + " are just as nice as " + second_fruit.upper())
