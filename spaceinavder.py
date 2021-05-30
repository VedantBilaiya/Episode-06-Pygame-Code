# Importing and Intilizing Pygame
import pygame
pygame.init()

# Creating The Screen For Our Game
screen = pygame.display.set_mode((800,600))

# Title
pygame.display.set_caption('Space Invander Game')

# Icon
icon = pygame.image.load('launch.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('spaceship.png')
playerX = 370
playerY = 480
playerX_change = 0

def player():
    screen.blit(playerImg ,(playerX,playerY))

# Game Loop
running = True
while running:
    
    screen.fill(0)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -10
            if event.key == pygame.K_RIGHT:
                playerX_change = 10

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                playerX_change = 0
            if event.key == pygame.K_RIGHT:
                playerX_change = 0

        playerX += playerX_change


    if playerX <= 0:
        playerX = 0
    if playerX >= 736:
        playerX = 736

    # Calling The Functions
    player()
    pygame.display.update()
