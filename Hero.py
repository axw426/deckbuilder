import pygame as pg
import copy 
from random import randint

import Card
import Communication as cm

pg.init()

class Hero():

	def __init__(self, name,verbose=False):
		self.Health=10
		self.Money=0
		self.Attack=0
		self.Name=name
		self.Deck=[]
		self.Hand=[]
		self.Discard=[]
		self.Dead=False
		self.Petrified=False
		
		#set up default deck for each hero
		if self.Name=='Harry':
			#print ("\nSetting up Harry Deck")
			for i in range(7):
				self.Deck.append(Card.Card("Alohomora"))
			self.Deck.append(Card.Card("Invisibility Cloak"))
			self.Deck.append(Card.Card("Hedwig"))
			self.Deck.append(Card.Card("Firebolt"))	
			
		if self.Name=='Ron':
			#print ("\nSetting up Ron Deck")
			for i in range(7):
				self.Deck.append(Card.Card("Alohomora"))
			self.Deck.append(Card.Card("Bertie Botts Every Flavour Beans"))
			self.Deck.append(Card.Card("Pigwidgeon"))
			self.Deck.append(Card.Card("CleanSweep 11"))	

		if self.Name=='Hermione':
			#print ("\nSetting up Harry Deck")
			for i in range(7):
				self.Deck.append(Card.Card("Alohomora"))
			self.Deck.append(Card.Card("Invisibility Cloak"))
			self.Deck.append(Card.Card("Hedwig"))
			self.Deck.append(Card.Card("Firebolt"))	
			
		if self.Name=='Neville':
			#print ("\nSetting up Ron Deck")
			for i in range(7):
				self.Deck.append(Card.Card("Alohomora"))
			self.Deck.append(Card.Card("Bertie Botts Every Flavour Beans"))
			self.Deck.append(Card.Card("Pigwidgeon"))
			self.Deck.append(Card.Card("CleanSweep 11"))				
			
			

		#self.ShuffleDeck(self.Deck)
		self.Deck=Card.Shuffle(self.Deck)
		self.DrawHand(5)
		if verbose==True:
			print ("\nCards in Hand are:")
			self.PrintHand()
			print ("\nCards in Deck are:")
			self.PrintDeck()
			
	def PrintDeck(self):
		for card in self.Deck:
			print (card.Name,",",card.Text)
	
	def PrintHand(self):
		for card in self.Hand:
			print (card.Name,",",card.Text)			
				
	def DrawHand(self,nCards):
		for i in range(nCards):
			#print (i,len(self.Hand),len(self.Deck))
			self.Hand.append(self.Deck.pop())

	def LoseHealth(self,damage,location):
		if self.Dead==False:
			
			#check if invisible
			invisible=False
			for card in self.Deck:
				if card.Name=="Invisibility Cloak":
					invisible=True
					break
			
			#assign damage		
			if invisible==True:	
				self.Health-=1
			else:
				self.Health-=damage
							
			if self.Health<=0:
				self.Die()
				location.AddControl(1)
				
				
	def Die(self):
		self.Dead=True
		self.DiscardCard((int)(len(self.Hand)/2))
		self.Health=0
		
	def DiscardCard(self, N):
		for i in range(N):
			if len(self.Hand)>0:
				self.Discard.append(self.Hand.pop(0))
				



def SelectHeroes():
	nHeroes=cm.GetInt("How many players are there? (Max 4)",1,4)
	allowedHeroes=['Harry','Hermione','Ron','Neville','Random']
	selectedHeroes=[]
	for i in range(nHeroes):
		message="Select a hero from: "
		for x in allowedHeroes:
			message+=x+" "
		message+="\n"
	
		while True:
			txt=input(message)
			if txt in allowedHeroes:
				if txt=='Random':
					txt=allowedHeroes[randint(0,len(allowedHeroes)-2)]
					print("You got",txt)
				selectedHeroes.append(Hero(txt,False))
				allowedHeroes.remove(txt)
				break
			else:
				print("Not a valid option!!")
	return selectedHeroes
	
	
		
	
	