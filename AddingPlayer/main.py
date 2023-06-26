import pygame  # Importing all the packages of the pygame

pygame.init()  # Initializes the pygame

# Dimension of the screen
width = 800  # Width of the SCREEN or the FRAME or the WINDOW
height = 600  # Height of the SCREEN or the FRAME or the WINDOW

# Colours
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)

# Creating a Screen
screen = pygame.display.set_mode((width, height))
# Title
pygame.display.set_caption("PyGame Title")  # Giving the title to the Output
# Icon
icon = pygame.image.load(
    "joystick.png")  # Loading the image to the pygame and important note is to store the image in main.py file
pygame.display.set_icon(icon)  # Displaying it or drawing on the screen

# Player
playerImg = pygame.image.load("joystick.png")
playerXPosition = 370
playerYPosition = 480


def player():
    screen.blit(playerImg, (playerXPosition, playerYPosition))  # blit means to draw on a screen and parameters are (what to draw, (where to draw))


# Gaming Loop:

running = True  # running value i.e its true while the player is running
while running:

    screen.fill(red)  # screen is filled with color    #Initially only create the background

    for event in pygame.event.get():  # getting all the events happening externally using loop
        if event.type == pygame.QUIT:  # if QUIT button or X button is pressed
            running = False  # Running value returns while loop as false and the loop breaks



    player()  # Call the player function after the screen is created (IMP)


    pygame.display.update()  # Updating the screen is imp because it changes the screen for each cycle or events or the loop
