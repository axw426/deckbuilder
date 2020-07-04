import pygame as pg
pg.init()
import Hero
import Locations
import DarkArts
import Villains
import Card
import Communication as cm
import Manager

class Manager():

	def __init__(self):
		self.Status="VillainTurn"
		self.Level=None
		self.Heroes=None
		self.LocationDeck=[]
		self.DarkArtsDeck=[]
		self.DarkArtsDiscard=[]
		self.VillainDeck=[]
		self.VillainDiscard=[]
		self.NVillains=0
		self.BuyDeck=[]#
		self.CurrentLocation=None
		self.CurrentVillainsNames=[]
		self.CurrentVillains=[]
		
	def NewGame(self):
		#Select Level
		self.Level=cm.GetInt("Select Level",1,1)

		#Select Heroes:
		self.Heroes=Hero.SelectHeroes()

		#Build Locations
		self.LocationDeck=Locations.BuildLocations(self.Level,False)
		self.CurrentLocation=self.LocationDeck[0]

		#Build Dark Arts
		self.DarkArtsDeck=DarkArts.BuildDarkArts(self.Level,False)

		#Build Villains
		self.VillainDeck,self.NVillains=Villains.BuildVillainDeck(self.Level,False)
		self.CurrentVillains=self.VillainDeck[0:self.NVillains]
		self.CurrentVillainsNames=[i.Name for i in self.VillainDeck[0:self.NVillains]]

		#Build Buy Deck
		self.BuyDeck=Card.BuildBuyDeck(self.Level,False)

			