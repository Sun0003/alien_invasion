import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Vien dan ban ra tu ship"""

    def __init__(self, ai_settings, screen, ship):
        """vien dan"""
        super(Bullet, self).__init__()
        self.screen = screen

        #tao vi tri cua dan
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        #cap nhat dan
        self.y = float(self.rect.y)

        #mau dan va toc do
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """Move dan :>"""
        self.y -= self.speed_factor
        self.rect.y = self.y

    def draw_bullet(self):
        """Ve dan tren screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)