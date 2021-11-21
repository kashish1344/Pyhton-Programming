import pygame
import random

pygame.init()

resolution = width, height = 1000, 500
screen = pygame.display.set_mode(resolution)

red = (255, 0, 0)
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 255, 0)
color_1 = (120, 10, 45)

bg_image = pygame.image.load("bg_img.jpg")

spaceShip = pygame.image.load("spaceship.png")
moveSpaceX = 0
moveSpaceY = 0
space_w = spaceShip.get_width()
space_h = spaceShip.get_height()

enemy = pygame.image.load('enemy.png')
enemy_w = random.randint(0, width)
enemy_h = random.randint(10, height // 2)
moveEnemyX = 1
moveEnemyY = 1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    posX, posY = pygame.mouse.get_pos()
    enemy_w += moveEnemyX
    if enemy_w <= 0:
        moveEnemyX = 1
        #enemy_w += moveEnemyX

    elif enemy_w >= width - 100:
        moveEnemyX = -1

    elif enemy_h <= 0:
        moveEnemyY = 1 - space_h
        enemy_h += moveEnemyY

    elif enemy_h >= width:
        moveEnemyY = -1

    screen.blit(bg_image, (0, 0))
    screen.blit(enemy, (enemy_w, enemy_h))
    screen.blit(spaceShip, (posX, height - 100))

    pygame.display.update()
