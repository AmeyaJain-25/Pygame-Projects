
import pygame
import random

pygame.init()



# Colours
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)



# Dimensions
width = 650
height = 700
pixel = 64

# Screen
screen = pygame.display.set_mode((width, height))

# Title/Caption
pygame.display.set_caption("CORONA SCARPER")

# Icon
gameIcon = pygame.image.load("rectangleBlock.png")
pygame.display.set_icon(gameIcon)

# Background
backgroundImg = pygame.image.load("wallBackground.jpg")




# Player
playerImage = pygame.image.load("player.png")
playerXPosition = (width/2) - (pixel/2)
playerYPosition = height - pixel - 10     # So that the player will be at height of 20 above the base
playerXPositionChange = 0
def player(x, y):
    screen.blit(playerImage, (x, y))



# Block
blockImage = pygame.image.load("rectangleBlock.png")
blockXPosition = random.randint(0, (width - pixel))
blockYPosition = 0 - pixel
blockXPositionChange = 0
blockYPositionChange = 2    #SPEED OF THE BLOCK
def block(x, y):
    screen.blit(blockImage, (x, y))






# Crashing
def crash():
    global blockYPosition, scoreFont
    # Crashing Condition and Game Over
    if playerYPosition < (
            blockYPosition + pixel):  # If the block passes through the player's horizontal line, then check for block passing through its vertical line
        if (playerXPosition > blockXPosition and playerXPosition < (blockXPosition + pixel)) or (
                (playerXPosition + pixel) > blockXPosition and (playerXPosition + pixel) < (
                blockXPosition + pixel)):
            # |-----># If players left corner meets the block's corner ranges AND same for right corner, then you can crash it.
            blockYPosition = height + 1000  # If block crashed, then go down at height after the repeating block condition












running = True
while running:

    # Background Image
    screen.blit(backgroundImg, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        # Movement Key Control of Player
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                playerXPositionChange = 3
            if event.key == pygame.K_LEFT:
                playerXPositionChange = -3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or pygame.K_LEFT:
                playerXPositionChange = 0

    # Boundaries to the Player
    if playerXPosition >= (width - pixel):
        playerXPosition = (width - pixel)  # if it comes at right end, stay at right end and does not exceed
    if playerXPosition <= 0:
        playerXPosition = 0  # if it comes at left end, stay at left end and does not exceed

    # Movement of Player
    playerXPosition += playerXPositionChange

    # Movement of Block
    blockYPosition += blockYPositionChange

    # Multiple Blocks Movement after each other
    if blockYPosition >= height - 0 and blockYPosition <= (
            height + 200):  # and condition used because of game over function
        blockYPosition = 0 - pixel
        blockXPosition = random.randint(0, (width - pixel))
        # If block passes the player, then it dodges that block and increases the score by



    # Player Function Call
    player(playerXPosition, playerYPosition)

    # Block Function Call
    block(blockXPosition, blockYPosition)

    # Call of Crashing Function
    crash()

    pygame.display.update()
