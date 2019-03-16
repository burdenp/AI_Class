#NPC Class and subclasses

import sys
import os
import time
import random
import string
import Player
import Util
import Item
import math

#list of names to use for NPC's
#helps keep player track of them in game

global NAMES
NAMES = ["Adam", "Alice", "Alex", "Andrew", "Ashley", "Alfred", "Barry", "Ben", "Blake", "Bob",
          "Bill", "David", "Patrick", "Jamel", "Kevin", "Tony", "Doug", "Paul",
          "Carl", "Cindy", "George", "Greg", "John", "Jake", "Jack", "Steve", "Sarah",
          "Aisha", "Zarah", "Abir", "Diyal", "Raiid", "Sabirah", "Nada", "Lina", "Jabbor",
          "Kedar", "Jumahah", "Caliana", "Rana", "Taysir", "Halim", "Rashaad", "Azzam", "Samman",
          "Halim", "Taliha", "Yesha", "Amina", "Falkhir", "Caliana", "Nura", "Amina"]

#NPC
class NPC():
  def __init__(self):
    self.name = random.choice(NAMES)
    self.health = 0
    self.inventory = [Item.sword()]
    self.interactions = ["buy", "sell", "talk", "examine", "attack"]
    tmp = 1/5 * self.health
    self.gold = 100
    self.vendor = 1.0 + (random.randint(-250, 1000) / 1000.0)
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
      if string == "talk": self.talk(player)
      if string == "examine": self.examine(player)
      if string == "attack": self.attack(player)
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
            Util.gamePrint(item + "costs " + str(math.floor(x.value * self.vendor)) +" gold")
            tmp = Util.cleanInput("Do you want to spend that much?: ")
            if Util.yesHuh(tmp):
              if player.gold >= x.value:
                  player.gold = player.gold - (math.floor(x.value * self.vendor))
                  self.gold = self.gold + (math.floor(x.value * self.vendor))
                  if x.effects == "sleep":
                      print "you go with " + str(self.name) + " to the " + str(x)
                      print "you sleep there for 8 hours"
                      player.tired = 110
                      player.end = player.end - 100
                      player.health = player.health + 100
                      self.inventory.remove(x)
                      break
                  else:
                    player.inventory.append(x)
                    self.inventory.remove(x)
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
          if x.compare(item):
            Util.gamePrint(item + "costs " + str(math.floor(x.value * self.vendor)) + " gold")
            tmp = Util.cleanInput("Do you want to sell it for that much?: ")
            if Util.yesHuh(tmp):
              if self.gold >= x.value: 
                  player.inventory.remove(x)
                  player.gold = player.gold + (math.floor(x.value * self.vendor))
                  self.gold = self.gold - (math.floor(x.value * self.vendor))
                  break
              else: Util.gamePrint(self.name + " can't afford that")
            if Util.noHuh(tmp):
              break
  def talk(self, player):
      Util.gamePrint(str(self.name) + " says: I'm not in the mood for conversation")

  def examine(self, player):
      Util.gamePrint(str(self.name) +" stands in exotic garb before you")

  def attack(self, player):
      maxPlayer = 1
      for item in player.inventory:
        if item.damage > maxPlayer:
          maxPlayer = item.damage
      maxEnemy = 1
      for item in self.inventory:
        if item.damage > maxEnemy:
          maxEnemy = item.damage
      while self.health >= 0 and player.health >= 0:
        self.health = self.health - maxPlayer
        player.health = player.health - maxEnemy
      if player.health <= 0:
        Util.gamePrint("you lost the fight")
      if self.health <= 0:
        Util.gamePrint("you won the fight ")
        print "you loot the body "
        for item in self.inventory:
          player.inventory.append(item)
          print "you gain a " + str(item)
        print "you also loot " + str(self.gold) + " gold"
        player.gold = player.gold + self.gold


class merchant(NPC):
    def __init__(self):
        self.name = random.choice(NAMES)
        self.health = 100
        self.inventory = [Item.sword(), Item.potion(), Item.knife()]
        self.interactions = ["buy", "sell", "talk", "attack", "examine"]
        self.gold = 200
        self.vendor = 1.0 + (random.randint(-250, 1000) / 1000.0)
    def npcType(self):
        return "Merchant "
    def attack(self, player):
      maxPlayer = 1
      for item in player.inventory:
        if item.damage > maxPlayer:
          maxPlayer = item.damage
      maxEnemy = 1
      for item in self.inventory:
        if item.damage > maxEnemy:
          maxEnemy = item.damage
      while self.health >= 0 and player.health >= 0:
        self.health = self.health - maxPlayer
        player.health = player.health - maxEnemy
      if player.health <= 0:
        Util.gamePrint("you lost the fight")
      if self.health <= 0:
        Util.gamePrint("you won the fight")
        print "you loot the body "
        for item in self.inventory:
          player.inventory.append(item)
          print "you gain a " + str(item)
        print "you also loot " + str(self.gold) + " gold"
        player.gold = player.gold + self.gold
    def talk(self, player):
      Util.gamePrint(str(self.name) + " says: I'm not in the mood for conversation")
    def examine(self, player):
      Util.gamePrint(str(self.name) +" stands in exotic garb before you")

class guard(NPC):
    def __init__(self):
        self.name = random.choice(NAMES)
        self.health = 200
        self.inventory = [Item.sword(), Item.shield(), Item.knife()]
        self.interactions = ["talk", "attack", "examine"]
        self.gold = 100
        self.vendor = 1.0 + (random.randint(-250, 1000) / 1000.0)
    def npcType(self):
        return "Guard "
    def attack(self, player):
      maxPlayer = 1
      for item in player.inventory:
        if item.damage > maxPlayer:
          maxPlayer = item.damage
      maxEnemy = 1
      for item in self.inventory:
        if item.damage > maxEnemy:
          maxEnemy = item.damage
      while self.health >= 0 and player.health >= 0:
        self.health = self.health - maxPlayer
        player.health = player.health - maxEnemy
      if player.health <= 0:
        Util.gamePrint("You lost the fight")
      if self.health <= 0:
        Util.gamePrint("You won the fight ")
        print "you loot the body "
        for item in self.inventory:
          player.inventory.append(item)
          print "you gain a " + str(item)
        print "you also loot " + str(self.gold) + " gold"
        player.gold = player.gold + self.gold
    def talk(self, player):
      Util.gamePrint(str(self.name) + " says: I'm not in the mood for conversation")

    def examine(self, player):
      Util.gamePrint(str(self.name) +" stands in exotic garb before you")

class innkeeper(NPC):
    def __init__(self):
      self.name = random.choice(NAMES)
      self.health = 50
      #innkeeper has cot that refills player's tired meter
      self.inventory = [Item.bed(), Item.potion(), Item.scroll()]
      self.interactions = ["Talk", "attack", "examine", "buy", "sell"]
      self.gold = 250
      self.vendor = 1.0
    def npcType(self):
      return "Innkeeper "
class barKeep(NPC):
    def __init__(self):
      self.name = random.choice(NAMES)
      self.health = 50
      self.inventory = [Item.cot(), Item.potion(), Item.scroll()]
      self.interactions = ["talk", "attack", "examine", "buy", "sell"]
      self.gold = 250
      self.vendor = 1.0
    def npcType(self):
      return "Bar Keep "
class peasant(NPC):
  def __init__(self):
      self.name = random.choice(NAMES)
      self.health = 50
      self.inventory = [Item.scrap(), Item.rock()]
      self.interactions = ["talk", "attack", "examine", "buy", "sell"]
      self.gold = 0
      self.vendor = .7
  def npcType(self):
      return "Peasant "
class dockhand(NPC):
  def __init__(self):
      self.name = random.choice(NAMES)
      self.health = 150
      self.inventory = [Item.potion(), Item.scroll()]
      self.interactions = ["talk", "attack", "examine", "buy", "sell"]
      self.gold = 200
      self.vendor = 1.1
  def npcType(self):
      return "Dockhand "
class royalty(NPC):
  def __init__(self):
      self.name = random.choice(NAMES)
      self.health = 150
      self.inventory = [Item.potion(5), Item.scroll()]
      self.interactions = ["talk", "attack", "examine", "buy", "sell"]
      self.gold = 500
      self.vendor = 1.5
  def npcType(self):
      return "Royal "
class highMerchant(NPC):
  def __init__(self):
      self.name = random.choice(NAMES)
      self.health = 150
      self.inventory = [Item.potion(5), Item.scroll(10), Item.spice(5)]
      self.interactions = ["talk", "attack", "examine", "buy", "sell"]
      self.gold = 500
      self.vendor = 1 + (random.randint(-500, 350)/1000.0)
  def npcType(self):
      return "High Merchant "
class cleric(NPC):
  def __init__(self):
      self.name = random.choice(NAMES)
      self.health = 150
      self.inventory = [Item.potion(5), Item.scroll(10), Item.spice(5)]
      self.interactions = ["Talk", "attack", "examine", "buy", "sell"]
      self.gold = 500
      self.vendor = 1 + (random.randint(-1000, 1000)/1000.0)
  def npcType(self):
    return "Cleric "
class cultist(NPC):
  def __init__(self):
      self.name = random.choice(NAMES)
      self.health = 150
      self.inventory = [Item.potion(5), Item.scroll(10), Item.spice(5)]
      self.interactions = ["talk", "attack", "examine", "buy", "sell"]
      self.gold = 500
      self.vendor = 1 + (random.randint(-1000, 1000)/1000.0)


