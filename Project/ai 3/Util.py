#Util class
import sys
import os
import time
from random import randint
import random
import string


#helper for input functions instead of having to call .trip.lower all the time
def cleanse(string):
    return str(string).strip().lower()
#helper for yes input booleans is safe for non clensed answers in case of mistake
def yesHuh(string):
    return cleanse(string) == "yes" or cleanse(string) == "y"
 #helper for no input booleans is safe for non cleansed answers in case of mistake
def noHuh(string):
    return cleanse(string) == "no" or cleanse(string) == "n"
def cleanInput(string):
	tmp = cleanse(raw_input(string))
	print
	return tmp
def gamePrint(string):
	print string
	print
def fullDirection(string):
	if string == "n":
		return "north"
	elif string == "s":
		return "south"
	elif string == "e":
		return "east"
	elif string == "w":
		return "west"
	return string