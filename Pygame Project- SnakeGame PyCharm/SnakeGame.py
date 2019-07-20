import pygame
import random

pygame.display.init()

display_widht = 1065
display_height = 465

snake_width = 15
snake_height = 15

white = (255, 255, 255)
black = (0, 0, 0)

gameDisplay = pygame.display.set_mode((display_widht, display_height))
pygame.display.set_caption('Snake Game')
clock = pygame.time.Clock()

snakeImg = pygame.image.load('body_part.png')
n1 = pygame.image.load('number_1.png')
n2 = pygame.image.load('number_2.png')
n3 = pygame.image.load('number_3.png')

def load_snake(x, y):
    gameDisplay.blit(snakeImg, (x, y))

def countdown():
    gameDisplay.fill(white)
    gameDisplay.blit(n3, (487, 167))
    pygame.display.update()
    clock.tick(1)
    gameDisplay.blit(n2, (487, 167))
    pygame.display.update()
    clock.tick(1)
    gameDisplay.blit(n1, (487, 167))
    pygame.display.update()
    clock.tick(1)

def gameloop():

    x = int((random.randint(0, 1050)) / snake_width) * snake_width
    y = int((random.randint(0, 450)) / snake_height) * snake_height
    x_change = 0
    y_change = 0

    LEFT = -15
    RIGHT = 15
    UP = -15
    DOWN = 15

    direction = random.randint(-2, 2)
    while direction == 0:
        direction = random.randint(-2, 2)
    behind = 0

    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

            if direction == 1 or direction == -1:
                behind = direction * 2
                if direction == 1:
                    x_change = LEFT
                    y_change = 0
                if direction == -1:
                    y_change = UP
                    x_change = 0
            else:
                behind = direction / 2
                if direction == 2:
                    x_change = RIGHT
                    y_change = 0
                if direction == -2:
                    y_change = DOWN
                    x_change = 0

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_UP:
                    direction = -1  # UP
                if event.key == pygame.K_RIGHT:
                    direction = 2  # RIGHT
                if event.key == pygame.K_DOWN:
                    direction = -2  # DOWN
                if event.key == pygame.K_LEFT:
                    direction = 1  # LEFT

        x += x_change
        y += y_change

        gameDisplay.fill(white)
        load_snake(x, y)

        if x >= (display_widht - snake_width) or x <= 0:
            #crash()
            gameExit = True
        if y <= 0 or y >= (display_height - snake_height):
            #crash()
            gameExit = True

        pygame.display.update()
        clock.tick(7)

countdown()
gameloop()

pygame.quit()
quit()