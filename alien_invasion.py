import sys
import pygame

from settings import Settings
from ship import Ship

def run_game():
    pygame.init
    #cua so game tu settings
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_wight,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #Make a ship
    ship = Ship(screen)

    #vong lap
    while True:

        #lenh thoat
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # background color
        screen.fill(ai_settings.bg_color)
        ship.blitme()
        #luon cap nhat trang thai moi nhat
        pygame.display.flip()

run_game()