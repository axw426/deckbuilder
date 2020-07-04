import pygame as pg
import Hero
import Locations
import DarkArts
import Villains
import Card
import Communication as cm
import Manager 

# --- Globals ---
# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
 
# Call this function so the Pygame library can initialize itself
pg.init()
 
# Create an 800x600 sized screen
#screen = pg.display.set_mode([1200, 650])
 
# Set the title of the window
#pg.display.set_caption('PokemonBattle')
 
clock = pg.time.Clock()

#setup game manager
print("Welcome to the Harry Potter game!!")
gm=Manager.Manager()
gm.NewGame()

while gm.Status!='Quit':

	status=gm.Status
	if status=='VillainTurn':
		print("")
		print("It's "+gm.Heroes[0].Name+"'s turn!")
		#update board & current cards- function based on current hero + all other decks
	
		#animation of each villain
		#effect of villain
		print("Current villains are:",gm.CurrentVillainsNames)
		for villain in gm.CurrentVillains:
			villain.Effect(gm)
	
		#animation for dark art
		#apply effect of dark art
		for i in range(gm.LocationDeck[0].NDarkArts):
			if len(gm.DarkArtsDeck)==0:
				gm.DarkArtsDeck=Card.Shuffle(gm.DarkArtsDiscard)
				gm.DarkArtsDiscard=[]
		
			gm.DarkArtsDeck[0].Effect(gm)
			gm.DarkArtsDiscard.append(gm.DarkArtsDeck.pop(0))
		
		#villains and dark arts done, change status to player turn
		gm.Status='PlayerTurn'
		
	#hero plays cards, assigns attack, buys cards
	#after each card evaluate if hero has died, villain has died
	#hero selects to end turn
	elif status=='PlayerTurn':
		print("Doing hero stuff")
		gm.Status='EndTurn'


	elif status=='EndTurn':
		#check if players have won
		if len(gm.VillainDeck)==0:
			print("Congratulations!! You defeated all the villains. You win!")
			gm.status='Quit'
		
		#check if location has been lost or game has been won
		elif gm.LocationDeck[0].Darkness==gm.LocationDeck[0].MaxDarkness:
			gm.LocationDeck.pop(0)
			if len(gm.LocationDeck)==0:
				print("You lost the last location. Game over!!")
				gm.Status='Quit'
			
		else:	
			#revive dead heroes, active hero discards deck and redraws	

			#start next round- rotate entires in hero list, hero[0] will always be active hero
			gm.Heroes.append(gm.Heroes.pop(0))
			gm.Status='VillainTurn'
	
	cm.PrintStatus(gm)
	cm.AllowQuit(gm)

	for event in pg.event.get():
		#check if game is over
		if event.type == pg.QUIT:
			gm.Status='Quit'
                    
            
	#draw everything    
	#screen.fill(BLACK)
    
	#pg.display.flip()
	# Pause
	clock.tick(5)
	
	
	#pg.time.delay(1000)
	
pg.quit()