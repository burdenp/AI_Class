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
        self.inventory = []
        self.gold = 0
        self.job = ""
        self.tired = 100
        self.hunger = 100
        self.tiredTicker = 5

    def minus_health(self, num):
        self.health = self.health - num
        if self.health <= 0:
            quit("You've lost!")

    def lookAtInventory(self):
        return self.inventory

    def tire(self, num):
        self.tired = self.tired - num
        if self.tired < 10:
            print "I'm about to pass out..."
        elif self.tired < 20:
            print "I'm feeling sleepy..."
        elif self.tired < 50:
            print "I'm feeling  a little tired"
        elif self.tired < 90:
            if self.tiredTicker == 0:
                print "*YAWN*"
                self.tiredTicker == 5
            else:
                self.tiredTicker =- 1