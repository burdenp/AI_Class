#Gridsystem
import sys
import os
import time
from random import randint
import random
import string
import Npc
import Util

class gridSquare():
    NPCs =[]
    spots = 0
    name = ""
    def __init__(self, num, name):
        self.name = name
        self.spots = int(num)
        self.NPCs = []
    def AI(self, character):
        #does some ai stuff and populates the spots by filling spots with generated NPCs
        for i in range(self.spots):
            self.NPCs.append(Npc.NPC())
        return self
    def view_NPCs(self):
        return self.NPCs

