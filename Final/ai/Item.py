#Item class
import sys
import os
import time
from random import randint
import random
import string

class item():
	def __init__(self):
		self.value = 0
		self.damage = 0
		self.name = ""
		self.effects = False
		self.num = 1
		self.type = "item"
	def __str__(self):
		return self.name
	def __repr__(self):
		return self.name
	def __eq__(self, other):
		return self.type == other.type
	def compare(self, string):
		return self.name == string
	def printOut(self):
		print self.name + "'s stats:"
		print "it is worth " + str(self.value) + " gold"
		print "it does " + str(self.damage) + " damage"
		if self.effects != False:
			print "It has "  + str(self.effects) + " effects"


class sword(item):
	def __init__(self):
		item.__init__(self)
		self.value = 20
		self.damage = 15
		self.name = "sword"
		self.type = "sword"

class staff(item):
	def __init__(self):
		item.__init__(self)
		self.value = 10
		self.damage = 5
		self.name = "staff"
		self.type = "staff"

class axe(item):
	def __init__(self):
		item.__init__(self)
		self.value = 15
		self.damage = 10
		self.name = "axe"
		self.type = "axe"

class potion(item):
	def __init__(self, num = None):
		item.__init__(self)
		if num == None:
			self.value = 20
			self.damage = 0
			self.name = "potion"
			self.effects = "liquid"
			self.num = 1
		else:
			self.value = 20 * num
			self.damage = 0
			self.name = str(num) + " bottles of potion"
			self.effects = "liquid"
			self.num = num
		self.type = "potion"

class scroll(item):
	def __init__(self, num = None):
		item.__init__(self)
		if num == None:
			self.value = 20
			self.damage = 0
			self.name = "scroll"
			self.effects = "magic"
			self.num = 1
		else:
			self.value = 20 * num
			self.damage = 0
			self.name = str(num) + " scroll's of magic"
			self.effects = "magic"
			self.num = num
		self.type = "scroll"

class knife(item):
	def __init__(self):
		item.__init__(self)
		self.value = 10
		self.damage = 7
		self.name = "knife"
		self.type = "knife"

class spear(item):
	def __init__(self):
		item.__init__(self)
		self.value = 10
		self.damage = 10
		self.name = "spear"
		self.type = "spear"

class shield(item):
	def __init__(self):
		item.__init__(self)
		self.value = 20
		self.damage = -5
		self.name = "shield"
		self.effects = "shield"
		self.type = "shield"

class bed(item):
	def __init__(self):
		item.__init__(self)
		self.value = 100
		self.damage = -100
		self.name = "bed"
		self.effects = "sleep"
		self.type = "bed"

class cot(item):
	def __init__(self):
		item.__init__(self)
		self.value = 50
		self.damage = -50
		self.name = "cot"
		self.effects = "sleep"
		self.type = "cot"
class spice(item):
	def __init__(self, num = None):
		item.__init__(self)
		if num == None:
			self.value = 8
			self.damage = 0
			self.name = "spice"
			self.effects = "spice"
			self.num = 1
		else:
			self.value = 8 * num
			self.damage = 0
			self.name = str(num) + " packets of spice"
			self.effects = "spice"
			self.num = num
		self.type = "spice"


class dagger(item):
	def __init__(self):
		item.__init__(self)
		self.value = 6
		self.damage = 4
		self.name = "dagger"
		self.effects = "dagger"
		self.type = "dagger"


class rock(item):
	def __init__(self):
		randomWeight = randint(1, 100)
		item.__init__(self)
		if randomWeight <= 20:
			self.damage = 8
		elif randomWeight <= 50 and randomWeight >= 20:
			self.damage = 14
		elif randomWeight <=100 and randomWeight >= 51:
			self.damage = 18
		self.name = "rock"
		self.effects = "rock"
		self.type = "rock"

class poison(item):
	def __init__(self):
		item.__init__(self)
		randomHit = randint(1, 10)
		self.value = 7
		if randomHit == 9 or randomHit == 10:
			self.damage = 10
		elif randomHit == 6 or randomHit == 7 or randomHit == 8:
			self.damage = 7
		elif randomHit == 3 or randomHit == 4 or randomHit == 5:
			self.damage = 4
		else:
			self.damage == 2
		self.name = "poison fang"
		self.effects = "poison"
		self.type = "poison"


class arrow(item):
	def __init__(self):
		item.__init__(self)
		self.value = 7
		self.damage = 8
		self.name = "arrow"
		self.effects = "arrow"
		self.type = "arrow"



class hammer(item):
	def __init__(self):
		item.__init__(self)
		self.value = 16
		self.damage = 13
		self.name = "hammer"
		self.effects = "hammer"
		self.type = "hammer"

class claw(item):
	def __init__(self):
		item.__init__(self)
		self.value = 9
		self.damage = 9
		self.name = "Berserker's Claws"
		self.effects = "claw"
		self.type = "claw"

class scrap(item):
	def __init__(self):
		item.__init__(self)
		self.value = 4
		self.damage = 3
		self.name = "metal scrap"
		self.effects = "scrap"
		self.type = "metal"

class glass(item):
	def __init__(self):
		item.__init__(self)
		self.value = 3
		self.damage = 6
		self.name = "shard glass"
		self.effects = "glass"
		self.type = "glass"

class slingshot(item):
	def __init__(self):
		item.__init__(self)
		self.value = 5
		self.damage = 5
		self.name = "sling shot"
		self.effects = "slingshot"
		self.type = "slingshot"
 
class grenade(item):
 	def __init__(self):
 		item.__init__(self)
 		self.value = 17
 		self.damage = 18
 		self.name = "grenade"
 		self.effects = "grenade"
 		self.type = "grenade"

