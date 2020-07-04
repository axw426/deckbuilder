import pygame as pg
pg.init()

import Card

class Villain():

	def __init__(self, name):
		self.Name=name
		self.Image=''
		self.Text=""
		self.Health=1
		self.MaxHealth=1
			
		if name=='Malfoy':
			self.Image=''
			self.Text="Active hero loses 2 health each time a control is added"
			self.Health=5
			self.MaxHealth=5

		elif name=='Crabbe and Goyle':
			self.Image=''
			self.Text="Lose 1 health when you discard a card"
			self.Health=5			
			self.MaxHealth=5

		elif name=='Professor Quirrel':
			self.Image=''
			self.Text="Active Hero lose 1 health"	
			self.Health=5
			self.MaxHealth=5
			
	def Effect(self,gm):
		print("Doing the bad stuff for:",self.Name)
		
		if self.Name=='Professor Quirrel':
			print(gm.Heroes[0].Name,"lost 1 health")
			gm.Heroes[0].LoseHealth(1,gm.LocationDeck[0])
			

def BuildVillainDeck(level,verbose=False):

	villains=[]
	nVillains=3
	
	if level==1:
		villains.append(Villain('Malfoy'))			
		villains.append(Villain('Crabbe and Goyle'))
		villains.append(Villain('Professor Quirrel'))
		nVillains=1
		
	villains=Card.Shuffle(villains)
	
	if verbose==True:
		print("\nVillains are:")
		for vil in villains:
			print (vil.Name)
	
	return villains,nVillains
			