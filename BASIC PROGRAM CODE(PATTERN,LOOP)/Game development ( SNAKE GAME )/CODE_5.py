import pygame

pygame.init()

resolution = width, height = 1000, 500
screen = pygame.display.set_mode(resolution)

# colour = ( r , g , b) /( Red, Green, Blue ) / (0-255)

red = (255, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 255)
colour_1 = (110, 61, 45)

screen.fill(red)

h, w = 50, 50
x, y = 0, 0
moveX = 1
moveY = 1
clock = pygame.time.Clock()
FPS = 10000

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    screen.fill(white)
    pygame.draw.rect(screen, green, [x, y, w, h])
    x += moveX
    y += moveY
    if x > width - w:
        moveX = -1
    elif x < 0:
        moveX = 1
    if y > height - w:
        moveY = -1
    elif y < 0:
        moveY = 1



    pygame.display.update()
    clock.tick(FPS)
