import sys
import pygame

from settings import Settings

def run_game():
    #Khoi tao game va tao doi tuong screen.
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien Invasion")
    
    # tao mau game
    bg_color = (230, 230, 230)
    # Vong lap chinh trong game
    while True:
    	#watch cho ma va su kien
    	for event in pygame.event.get():
    	    if event.type == pygame.QUIT:
    	        sys.exit()
    	        
    	screen.fill(bg_color)
    	
    	#ve man hinh
    	pygame.display.flip()
    	
run_game()
    	
    
    
