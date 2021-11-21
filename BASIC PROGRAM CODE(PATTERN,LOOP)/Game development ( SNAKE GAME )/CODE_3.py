import pygame
pygame.init()

resolution = width , height = 1000 , 500
screen = pygame.display.set_mode(resolution)

#colour = ( r , g , b) /( Red, Green, Blue ) / (0-255)

red = (255,0,0)
white = (255,255,255)
green = (0,255,0)
blue = (0,0,255)
colour_1 = (110,61,45)

screen.fill(red)
h,w = 50,50
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            quit()

    for i in range(10):
        for j in range(i+1):
            pygame.draw.rect(screen, green, [j * 51, i*51, w, h])

    pygame.display.update()