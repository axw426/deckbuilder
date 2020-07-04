import pygame as pg
pg.init()

import Card


class DarkArt():

	def __init__(self, name):
		self.Name=name
		self.Image=''
		self.Text=""
		
		if name=='Expulso':
			self.Image=''
			self.Text="Active hero loses 2 health"
		
		if name=='Petrification':
			self.Image=''
			self.Text="All heroes loses a health and cannot draw extra cards"

		if name=='Flipendo':
			self.Image=''
			self.Text="Active Hero loses a health and discards a card"

		if name=='He who must not be named':
			self.Image=''
			self.Text="Add 1 control to the location"	
			
	def Effect(self,gm):
		print ("Dark art event:", self.Name)	
		
		if self.Name=='Expulso':
			gm.Heroes[0].LoseHealth(2,gm.LocationDeck[0])
		
		if self.Name=='Petrification':
			for Hero in gm.Heroes:
				Hero.LoseHealth(1,gm.LocationDeck[0])
				Hero.Petrified=True

		if self.Name=='Flipendo':
			if 'Crabbe and Goyle' in gm.CurrentVillainsNames:
				gm.Heroes[0].LoseHealth(2,gm.LocationDeck[0])
			else:
				gm.Heroes[0].LoseHealth(1,gm.LocationDeck[0])
			gm.Heroes[0].DiscardCard(1)

		if self.Name=='He who must not be named':
			gm.LocationDeck[0].AddControl(1)		
			if 'Malfoy' in gm.CurrentVillainsNames:
				gm.Heroes[0].LoseHealth(2,gm.LocationDeck[0])			 
			

def BuildDarkArts(level,verbose=False):

	darkArts=[]
		
	if level==1:
		for i in range(3):
			darkArts.append(DarkArt('Expulso'))			
		for i in range(3):
			darkArts.append(DarkArt('He who must not be named'))
		for i in range(2):
			darkArts.append(DarkArt('Petrification'))			
		for i in range(2):
			darkArts.append(DarkArt('Flipendo'))		

	darkArts=Card.Shuffle(darkArts)
	if verbose==True:
		print("\nDark Arts are:")
		for card in darkArts:
			print (card.Name)
	return darkArts
	

			