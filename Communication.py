import pygame as pg
pg.init()

def PrintStatus(gm):
	for hero in gm.Heroes:
		print(hero.Name+": Health=",hero.Health,", Attack=",hero.Attack,", Money=",hero.Money)
	print ("Location:",gm.LocationDeck[0].Name,", Control=",gm.LocationDeck[0].Darkness," of ",gm.LocationDeck[0].MaxDarkness)
	for villain in gm.VillainDeck[0:gm.NVillains]:
		print("Villain:",villain.Name)

	
def AllowQuit(gm):
	
	print("Would you like to quit the game? (y/n)")

	while True:
		opt=input()
		if opt=='y' or opt=='yes':
			gm.Status='Quit'
			break
		elif opt=='n' or opt=='no':
			break
		else:
			print("Invalid option, please type either y or n")
			
def GetInt(message,min,max):
	print(message)
	while True:
		try:
			opt = int(input())       
		except ValueError:
			print("Enter a value between",min,"and",max)
			continue
		else:
			if opt>max or opt<min:
				print("Enter a value between",min,"and",max)
				continue
			else:
				return opt