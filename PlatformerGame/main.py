
import pygame

pygame.init()

# Dimension of the screen
width = 600
height = 600

# Colours
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)

# Creating a Screen
screen = pygame.display.set_mode((width, height))
# Title
pygame.display.set_caption("Platformer Game")


bgImg = pygame.image.load("blocksBackground.jpg")
bgImg2 = pygame.image.load("wallBackground.jpg")
bgX = 0
bgY = 0
bgX2 = bgX + 650
bgXChange = 0.5


#Player 
playerImg = pygame.image.load("player.png")
player_X = 50
player_Y = 50
playerPixel = 64
player_XChange = 0
player_YChange = 0
playerRect = pygame.Rect(player_X, player_Y, playerPixel, playerPixel)
testRect = pygame.Rect(100, 100, 100, 50)




def draw():
    screen.blit(bgImg, (bgX, bgY))
    screen.blit(bgImg2, (bgX2, bgY))


# Gaming Loop:
running = True
while running:
    screen.fill(white)
    draw()

    screen.blit(playerImg, (player_X, player_Y))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player_XChange = 0.5
            if event.key == pygame.K_LEFT:
                player_XChange = -0.5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                player_XChange = 0
            if event.key == pygame.K_LEFT:
                player_XChange = 0

    if player_Y > height - playerPixel:
        player_YChange = -player_YChange
    else:
        player_YChange += 0.025


    playerRect.x = player_X
    playerRect.y = player_Y

    player_X += player_XChange
    player_Y += player_YChange



    if playerRect.colliderect(testRect):
        pygame.draw.rect(screen, red, testRect)
    else:
        pygame.draw.rect(screen, black, testRect)




    if bgX > width:
        bgX = -650
    if bgX2 > width:
        bgX2 = -650
    bgX += bgXChange
    bgX2 += bgXChange


    pygame.display.update()