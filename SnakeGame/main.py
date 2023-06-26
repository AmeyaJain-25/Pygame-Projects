#Icon

import pygame
import random


pygame.init()

# Dimension of the screen
width = 700
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
pygame.display.set_caption("Snake")

#Plot snake
def plotSnake(screen, color, snakeList, snake_size):
    for x,y in snakeList:
        pygame.draw.rect(screen, color, [x, y, snake_size, snake_size])


snakeList = []
snakeLength = 1


def gameLoop():
    # Snake Dimenions
    snake_X = width / 2
    snake_Y = height / 2
    snakeSize = 10
    snake_XChange = 0
    snake_YChange = 0

    # Food
    foodSize = 10
    food_X = random.randint(0, width - foodSize)
    food_Y = random.randint(0, height - foodSize)

    # Score
    score = 0
    scoreFont = pygame.font.Font("freesansbold.ttf", 40)



    gameOver = None

    # Gaming Loop:
    running = True
    while running:

        if gameOver:
            screen.fill(white)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameLoop()

        else:
            screen.fill(white)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        snake_XChange = 0.25
                        snake_YChange = 0
                    if event.key == pygame.K_LEFT:
                        snake_XChange = -0.25
                        snake_YChange = 0
                    if event.key == pygame.K_UP:
                        snake_XChange = 0
                        snake_YChange = -0.25
                    if event.key == pygame.K_DOWN:
                        snake_XChange = 0
                        snake_YChange = 0.25

            # #snakeShowing
            pygame.draw.rect(screen, black, [snake_X, snake_Y, snakeSize, snakeSize])

            # FoodShowing
            pygame.draw.rect(screen, red, [food_X, food_Y, foodSize, foodSize])

            # Eating Food
            global snakeLength
            if abs(snake_X - food_X) < 8 and abs(snake_Y - food_Y) < 8:
                score += 1
                snakeLength += 5  # increase by 5 pixel
                food_X = random.randint(0, width - foodSize)
                food_Y = random.randint(0, height - foodSize)

            # Snake Movement
            snake_X += snake_XChange
            snake_Y += snake_YChange

            # Drawing snake's head in snake list
            head = []
            head.append(snake_X)
            head.append(snake_Y)
            snakeList.append(head)

            if len(snakeList) > snakeLength:
                del snakeList[0]

            if snake_X < 0 or snake_X > width or snake_Y > height or snake_Y < 0 or head in snakeList[:-1]:
                gameOver = True
            # Plotting snake function
            plotSnake(screen, green, snakeList, snakeSize)





        screen.blit(scoreFont.render("Score: " + str(score), True, red), (10, 10))

        pygame.display.update()



gameLoop()