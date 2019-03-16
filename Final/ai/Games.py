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


class game():
    def __init__(self):
        gridSystem = {}
        self.player = Player.player()
        hotel = GridSquare.gridSquare(2, "Hotel").AI(self.player)
        northMarket = GridSquare.gridSquare(5, "North Market").AI(self.player)
        tavern = GridSquare.gridSquare(3, "Tavern").AI(self.player)
        gate = GridSquare.gridSquare(3, "Gate").AI(self.player)
        marketCenter = GridSquare.gridSquare(8, "Market Center").AI(self.player)
        dock = GridSquare.gridSquare(5, "Dock").AI(self.player)
        capital = GridSquare.gridSquare(5, "Capital").AI(self.player)
        southMarket = GridSquare.gridSquare(6, "South Market").AI(self.player)
        shanty = GridSquare.gridSquare(4, "Shanty Town").AI(self.player)
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
            while True:
                self.player.name = raw_input("Choose the name of your character: ").strip()
                print
                sure = Util.cleanInput("Your name is " + self.player.name + ". Are you sure?: ")
                print
                if Util.yesHuh(sure):
                    break
                if Util.noHuh(sure):
                    Util.gamePrint("restarting")
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
                    self.player.gold = 100 + self.player.gold
                    self.player.inventory = []
                    self.player.inventory.append(Item.knife())
                    break
                if action == "fighter" or action == "f":
                    self.player.job = "fighter"
                    self.player.gold = 50 + self.player.gold
                    self.player.inventory = []
                    self.player.inventory.append(Item.sword())
                    break
                if action == "mage" or action == "m":
                    self.player.job = "mage"
                    self.player.gold = 150 + self.player.gold
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
                data = Util.cleanInput("type q, or quit or back to go back or type in an item to see it's stats: ")
                if data == "q" or data == "quit" or data == "back" :
                    break
                for x in self.player.inventory:
                    if data == str(x):
                        x.printOut()
                        if x == Item.potion():
                            response = Util.cleanInput("Would you like to drink one?: ")
                            if Util.yesHuh(response):
                                if x.num > 1:
                                    x.num = x.num - 1
                                else: self.player.inventory.remove(x)
                                self.player.health = self.player.health + 50
                        elif x == Item.spice():
                            response = Util.cleanInput("Would you like to taste it?: ")
                            if Util.yesHuh(response):
                                if x.num > 1:
                                    x.num = x.num - 1
                                else: self.player.inventory.remove(x)
                                self.player.health = self.player.health + 25
                                self.player.magic = self.player.magic + 1
                                print "you begin to feel more magical"
                        elif x == Item.scroll():
                            response = Util.cleanInput("Would you like to read it? ")
                            if Util.yesHuh(response):
                                if x.numm > 1:
                                    x.num = x.num -1
                                else: self.player.inventory.remove(x)
                                self.player.magic = self.player.magic + 5
                                print "you feel much more magical"

                        else: raw_input("Enter any key to move back: ")
                

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
            #win condition
            choice = False
            if self.player.end <= 0 and self.location == self.gridSystem.get("gate"):
                win = Util.cleanInput("Do you want to leave the city? (ends game): ")
                if Util.yesHuh(win):
                    choice = True
                    return True
            if self.player.health <= 0:
                choice = True
                print "You are dead"
                return False
                break
            if self.player.tired <= 0:
                choice = True
                print"you've become unconscious"
                Util.gamePrint("You awake in the shanty town missing your gold and hurting")
                self.player.gold = 0
                self.player.health - 30
                self.location = self.gridSystem.get("shanty town")
                self.player.tired = 50
            if self.player.end % 80 == 0:
                self.repopulate()
            Util.gamePrint("You see " + str(len(self.location.view_NPCs())) +
                             " people in the " + self.location.name)
            Util.gamePrint("They are " + str(self.location.view_NPCs()))
            Util.gamePrint("Directions you could move in " + str(self.map()))
            Util.gamePrint("You can interact with any of them or you can move to a new location" + "\n" \
                + " or you can examine yourself or your inventory")
            action = Util.cleanInput("What do you do?: ")
            action = Util.fullDirection(action)
            if action == "inventory" or action == "i":
                self.showInventory()
                choice = True
                break
            elif action in self.map():
                tmp = Util.cleanInput("Are you sure you want to go " + action + "?: ")
                if Util.yesHuh(tmp):
                    self.move(action)
                    self.player.tire(10)
                    self.player.end = self.player.end - 10
                    self.actions()
                    choice = True
                    break
                if Util.noHuh(tmp):
                    Util.gamePrint("Alright then ")
                    choice = True
            elif action == "examine" or action == "self":
                self.player.printOut()
                choice = True
            for x in self.gridSystem.get(Util.cleanse(self.location.name)).view_NPCs():
                if x.compare(action):
                    while x.health >= 0:
                        Util.gamePrint(x.view_Actions())
                        Util.gamePrint("Here is a list of interactions with the " + str(x))
                        choice = Util.cleanInput("What do you want to do?: ")
                        if choice == "quit" or choice == "q" or choice == "back":
                            break
                        for y in x.view_Actions():
                            if choice == y:
                                x.do(choice, self.player)
                                self.player.tire(10)
                                self.player.end = self.player.end - 10
                                choice = True
                                break
                    break
                #when the choice doesn't match to an option
                #needs to bumb back up to the printed list of npcs and re ask for an NPC
            if not choice:
                print "Not an acceptable choice try again"
                print

    def repopulate(self):
        for key, value in self.gridSystem.iteritems():
            if value != self.location:
                value.AI(self.player)


    def quit(self, b):
        if b:
            print "game over, exited through the front you win"
            sys.stdout.flush()
            sys.exit()
        else:
            print "you lose"
            sys.stdout.flush()
            sys.exit()

    #runs game
    def run(self):
        self.chooseYourCharacter()
        while True:
            show_Inventory = Util.cleanInput("Would you like to view your inventory?: ")
            print
            if Util.yesHuh(show_Inventory):
                self.showInventory()
            elif Util.noHuh(show_Inventory):
                print "Very well. "
                print
                break
            else:
                print "Please type yes or no"
        self.proceedToAdventure()
        Util.gamePrint("Your adventure begins now" +" "+  self.player.name + " the " + self.player.job)
        while self.player.end > 0 or self.location != self.gridSystem.get("gate"):
            while not self.quit(self.actions()):
                break
game().run()
