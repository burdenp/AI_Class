#NPC Class and subclasses

import sys
import os
import time
from random import randint
import random
import string
import Player
import Util
import Item

#list of names to use for NPC's
#helps keep player track of them in game

global names
names = ["Adam", "Alice", "Alex", "Andrew", "Ashley", "Alfred", "Barry", "Ben", "Blake", "Bob",
          "Bill", "David", "Patrick", "Jamel", "Kevin", "Tony", "Doug", "Paul",
          "Carl", "Cindy", "George", "Greg", "John", "Jake", "Jack", "Steve", "Sarah"]



#NPC
class NPC():
  def __init__(self):
    self.name = random.choice(names)
    self.health = 0
    self.inventory = [Item.sword()]
    self.interactions = ["buy", "sell", "talk", "examine", "hunt"]
    self.weight = 0
    self.gold = 100

  def npcType(self):
      return "NPC "
  def __str__(self):
      return self.npcType() + self.name
  def __repr__(self):
      return self.npcType() + self.name
  #view list of actions an NPC has
  def view_Actions(self):
    return self.interactions
  #compare function to compare input string versus a npc
  def compare(self, str):
      if Util.cleanse(str) == Util.cleanse(self.npcType()\
       + self.name) or Util.cleanse(str) == Util.cleanse(self.name):
          return True
      else:
          return False
  #function that turns inputted string into actions that are defined lower
  def do(self, string, player):
          if string == "buy": self.buy(player)
          if string =="sell": self.sell(player)
          if string == "examine": self.examine(player)
          if string == "hunt": self.hunt(player)
  def buy(self, player):
    while True:
        Util.gamePrint("enter q, quit, or back to leave")
        Util.gamePrint(self.name + "'s inventory is " + str(self.inventory))
        item = Util.cleanInput("you have " + str(player.gold) + " gold. what would you like to buy?: ")
        if item == "back" or item == "b" or item == "quit" or item == "q":
          break
        for x in self.inventory:
          if x.compare(item):
            Util.gamePrint(item + "costs " + str(x.value) +" gold")
            tmp = Util.cleanInput("Do you want to spend that much?: ")
            if Util.yesHuh(tmp):
              if player.gold >= x.value:
                  player.inventory.append(x)
                  player.gold = player.gold - x.value
                  self.gold = self.gold + x.value
                  break
              else: Util.gamePrint("You can't afford that")
            if Util.noHuh(tmp):
              break



  def sell(self, player):
    while True:
        Util.gamePrint("enter q, quit, or back to leave")
        Util.gamePrint("you have" + str(player.inventory) + " in your inventory")
        item = Util.cleanInput(self.name + " has " + str(self.gold) + " gold. What do you want to sell?: ")
        if item == "back" or item == "b" or item == "quit" or item == "q":
            break
        for x in player.inventory:

          ####CURRENT ERROR IS HERE YPER ERROR UNBOUND METHOD COMPARE() MUST
          ##### BE CALLED WITH STAFF INSTANCE AS FIRST ARGUMENT (got str instance instead)
          if x.compare(item):
            Util.gamePrint(item + "costs " + str(x.value) + " gold")
            tmp = Util.cleanInput("Do you want to sell it for that much?: ")
            if Util.yesHuh(tmp):
              if self.gold >= x.value: 
                  player.inventory.remove(x)
                  player.gold = player.gold + x.value
                  self.gold = self.gold - x.value
                  break
              else: Util.gamePrint(self.name + " can't afford that")
            if Util.noHuh(tmp):
              break

  def examine(self, player):
      randomHealth = random.randint(1, 100)
      randomList = ["grass", "food", "enemey", "bench"]
      Attack = ["attack", "kill"]
      randomAttack = random.choice(Attack)
      randomItem = random.choice(randomList)
      print (str(player.name) + " is examining his surrounding")
      if randomItem == "grass":
          print "There is nothing but plain grass"
      elif randomItem == "food":
          while True:
              food = Util.cleanInput(("There is food on the table. Eat? "))
              if Util.yesHuh(food):
                  print "You recovered some health"
                  a = player.health+10
                  break
              elif Util.noHuh(food):
                  print "Not hungry I suppose"
                  break
              else:
                  print "Type yes or no"
      elif randomItem == "enemey":
          proceed = Util.cleanInput(("There is a mysterious dark shadow on your left. Examine? "))
          if Util.yesHuh(proceed):
              print str(player.name) + " is approaching the figure"
              print
              print "It's " + str(merchants.name) + " the merchant!"
              while True:
                  attack = Util.cleanInput(("Attack? "))
                  if Util.yesHuh(attack):
                      hit = merchants.health -randomHealth
                      print str(player.name) + " attatcked. " +  str(merchants.name) + " health took a hit  "
                      print Util.cleanse(str(merchants.name) + " decided it wasn't worth fighting and got away")
                      break
                  elif Util.noHuh(attack):
                      print str(player.name) + " cowardly runs away"
                      break
                  else:
                      print "type yes or no"
          elif Util.noHuh(proceed):
              print str(player.name) + " chose not to approach the figure"
      elif randomItem == "bench":
          while True:
              rest = Util.cleanInput("There is an bench. Take a rest? ")
              if Util.yesHuh(rest):
                  increaseHealth = player.health + 100
                  print str(player.name) + " decided to take a rest. " + str(player.name) + " made a full recovery"
                  return increaseHealth
              elif Util.noHuh(rest):
                  print str(player.name) + " decided not to take a rest"
                  break
              else:
                  print "type yes or no"



  def hunt(self, player):
      animals = ["pig", "rabbit", "boar", "none"]
      Attack = ["attack", "kill"]
      randomAttack = random.choice(Attack)
      randomAnimal = random.choice(animals)
      print str(player.name) + " decided to hunt"
      if randomAnimal == "pig":
              print "There is a pig "
              print
              print str(player.name) + " hunts the pig"
              myHealth = player.health + 15
              print "Your health increased after eating the pig"
              print
              return myHealth
      elif randomAnimal == "boar":
              while True:
                  damage = Util.cleanInput("There is a boar. This is a big animal and it could attack. Do you still want to hunt it? ")
                  if Util.yesHuh(damage):
                      if randomAttack == "attack":
                          characterHealth = player.health - 10
                          print "The boar attacks and has done some damage"
                          print
                          print "You are hurt and can't attack back. The boar ran away"
                          print
                          return characterHealth
                      elif randomAttack == "kill":
                          print "One shot kill"
                          characterHealth = player.health + 10
                          print "You have increased your health"
                          print
                          return characterHealth
                  elif Util.noHuh(damage):
                      print "You decided not to hunt the boar"
                      break
                  else:
                      print "type yes or no"

      elif randomAnimal == "none":
              print "There is nothing to hunt! Better luck next time"









class merchant(NPC):
    def __init__(self):
        self.name = random.choice(names)
        self.health = 100
        self.inventory = ["sword", "shield", "clothing"]
        self.interactions = ["buy", "sell", "talk", "attack", "examine"]
        self.gold = 200
    def npcType(self):
        return "Merchant "

class guard(NPC):
    def __init__(self):
        self.name = random.choice(names)
        self.health = 200
        self.inventory = ["sword", "shield", "knife"]
        self.interactions = ["talk", "attack", "examine"]
        self.weight = 1
        self.gold = 100
    def npcType(self):
        return "Guard "
class innkeeper(NPC):
    def __init__(self):
      self.name = random.choice(names)
      self.health = 50
      #innkeeper has bed/rest that refills player's tired meter
      self.inventory = ["Bed/Rest"]
      self.interactions = ["Talk", "attack", "examine", "buy", "sell"]
      self.gold = 250
#class wizard(NPC):
 #   def __init__(self):

merchants = merchant()
