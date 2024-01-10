import pygame

from pygame.sprite import Sprite

class Alien(Sprite):
    """class alien"""

    def __init__(self, ai_settings, screen):
        """init alien va set its start"""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        #load alien image va set its 
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        #dat dinh vi
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def blitme(self):
        """Draw alien"""
        self.screen.blit(self.image, self.rect)