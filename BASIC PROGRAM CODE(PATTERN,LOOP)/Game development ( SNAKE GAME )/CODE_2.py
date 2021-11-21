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
h,w = 100,100
x = width//2-w//2
y = height//2-h//2

while True:
    for event in pygame.event.get():
        #print(event)
        if event.type==pygame.QUIT:
            pygame.quit()
            quit()

    #pygame.draw.rect(screen,green,[0,0,50,50])
    #pygame.draw.rect(screen,blue,[width//2-25,height//2-25,50,50])
    pygame.draw.rect(screen, green, [x, y, w, h])
    pygame.draw.circle(screen,blue,[x,y],50)

    pygame.display.update()