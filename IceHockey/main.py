#Icon

import pygame
import random

pygame.init()

# Dimension of the screen
width = 700
height = 550

# Colours
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)

# Creating a Screen
screen = pygame.display.set_mode((width, height))
# Title
pygame.display.set_caption("Ice Hockeys")


playerAScore = 0
playerBScore = 0

game_font = pygame.font.Font("freesansbold.ttf", 32)




#Ball
ballImg = pygame.image.load("balance-ball.png")
ball_X = width/2 - 12
ball_Y = height/2 - 12
ball_XChange = 0.3* random.choice((1, -1))
ball_YChange = 0.3
ballPixel = 24

def ball(x, y):
    screen.blit(ballImg, (x, y))

#Players
playerA_XPos = 0
playerA_YPos = height/2 - 50

playerB_XPos = width - 20
playerB_YPos = height/2 - 50

playerASpeed = 0
playerBSpeed = 0



playerA = pygame.Rect(playerA_XPos,playerA_YPos, 20, 100)
playerB = pygame.Rect(playerB_XPos, playerB_YPos, 20, 100)


def ballRestart():
    global ball_X, ball_Y, scoreTime
    ball_X = width/2 - 12
    ball_Y = height/2 -12
    global ball_YChange, ball_XChange
    currentTime = pygame.time.get_ticks()

    if currentTime - scoreTime < 2100:
        ball_XChange, ball_YChange = 0, 0
    else:
        ball_YChange = 0.3*random.choice((1, -1))
        ball_XChange = 0.3*random.choice((1, -1))
        scoreTime = None


def crash():
    global ball_XChange
    if (ball_Y > playerA.y and ball_Y < playerA.y + 100) or (ball_Y + ballPixel > playerA.y and ball_Y + ballPixel < playerA.y + 100) :
        if (ball_X <= playerA.x + 20 and ball_X >= playerA.x) or (ball_X + ballPixel <= playerA.x + 20 and ball_X + ballPixel >= playerA.x):
            print(1)
            ball_XChange *= -1

    if (ball_Y > playerB.y and ball_Y < playerB.y + 100) or (ball_Y + ballPixel > playerB.y and ball_Y + ballPixel < playerB.y + 100):
        if (ball_X + ballPixel >= playerB.x and ball_X + ballPixel <= playerB.x + 20) or (ball_X >= playerB.x and ball_X <= playerB.x + 20):
            print(2)
            ball_XChange *= -1





scoreTime = None

# Gaming Loop:

running = True
while running:
    screen.fill(red)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                playerASpeed += 1
            if event.key == pygame.K_w:
                playerASpeed -= 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_s:
                playerASpeed -= 1
            if event.key == pygame.K_w:
                playerASpeed += 1

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                playerBSpeed += 1
            if event.key == pygame.K_UP:
                playerBSpeed -= 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                playerBSpeed -= 1
            if event.key == pygame.K_UP:
                playerBSpeed += 1


    #Bouncing the ball
    if ball_X + ballPixel >= width:
        playerAScore += 1
        scoreTime = pygame.time.get_ticks()
    if ball_X <= 0:
        playerBScore += 1
        scoreTime = pygame.time.get_ticks()
    if ball_Y + ballPixel >= height or ball_Y <= 0:
        ball_YChange *= -1






    # Moving the ball
    ball_X += ball_XChange
    ball_Y += ball_YChange

    #Crash function calling
    crash()

    #Drawing the ball
    ball(ball_X, ball_Y)


    playerAText = game_font.render(str(playerAScore), True, blue)
    screen.blit(playerAText, (width/2 - 75, 340))

    playerBText = game_font.render(str(playerBScore), True, blue)
    screen.blit(playerBText, (width/2 + 75, 340))

    #Drawing the Players
    pygame.draw.rect(screen, black, playerA)
    pygame.draw.rect(screen, black, playerB)



    playerA.y += playerASpeed
    if playerA.top <= 0:
        playerA.top = 0
    if playerA.bottom >= height:
        playerA.bottom = height

    playerB.y += playerBSpeed
    if playerB.top <= 0:
        playerB.top = 0
    if playerB.bottom >= height:
        playerB.bottom = height


    if scoreTime:
        ballRestart()

    pygame.display.update()
