import pygame as pg
pg.init()
from random import randint

class Card():

	def __init__(self, name):
		self.Name=name
		self.Image=''
		self.Text="Example text"
		self.Type=''
		
		if name=='Alohomora':
			self.Image=''
			self.Text="Gain 1 coin"
			self.Type="Spell"
			
		elif name=='Hedwig':
			self.Image=''
			self.Text="Gain 1 attack or two health"
			self.Type="Ally"
				
		elif name=='Firebolt':
			self.Image=''
			self.Text="Gain 1 attack. Gain a coin if you defeat a villain this turn"		
			self.Type="Item"
		
		elif name=='Invisibility Cloak':
			self.Image=''
			self.Text="Gain 1 coin, and stuff"	
			self.Type="Item"

		elif name=='Pigwidegeon':
			self.Image=''
			self.Text="Gain 1 attack or two health"
			self.Type="Ally"
				
		elif name=='Cleansweep 11':
			self.Image=''
			self.Text="Gain 1 attack. Gain a coin if you defeat a villain this turn"		
			self.Type="Item"
		
		elif name=='Bertie Botts Every Flavour Beans':
			self.Image=''
			self.Text="Gain 1 attack or two health"	
			self.Type="Item"			

		elif name=='Wingardium Leviosa':
			self.Image=''
			self.Text=""
			self.Type="Spell"

		elif name=='Descendo':
			self.Image=''
			self.Text=""
			self.Type="Spell"

		elif name=='Reparo':
			self.Image=''
			self.Text=""			
			self.Type="Spell"

		elif name=='Lumos':
			self.Image=''
			self.Text=""
			self.Type="Spell"

		elif name=='Incendio':
			self.Image=''
			self.Text=""
			self.Type="Spell"

		elif name=='Essence of Dittany':
			self.Image=''
			self.Text=""		
			self.Type="Item"

		elif name=='Quidditch Gear':
			self.Image=''
			self.Text=""
			self.Type="Item"

		elif name=='Golden Snitch':
			self.Image=''
			self.Text=""
			self.Type="Item"

		elif name=='Sorting Hat':
			self.Image=''
			self.Text=""
			self.Type="Item"

		elif name=='Oliver Wood':
			self.Image=''
			self.Text=""
			self.Type="Ally"

		elif name=='Albus Dumbledore':
			self.Image=''
			self.Text=""		
			self.Type="Ally"

		elif name=='Rubeus Hagrid':
			self.Image=''
			self.Text=""
			self.Type="Ally"

		elif name=='':
			self.Image=''
			self.Text=""			

def Shuffle(cards):
	temp=[]
	while len(cards)>0:
		i=randint(0,len(cards)-1)
		temp.append(cards[i])	
		cards.remove(cards[i])
	return temp

def AddToDeck(myList,x,n):
	for i in range(n):
		myList.append(x)
	
def BuildBuyDeck(level,verbose=False):
	buyDeck=[]
	
	if level==1:
		AddToDeck(buyDeck,Card("Wingardium Leviosa"),3)
		AddToDeck(buyDeck,Card("Descendo"),2)
		AddToDeck(buyDeck,Card("Reparo"),6)
		AddToDeck(buyDeck,Card("Lumos"),2)
		AddToDeck(buyDeck,Card("Incendio"),4)
		AddToDeck(buyDeck,Card("Essence of Dittany"),4)
		AddToDeck(buyDeck,Card("Quidditch Gear"),4)
		AddToDeck(buyDeck,Card("Golden Snitch"),1)
		AddToDeck(buyDeck,Card("Sorting Hat"),1)
		AddToDeck(buyDeck,Card("Oliver Wood"),1)
		AddToDeck(buyDeck,Card("Albus Dumbledore"),1)
		AddToDeck(buyDeck,Card("Rubeus Hagrid"),1)
	
	
	buyDeck=Shuffle(buyDeck)

	if verbose==True:
		print("\nBuy deck cards are:")
		for card in buyDeck:
			print (card.Name)


	