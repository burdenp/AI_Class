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
	def __str__(self):
		return self.name
	def __repr__(self):
		return self.name
	def compare(self, string):
		return self.name == string

class sword(item):
	def __init__(self):
		self.value = 15
		self.damage = 15
		self.name = "sword"
		self.effects = False
	def __str__(self):
		return self.name
	def __repr__(self):
		return self.name
	def compare(self, string):
		return self.name == string

class axe(item):
	def __init__(self):
		self.value = 10
		self.damage = 10
		self.name = "axe"
		self.effects = False
	def __str__(self):
		return self.name
	def __repr__(self):
		return self.name
	def compare(self, string):
		return self.name == string

class potion(item):
	def __init__(self):
		self.value = 20
		self.damage = 0
		self.name = "potion"
		self.effects = "liquid"
	def __str__(self):
		return self.name
	def __repr__(self):
		return self.name
	def compare(self, string):
		return self.name == string

class scroll(item):
	def __init__(self):
		self.value = 20
		self.damage = 0
		self.name = "scroll"
		self.effects = "magic"
	def __str__(self):
		return self.name
	def __repr__(self):
		return self.name
	def compare(self, string):
		return self.name == string

class staff(item):
	def __init__(self):
		self.value = 5
		self.damage = 5
		self.name = "staff"
		self.effects = "none"
	def __str__(self):
		return self.name
	def __repr__(self):
		return self.name
	def compare(self, string):
		return self.name == string

class knife(item):
	def __init__(self):
		self.value = 10
		self.damage = 7
		self.name = "knife"
		self.effects = "kinfe"
	def __str__(self):
		return self.name
	def __repr__(self):
		return self.name
	def compare(self, string):
		return self.name == string

