import sys
import pygame

from settings import Settings

def run_game():
    pygame.init
    #cua so game tu settings
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_wight,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #vong lap
    while True:

        #lenh thoat
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # background color
        screen.fill(ai_settings.bg_color)
        
        #luon cap nhat trang thai moi nhat
        pygame.display.flip()

run_game()