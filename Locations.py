import pygame as pg
pg.init()


class Location():

	def __init__(self, name):
		self.Name=name
		self.Image=''
		self.Text=""
		self.MaxDarkness=1
		self.Darkness=0
		self.NDarkArts=1
		
		if name=='Diagon Alley':
			self.Image=''
			self.Text=""
			self.MaxDarkness=5

		if name=='Mirror of Erised':
			self.Image=''
			self.Text=""
		self.MaxDarkness=5			

	
	def AddControl(self,nEvil):
		for i in range(nEvil):
			if self.Darkness<self.MaxDarkness:
				self.Darkness+=nEvil
				


def BuildLocations(level,verbose=False):

	locations=[]
		
	if level==1:
		locations.append(Location('Diagon Alley'))			
		locations.append(Location('Mirror of Erised'))
		
	if verbose==True:
		print("\nLocations are:")
		for loc in locations:
			print (loc.Name)
	
	return locations
			