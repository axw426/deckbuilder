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
			self.Text="Active Hhero loses a health and discards a card"

		if name=='He who must not be named':
			self.Image=''
			self.Text="Add 1 control to the location"	

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
	
	
	
			