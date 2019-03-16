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
		self.value = 20
		self.damage = 15
		self.name = "sword"
		self.effects = False
		self.num = 1
		self.type = "sword"

class staff(item):
	def __init__(self):
		self.value = 10
		self.damage = 5
		self.name = "staff"
		self.effects = False
		self.num = 1
		self.type = "staff"

class axe(item):
	def __init__(self):
		self.value = 15
		self.damage = 10
		self.name = "axe"
		self.effects = False
		self.num = 1
		self.type = "axe"

class potion(item):
	def __init__(self, num = None):
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
		self.value = 10
		self.damage = 7
		self.name = "knife"
		self.effects = False
		self.num = 1
		self.type = "knife"

class spear(item):
	def __init__(self):
		self.value = 10
		self.damage = 10
		self.name = "spear"
		self.effects = False
		self.num = 1
		self.type = "spear"

class shield(item):
	def __init__(self):
		self.value = 20
		self.damage = -5
		self.name = "shield"
		self.effects = "shield"
		self.num = 1
		self.type = "shield"

class bed(item):
	def __init__(self):
		self.value = 100
		self.damage = -100
		self.name = "bed"
		self.effects = "sleep"
		self.type = "bed"

class cot(item):
	def __init__(self):
		self.value = 50
		self.damage = -50
		self.name = "cot"
		self.effects = "sleep"
		self.type = "cot"
class spice(item):
	def __init__(self, num = None):
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