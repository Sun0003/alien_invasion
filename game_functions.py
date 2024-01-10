import sys
import pygame

from bullet import Bullet

def check_events(ai_settings, screen, ship, bullets):
    """quan ly su kien rieng biet"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings,screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """move right-left"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)

def fire_bullet(ai_settings, screen, ship, bullets):
    """Fire a bullet"""
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def check_keyup_events(event, ship):
    """donot move"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def update_screen(ai_settings, screen, ship, bullets):
    """Cap nhat trang thai va ship moi nhat"""
    # background color
    screen.fill(ai_settings.bg_color)
    #ve lai vien dan
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    #luon cap nhat trang thai moi nhat
    pygame.display.flip()
    
def update_bullets(bullets):
    """Update position of bullets va xoa dan cu"""
    #update
    bullets.update()
    #xoa vien dan
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    