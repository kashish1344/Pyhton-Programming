import pygame
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

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:

    posX, posY = pygame.mouse.get_pos()
    screen.blit(bg_image, (0, 0))
    screen.blit(spaceShip, (posX, height - 150))
    pygame.display.update()
