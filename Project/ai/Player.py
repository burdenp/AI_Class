#Player class
import sys
import os
import time
from random import randint
import random
import string
import Util
import Item

#create your player
class player:
    def __init__(self):
        self.health = 100
        self.name = ""
        self.inventory = [Item.potion(5)]
        self.gold = 200
        self.job = ""
        self.tired = 100
        self.tiredTicker = 5
        self.end = 500
        self.magic = 0

    def tire(self, num):
        self.tired = self.tired - num
        if self.tired < 10:
            print "You are about to pass out..."
            print
        elif self.tired < 20:
            print "You are feeling sleepy..."
            print
        elif self.tired < 50:
            print "You are feeling tired"
            print
        elif self.tired < 90:
            if self.tiredTicker == 0:
                print "*YAWN*"
                print
                self.tiredTicker = 5
            else:
                self.tiredTicker = self.tiredTicker - 1
    def printOut(self):
        print "you look down at yourself"
        print "your name is " + str(self.name)
        print "you have " + str(self.health) + " health"
        print "you have " + str(self.inventory) + " in your inventory"
        print "you have " + str(self.gold) + " gold"
        print "you are a " + str(self.job)
        if self.tired < 10:
            print "you are about to pass out"
        elif self.tired < 20:
            print "you are feeling very sleepy"
        elif self.tired < 50:
            print "you are feeling tired"
        elif self.tired < 70:
            print "you are feeling energetic"
        elif  self.tired < 90:
            print "You are feeling great"
        if self.end <= 0:
            print "You can leave the city when you want to just go to the gate to win"
        else:
            print "There is " + str(self.end) + " time left till you can leave the city"
        print "Your score is " + str(self.score()[0])
        print
    #function to balance for the power of the player
    #information for AI, difficulty settings and such
    def score(self):
        score = (1/2 * self.health + self.gold) * (self.magic/10.0 + 1)
        for x in self.inventory:
            score = score + x.value
        #first is score, second is health, 3rd is how tired, 4th is how close to end
        return [score, self.health, self.tired, self.end]