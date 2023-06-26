import pygame

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

# Ball

ball_X = width / 2 - 12
ball_Y = height / 2 - 12
ball_XChange = 0.3
ball_YChange = 0.3
ballPixel = 24


def ball(x, y):
    screen.blit(ballImg, (x, y))


# Gaming Loop:

running = True
while running:
    screen.fill(red)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Bouncing the ball
    if ball_X + ballPixel >= width or ball_X <= 0:
        ball_XChange *= -1
    if ball_Y + ballPixel >= height or ball_Y <= 0:
        ball_YChange *= -1

    # Moving the ball
    ball_X += ball_XChange
    ball_Y += ball_YChange

    # Drawing the ball
    ballImg = pygame.draw.circle(screen, (0, 0, 255), (int(ball_X), int(ball_Y)), 15)

    pygame.display.update()