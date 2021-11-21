import pygame
import random

pygame.init()

resolution = width, height = 1000, 500
screen = pygame.display.set_mode(resolution)

bg_img = pygame.image.load("background.jpg")
aim_pointer = pygame.image.load("scope.png")
zom_1 = pygame.image.load("zombie.gif")
zom_2 = pygame.image.load("zombie_1.jpg")
zom_3 = pygame.image.load("zombie_2.gif")
gun_img = pygame.image.load("gun_1.png")

shotSound = pygame.mixer.Sound('shot.wav')
reloadSound = pygame.mixer.Sound("reloading.wav")
bg_sound = pygame.mixer.Sound('bg_sound.wav')
bg_sound.play()

red = (255, 0, 0)
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 255, 0)
color_1 = (120, 10, 45)
zom_x = random.randint(0, width - 220)
zom_y = random.randint(0, height - 220)


def score(counter):
    font = pygame.font.SysFont(None, 60)
    text = font.render("Score : " + str(counter), True, black)
    text_1 = font.render("Press 'r' to Reload the gun: ", True, black)
    screen.blit(text, (10, 10))
    screen.blit(text_1, (0, 60))


def main():
    zomList = [zom_1, zom_2, zom_3]
    zom_img = random.choice(zomList)
    counter = 0
    shot = 4

    while True:
        for event in pygame.event.get():

            if event.type == pygame.MOUSEBUTTONDOWN:
                shot -= 1
                if shot >= 0:
                    shotSound.play()
                    if rect_1.colliderect(rect_2):
                        zom_img = random.choice(zomList)
                        counter += 1

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    shot = 4
                    reloadSound.play()

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        posX, posY = pygame.mouse.get_pos()

        screen.blit(bg_img, (0, 0))
        screen.blit(zom_img, (zom_x, zom_y))
        screen.blit(aim_pointer, (posX - 50, posY - 48))
        screen.blit(gun_img, (posX, height - 80))

        rect_1 = pygame.Rect(posX - 50, posY - 48, aim_pointer.get_width(), aim_pointer.get_height())
        rect_2 = pygame.Rect(zom_x, zom_y, zom_img.get_width(), zom_img.get_height())

        score(counter)
        pygame.display.update()


main()
