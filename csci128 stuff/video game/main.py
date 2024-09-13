# 2D Combat Platformer (Unnamed)
# Written by Roman Rodriguez

# Importing
import pygame
from pygame.locals import *

# Initializing pygame and screen
pygame.init()
size = width, height = 1280, 720
screen = pygame.display.set_mode(size)

# Schedule (list of classes)
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.image.load("32x64.png").convert()
        self.rect = self.surf.get_rect()

class Weapon(pygame.sprite.Sprite):
    def __init__(self):
        super(Weapon, self).__init__()
        self.surf = pygame.image.load("weapon.png").convert()
        self.rect = self.surf.get_rect()

class EnvObject(pygame.sprite.Sprite):
    def __init__(self):
        super(EnvObject, self).__init__()
        self.surf = pygame.image.load("512platform.png").convert()
        self.rect = self.surf.get_rect()

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.image.load("enemy1.png").convert()
        self.rect = self.surf.get_rect()

# Object initialization
square = Player(); weapon = Weapon()
obst1 = EnvObject()
enemy1 = Enemy()
square.rect.centerx = width / 2; square.rect.bottom = height
obst1.rect.center = (width / 2, height - 110)
enemy1.rect.centerx, enemy1.rect.bottom = width / 2, obst1.rect.top


# Group management
all_sprites = pygame.sprite.Group()
environ = pygame.sprite.Group()
player = pygame.sprite.Group()
weapons = pygame.sprite.Group()
enemies = pygame.sprite.Group()
all_sprites.add(square); all_sprites.add(obst1); all_sprites.add(enemy1)
environ.add(obst1)
enemies.add(enemy1)

# Game clock for framerate (might need work later)
clock = pygame.time.Clock()

# Stuff that needed defining 
speedx, speedy = 0, 0
counter = 0
sheathed = True
jump = False
grounded = True

running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYUP:
            if event.key == K_SPACE:
                jump = False
            if event.key == K_k:
                sheathed = True
    
    # Input reading
    pressed_keys = pygame.key.get_pressed()

    # Character location update and collision detection
    if pressed_keys[K_a]:
        weapon.rect.right = square.rect.left
        speedx = -4
        square.rect.move_ip(speedx, 0)
        if pygame.sprite.spritecollideany(square, environ):
            obstacle = pygame.sprite.spritecollideany(square, environ)
            square.rect.left = obstacle.rect.right
        speedx = 0
    if pressed_keys[K_d]:
        weapon.rect.left = square.rect.right
        speedx = 4
        square.rect.move_ip(speedx, 0)
        if pygame.sprite.spritecollideany(square, environ):
            obstacle = pygame.sprite.spritecollideany(square, environ)
            square.rect.right = obstacle.rect.left
        speedx = 0
    if pressed_keys[K_SPACE]:
        if jump == False and grounded == True and speedy == 0:
            jump = True
            grounded = False
            speedy = -16
    square.rect.move_ip(0, speedy)
    speedy += 1
    if pygame.sprite.spritecollideany(square, environ):
        obstacle = pygame.sprite.spritecollideany(square, environ)
        if square.rect.top < obstacle.rect.bottom and square.rect.bottom > obstacle.rect.bottom:
            square.rect.top = obstacle.rect.bottom
            speedy = 0
        elif square.rect.bottom > obstacle.rect.top and square.rect.top < obstacle.rect.bottom:
            square.rect.bottom = obstacle.rect.top
            speedy = 0
            grounded = True
    if square.rect.top < 0:
        square.rect.top = 0
        speedy = 0
    if square.rect.bottom > height:
        square.rect.bottom = height
        speedy = 0
        grounded = True
    if square.rect.right > width:
        square.rect.right = width
    if square.rect.left < 0:
        square.rect.left = 0

    # Attack handling
    if pressed_keys[K_k]:
        if sheathed:
            weapons.add(weapon)
            all_sprites.add(weapon)
            counter = 10
            sheathed = False
    weapon.rect.centery = square.rect.centery
    counter -= 1
    if counter < 0:
        counter = 0
        all_sprites.remove(weapon)
        weapons.remove(weapon)
    
    if pygame.sprite.groupcollide(weapons, enemies, False, False):
        pygame.sprite.spritecollideany(weapon, enemies).kill()

    screen.fill((30, 30, 30))
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
