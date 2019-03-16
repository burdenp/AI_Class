#Game class
import sys
import os
import time
from random import randint
import random
import string
import Npc
import Player
import GridSquare
import Util
import Item
import Timer

class game():
    def __init__(self):
        gridSystem = {}
        #self.End is end game timer when end hits 0 game ends when you get to gate and you win
        self.end = 1000
        self.player = Player.player()
        #self.merchant = Npc.merchant()
        hotel = GridSquare.gridSquare(1, "Hotel").AI(self.player)
        northMarket = GridSquare.gridSquare(2, "North Market").AI(self.player)
        tavern = GridSquare.gridSquare(3, "Tavern").AI(self.player)
        gate = GridSquare.gridSquare(4, "Gate").AI(self.player)
        marketCenter = GridSquare.gridSquare(5, "Market Center").AI(self.player)
        dock = GridSquare.gridSquare(6, "Dock").AI(self.player)
        capital = GridSquare.gridSquare(7, "Capital").AI(self.player)
        southMarket = GridSquare.gridSquare(8, "South Market").AI(self.player)
        shanty = GridSquare.gridSquare(9, "Shanty Town").AI(self.player)
        self.gridSystem = {"hotel":hotel,
            "north market":northMarket,
            "tavern":tavern,
            "gate":gate,
            "market center":marketCenter,
            "dock": dock,
            "capital":capital,
            "south market":southMarket,
            "shanty town":shanty}
        self.location = gate



    #start game by choosing the name and class of your character
    def chooseYourCharacter(self):
        while True:
            self.player.name = raw_input("Create the name of your character: ").strip()
            print
            while True:
                    sure = Util.cleanInput("Your name is " + self.player.name + " Are you sure?: ")
                    print
                    if Util.yesHuh(sure):
                        break
                    elif Util.noHuh(sure):
                        Util.gamePrint("restarting")
                        self.chooseYourCharacter()
                    else:
                        print "Please enter yes or no"
                        print
            print "Pick a Class:"
            print
            while True:
                action = Util.cleanse(raw_input("Thief, Fighter, Mage: "))
                print
                if action == "thief" or action == "t":
                    self.player.job = "thief"
                    self.player.inventory = []
                    self.player.inventory.append(Item.knife())
                    break
                if action == "fighter" or action == "f":
                    self.player.job = "fighter"
                    self.player.gold = 50
                    self.player.inventory = []
                    self.player.inventory.append(Item.sword())
                    break
                if action == "mage" or action == "m":
                    self.player.job = "mage"
                    self.player.gold = 150
                    self.player.inventory = []
                    self.player.inventory.append(Item.staff())
                    break
                else:
                    print "Not an Option"
                    print
            break
    #would you like to see the list of items in your inventory?
    def showInventory(self):
        while True:
                print "Your current inventory is: " + str(self.player.inventory) + "."
                print "You can continue adding to your inventory" + " as your adventure continues"
                print
                break
#builds the map functionality
#returns the directions that the player can move in
    def map(self):
        if self.location ==  self.gridSystem.get("hotel"):
            return ["south", "east"]
        if self.location == self.gridSystem.get("north market"):
            return ["south", "east", "west"]
        if self.location == self.gridSystem.get("tavern"):
            return ["south", "west"]
        if self.location == self.gridSystem.get("gate"):
            return ["north", "south", "east"]
        if self.location == self.gridSystem.get("market center"):
            return ["north", "south", "east", "west"]
        if self.location == self.gridSystem.get("dock"):
            return ["north", "south", "west"]
        if self.location == self.gridSystem.get("capital"):
            return ["north", "east"]
        if self.location == self.gridSystem.get("south market"):
            return ["north", "east", "west"]
        if self.location == self.gridSystem.get("shanty town"):
            return ["north", "west"]
    #if statements to move between gridSquares
    def move(self, direction):
        if (self.location == self.gridSystem.get("hotel") and direction == "south") \
           or (self.location == self.gridSystem.get("capital") and direction == "north") \
           or (self.location == self.gridSystem.get("market center") and direction == "west"):
            self.location = self.gridSystem.get("gate")
        elif (self.location == self.gridSystem.get("gate") and direction == "north") \
           or (self.location == self.gridSystem.get("north market") and direction == "west"):
            self.location = self.gridSystem.get("hotel")
        elif (self.location == self.gridSystem.get("hotel") and direction == "east") \
           or (self.location == self.gridSystem.get("tavern") and direction == "west") \
           or (self.location == self.gridSystem.get("market center")  and direction == "north"):
            self.location = self.gridSystem.get("north market")
        elif (self.location == self.gridSystem.get("north market")and direction == "east") \
           or (self.location == self.gridSystem.get("dock") and direction == "north"):
            self.location = self.gridSystem.get("tavern")
        elif (self.location == self.gridSystem.get("north market") and direction == "south") \
           or (self.location == self.gridSystem.get("south market") and direction == "north") \
           or (self.location == self.gridSystem.get("dock") and direction == "west") \
           or (self.location == self.gridSystem.get("gate") and direction == "east"):
            self.location = self.gridSystem.get("market center") 
        elif (self.location == self.gridSystem.get("tavern") and direction == "south") \
           or (self.location == self.gridSystem.get("shanty town") and direction == "north") \
           or (self.location == self.gridSystem.get("market center") and direction == "east"):
            self.location = self.gridSystem.get("dock")
        elif (self.location == self.gridSystem.get("gate") and direction == "south") \
           or (self.location == self.gridSystem.get("south market") and direction == "west"):
            self.location = self.gridSystem.get("capital")
        elif (self.location == self.gridSystem.get("market center") and direction == "south") \
           or (self.location == self.gridSystem.get("capital") and direction == "east") \
           or (self.location == self.gridSystem.get("shanty town") and direction == "west"):
            self.location = self.gridSystem.get("south market")
        elif (self.location == self.gridSystem.get("dock") and direction == "south") \
           or (self.location == self.gridSystem.get("south market") and direction == "east"):
            self.location = self.location = self.gridSystem.get("shanty town")
        else: print "Error none worked"

    #ready to begin adventure?
    def proceedToAdventure(self):
        myList = ["Show Inventory", "Choose a character", "Proceed"]
        while True:
            proceed = Util.cleanInput("Would you like to proceed?: ")
            print
            if Util.yesHuh(proceed):
                break
            elif Util.noHuh(proceed):
                while True:
                    print myList
                    goBack = Util.cleanInput("Where would you like to go back?: ")
                    print
                    if goBack == Util.cleanse("Show Inventory") or goBack == Util.cleanse("Inventory"):
                        self.showInventory()
                        self.proceedToAdventure()
                        break
                    elif goBack == Util.cleanse("Choose a character") or goBack == Util.cleanse("Character"):
                        self.chooseYourCharacter()
                        self.proceedToAdventure()
                        break
                    elif Util.cleanse("Proceed") == goBack:
                        break
                    else:
                        print "Not in the menu. Please select an action from this list: " + str(myList)
                break
            else:
                print "Please type yes or no"

    def actions(self):
        while True:
            Util.gamePrint("You see " + str(self.location.spots) + " people in the " + self.location.name)
            Util.gamePrint(self.location.view_NPCs())
            Util.gamePrint("You can interact with any of them or you can move to a new location" +"\n" \
                + " or you can examine yourself or your inventory")
            action = Util.cleanInput("What do you do?: ")
            if action == "inventory" or action == "i":
                self.showInventory()
            action = Util.fullDirection(action)
            if action in self.map():
                tmp = Util.cleanInput("Are you sure you want to go " + action + "?: ")
                if Util.yesHuh(tmp):
                    self.move(action)
                    self.actions()
                if Util.noHuh(tmp):
                    Util.gamePrint("Alright then ")
            for x in self.gridSystem.get(Util.cleanse(self.location.name)).view_NPCs():
                if x.compare(action):
                    Util.gamePrint(x.view_Actions())
                    Util.gamePrint("Here is a list of interactions with the NPC: " + action)
                    choice = Util.cleanInput("What do you want to do?: ")
                    for y in x.view_Actions():
                        if choice == y:
                            x.do(choice, self.player)
                    #implement actions

                    break
                #when the choice doesn't match to an option
                #needs to bumb back up to the printed list of npcs and re ask for an NPC
            else:
                print "Not an acceptable choice try again"
                print
                self.actions()

    #runs game
    def run(self):
        self.chooseYourCharacter()
        while True:
            show_Inventory = Util.cleanInput("Would you like to view your inventory?: ")
            print
            if Util.yesHuh(show_Inventory):
                self.showInventory()
                break
            elif Util.noHuh(show_Inventory):
                print "Very well. "
                print
                break
            else:
                print "Please type yes or no"
        self.proceedToAdventure()
        Util.gamePrint("Your adventure begins now" +" "+  self.player.name + " the " + self.player.job)
        while self.end > 0 or self.location != self.gridSystem.get("gate"):
            self.actions()
            break
        print "game over, exited through the front"

game().run()

