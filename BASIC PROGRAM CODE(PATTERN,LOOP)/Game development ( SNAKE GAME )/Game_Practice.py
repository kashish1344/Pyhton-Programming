import pygame
import random

pygame.init()

resolution = width, height = 1000, 500
screen = pygame.display.set_mode(resolution)
red = (255, 00, 0)
green = (0, 255, 0)
white = (0, 0, 0)
blue = (0, 0, 255)

clock = pygame.time.clock()
FPS = 1000

h , w = 50 , 50

frog_img = pygame.image.load('frog.png')
frog_img_w = frog.img.get_width()
frog_img_h = frog.img.get_height()

def home():
    font = pygame.font.SysFont(None,100)
    text = font.render("Welcome to Snake Game",True,black)
    text_2 = font.render("Press SPACE to Start Game",True,black)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pyagme.K_Space:
                    game()

        screen.fill(white)
        screen.blit(text,(100,100))
        screen.blit(text_2,(100,200))
        pygame.display.update()

def gameOver():
    font = pygame.font.SysFont(None,100)
    text = font.render("Game Over",True,black)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.blit(text,(100,100))
        pygame.display.update()

def draw_snake(snakelist):
    for i in range(len(snakelist)):
        pygame.draw.rect(screen,red,[snakelist[i][0],
                                     snakelist[i][1],
                                     w,h])

def game():
    x , y = 0,0
    moveX = 0
    moveY = 0

    frog_x = random.randint(0,width - frog_img_w)
    frog_y = random.randint(0, height - frog_img_h)

    snakelist = []
    snakelength = 1

    while True:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    moveX = 1
                    moveY = 0
                elif event.key == pygame.K_LEFT:
                    moveX = -1
                    moveY = 0
                elif event.key == pygame.K_DOWN:
                    moveY = 1
                    moveX = 0
                elif event.key == pygame.K_UP:
                    moveY = -1
                    moveX = 0

        screen.fill(white)
        snake_rect = pygame.draw.rect(screen,red,[x,y,w,h])
        screen.blit(frog_img,(frog_x,frog_y))
        frog_rect = pyagme.Rect(frog_x,frog_y,frog_img_w,frog_img_h)
        x+=moveX
        y+=moveY

        snakehead = []
        snakehead.append(x)
        snakehead.append(y)
        snakelist.append(snakehead)

        draw_snake(snakelist)

        if len(snakelist) > snakelength:
            del snakelist[0]

        if frog_rect.colliderrect(snake_rect)
            frog_x = random.randint(0,width - frog_img_w)
            frog_y = random.randint(0, height - frog_img_h)

        snakelength+=20

    for each in snakelist[:-1]:
        if each == snakelist[-1]:
            print("Game Over")
            gameOver()

    if x > width:
        x = -w
    elif x < -w:
        x = width

    if y > height:
        y = -h
    elif y < -h:
        y = height
    pygame.display.update()
    clock.tick(FPS)

home()






