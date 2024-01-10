import pygame

from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf
from pygame.sprite import Group

def run_game():
    pygame.init
    
    #cua so game tu settings
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_wight,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #Make a ship
    ship = Ship(screen,ai_settings)
    #Make group alien
    aliens = Group()
    #Make group bullet
    bullets = Group()

    gf.create_fleet(ai_settings, screen, aliens)

    #vong lap
    while True:
        #lenh thoat va cap nhat doi tuong
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        
        gf.update_bullets(bullets)

        # background color #luon cap nhat trang thai moi nhat
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)

run_game()