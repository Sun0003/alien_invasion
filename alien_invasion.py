import pygame

from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    pygame.init
    #cua so game tu settings
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_wight,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    #Make a ship
    ship = Ship(screen,ai_settings)
    #vong lap
    while True:
        #lenh thoat va cap nhat doi tuong
        gf.check_events(ship)
        ship.update()
        # background color #luon cap nhat trang thai moi nhat
        gf.update_screen(ai_settings, screen, ship)

run_game()