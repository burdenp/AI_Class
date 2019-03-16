#Gridsystem
import sys
import os
import time
import random
import string
import Npc
import Util
import Player
import Item

global ITEMS
ITEMS = [Item.sword(), Item.staff(), Item.axe(), Item.potion(), Item.scroll(), Item.knife(), 
        Item.spear(), Item.shield(), Item.potion(5), Item.scroll(5), Item.potion(10), Item.scroll(10),
        Item.spice(), Item.spice(5), Item.spice(2), Item.spice(3), Item.spice(4), Item.potion(15),
        Item.scroll(15)]

global PEOPLE
PEOPLE =  [Npc.merchant(), Npc.dockhand(), Npc.peasant(), Npc.guard(), Npc.royalty(), Npc.wizard(),
           Npc.highMerchant(), Npc.cleric(), Npc.cultist()]

class gridSquare():
    NPCs =[]
    spots = 0
    name = ""
    def __init__(self, num, name):
        self.name = name
        self.spots =int(num)
        self.NPCs = []
    def AI(self, player):
        #does some ai stuff and populates the spots by filling spots with generated NPCs
        AIScore = 1
        self.NPCs = []
        openSpots = self.spots
        data = player.score()
        if self.name == "Hotel" or self.name == "Tavern":
            openSpots = openSpots - 1
        #large amount of AI balancing is in this line
        AIScore = AIScore + data[0] * 3/(openSpots + 1) * data[2]/100.0 + 500/(data[3]+1)
        if self.name == "Shanty Town" or self.name == "Capital":
            openSpots = openSpots - 1
            AIScore = AIScore / 4
        if self.name == "Center Market":
            AIScore = AIScore * 1.5
        if openSpots > 4:
            openSpots = openSpots - 1
            self.NPCs.append(random.choice(PEOPLE))
        if openSpots > 0:
            for i in range(openSpots):
                if AIScore <= 30:
                    self.NPCs.append(self.itemAssigner(Npc.peasant(), player))
                if AIScore <= 65:
                    self.NPCs.append(random.choice([self.itemAssigner(Npc.guard(), player),
                     Npc.peasant()]))
                elif AIScore <= 105:
                    self.NPCs.append(random.choice([self.itemAssigner(Npc.merchant(), player),
                     self.itemAssigner(Npc.dockhand(), player), Npc.guard()]))
                elif AIScore <= 150:
                    self.NPCs.append(random.choice([self.itemAssigner(Npc.merchant(), player),
                     Npc.dockhand(), Npc.wizard()]))
                elif AIScore <= 200:
                    self.NPCs.append(random.choice([Npc.highMerchant(), Npc.merchant(), Npc.wizard]))
                elif AIScore <= 300:
                    if NPC.cleric in NPCs:
                        self.NPCs.append(random.choice([Npc.highMerchant, Npc.cultist]))
                    else:   
                        self.NPCs.append(random.choice([Npc.highMerchant, Npc.cleric]))
        if self.name == "Hotel":
                self.NPCs.append(Npc.innkeeper())
        elif self.name == "Tavern":
                self.NPCs.append(Npc.barKeep())
        elif self.name == "Capital":
                self.NPCs.append(Npc.royalty())
        elif self.name == "Shanty Town":
                self.NPCs.append(Npc.peasant())
        self.healthAssigner(player)
        return self
    #only returns alive NPC's
    def view_NPCs(self):
        alive = []
        for npc in self.NPCs:
            if npc.health >= 0:
                alive.append(npc)
        return alive
    #Ai helper function for AI in gridsystem
    #given a value, ie weight, generates a set of items that gets closest to the number possible
    def generatelist(self, num):
        temp = []
        tempItems = []
        tempItems = ITEMS
        #generates random segments of possible inventories based on common items
        for i in range(30):
            random.shuffle(tempItems)
            temp.append(tempItems[0:5])
        for i in range(30):
            random.shuffle(tempItems)
            temp.append(tempItems[0:4])
        for i in range(30):
            random.shuffle(tempItems)
            temp.append(tempItems[0:3])
        for i in range(30):
            random.shuffle(tempItems)
            temp.append(tempItems[0:2])
        for i in range(30):
            random.shuffle(tempItems)
            temp.append(tempItems[0:1])
        tmp2 = []
        #for each possible inventory
        for x in temp:
            add = 0
            for y in x:
                #calculate the value of the inventory
                add = y.value + add
            #save the total value of an inventory
            tmp2.append(add)
        #for each total value remove our num
        for e in tmp2:
            e = num - e
        #location in list
        loc = 0
        #distance from target looking for small distance
        dist = float('inf')
        for i in range(len(tmp2)):
            if i >= 0:
                if tmp2[i] <= dist:
                    dist = tmp2[i] 
                    loc = i
        return temp[loc]
    #connected to generatelist
    #other AI function is the item assigner   
    def itemAssigner(self, NPC, player):
        #player.score
        #first is score, second is health, 3rd is how tired, 4th is how close to end
        difficulty = player.score()
        difficulty[0]
        NPC.inventory = self.generatelist(difficulty[0])
        return NPC

    def healthAssigner(self, player):
        healthMax = int(player.score()[1] * 1.3)
        healthMin = int(player.score()[1] * .3)
        for npc in self.NPCs:
            npc.health = random.choice(range(healthMin, healthMax + 1, 1))
