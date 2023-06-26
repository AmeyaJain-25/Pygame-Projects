import pygame  # Importing all the packages of the pygame
import random # Importing random so that we can give random positions to our enemy

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
pygame.init()  # Initializes the pygame
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Dimension of the screen
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

width = 800  # Width of the SCREEN or the FRAME or the WINDOW
height = 600  # Height of the SCREEN or the FRAME or the WINDOW

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Colours
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Creating a Screen
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
screen = pygame.display.set_mode((width, height))

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Creating Background
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
backgroundImg = pygame.image.load("space.jpg")



#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Title
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
pygame.display.set_caption("PyGame Title")  # Giving the title to the Output

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Icon
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
icon = pygame.image.load(
    "joystick.png")  # Loading the image to the pygame and important note is to store the image in main.py file
pygame.display.set_icon(icon)  # Displaying it or drawing on the screen

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Player
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
playerImg = pygame.image.load("shooter.png")
playerXPosition = 370
playerYPosition = 480
playerXPositionChange = 0

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Enemy
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
enemyImg = pygame.image.load("enemy.png")
enemyXPosition = random.randint(0,800)         #Giving enemy a random position on X-axis between range 0 to 800
enemyYPosition = random.randint(0, 150)        #Giving enemy a random position on Y-axis between range 0 to 150
enemyXPositionChange = 1.5                     #Initial speed of enemy in X direction is, 0.3 because if its 0, then it will not move because there is no key function given it to move
enemyYPositionChange = 40                      #Initial speed of enemy in y direction is, 40 pixels downwards because if its 0, then it will not move because there is no key function given it to move


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Bullet
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
bulletImg = pygame.image.load("bullet.png")
bulletXPosition = 0                            #Bullet position is at 0 because its not moving in X direction
bulletYPosition = 480                          #Bullet position is as such that it is at position of player
bulletXPositionChange = 0                      #No need of changing the X positon as the bullet is only moving upward
bulletYPositionChange = 5                      #Speed of the bullet in upward direction
bulletState = "ready"                          #state of bullet is ready --- its ready to fire but INVISIBLE




#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Player Function
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def player(x, y):
    screen.blit(playerImg, (x, y))  # blit means to draw on a screen and parameters are (what to draw, (where to draw))

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Enemy Function
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def enemy(x, y):
    screen.blit(enemyImg, (x, y))  # blit means to draw on a screen and parameters are (what to draw, (where to draw))

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Firing Bullet Function
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def fireBullet(x, y):                                #Function for bullet when fired
    global bulletState
    bulletState = "fired"                            #when this function is called....bullet state is fired
    screen.blit(bulletImg, (x + 8, y + 10))          #and its image drawn is at 8 pixels right to X parameter(player X pos) and 10 pixels below Y parameter(bullet Y pos)





#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Gaming Loop:
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
running = True  # running value i.e its true while the player is running
while running:
    # --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    screen.fill(red)  # screen is filled with color
    # --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    screen.blit(backgroundImg, (0, 0))     #Backround image drawn from start i.e (0, 0)
    # --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



    for event in pygame.event.get():  # getting all the events happening externally using loop
        if event.type == pygame.QUIT:  # if QUIT button or X button is pressed
            running = False  # Running value returns while loop as false and the loop breaks
        # --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        # Checkimg whether the keystroke pressed is correct or not or whether its right key or left key
        # --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        if event.type == pygame.KEYDOWN:  # KEYDOWN means a key is *pressed* on a keyboard
            print("Any key is pressed")  # Any key is pressed

            if event.key == pygame.K_LEFT:  # Left key is Pressed
                print("Left arrow is pressed")
                playerXPositionChange = -2   # When left key is pressed, move the player in left direction with a value or speed of 0.1

            if event.key == pygame.K_RIGHT:  # Right key is Pressed
                print("Right arrow is pressed")
                playerXPositionChange = 2    # When right key is pressed, move the player in right direction with a value or speed of 0.1

            if event.key == pygame.K_SPACE:  # When SpaceBar is pressed
                fireBullet(playerXPosition, bulletYPosition)  #firebullet function calls and image is shown at its starting position but not moving

        if event.type == pygame.KEYUP:  # KEYUP means a key which is pressed is *released* on a keyboard
            if event.key == pygame.K_LEFT:
                print("Left arrow is released")
                playerXPositionChange = 0  # If the key is released, then change the playerXchangepos to 0...... i.e no increment in playerXchange and the player tops

            if event.key == pygame.K_RIGHT:
                print("Right arrow is released")
                playerXPositionChange = 0  # If the key is released, then change the playerXchangepos to 0...... i.e no increment in playerXchange and the player tops

    # --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    if bulletState is "fired":                            #If bullet state is fired i.e when firebullet func calls i.e. when spacebar is pressed
        fireBullet(playerXPosition, bulletYPosition)      #call the bullet image and
        bulletYPosition -= bulletYPositionChange          #move the bullet in upward direction
    # --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



    # --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    playerXPosition += playerXPositionChange  # Increasing the position in X direction for moving the player
    # --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #For returning back or bouncing back when it collides with its walls
    # --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    if playerXPosition <= 0:                         #if the player is at coordinate 0 or less than 0 i.e leaving the screen
        playerXPosition = 0                          #then keep it at 0 position and dont let it go less than 0
    elif playerXPosition >= width - 32:              #if the player is at coordinate width - (image pixel size) or greater than width - (image pixel size)  i.e leaving the screen
        playerXPosition = width - 32                 #then keep it at width - (image pixel size) position and dont let it go beyond width - (image pixel size)
               #width - (image pixel size)

    # --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    """
    # For returning the player again in from left side after leaving from right:
    if playerXPosition > width:  # if the player leaves the screen i.e if player if after (800)
        playerXPosition = 0  # bring player back to the left coordinate
    # For returning the player again in from right side after leaving from left:
    if playerXPosition < 0:  # if the player leaves the screen i.e if player is before (0)
        playerXPosition = width  # bring player back to the right coordinate
    """
    # --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    # --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    enemyXPosition += enemyXPositionChange  # Increasing the position in X direction for moving the enemy #Enemy moves only in X direction..as no y position given
    # --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    # --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # For returning back or bouncing back when it collides with its walls and when colliding, bring it down by 40 pixels
    # --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    if enemyXPosition <= 0:                          #if the enemy is at coordinate 0 or less than 0 i.e leaving the screen
        enemyXPositionChange = 1.5                   #then change its position with speed of 0.3 i.e in right side direction
        enemyYPosition += enemyYPositionChange       #when it collides the left wall, then bring it down by enemyYposChange value i.e. 40
    elif enemyXPosition >= width - 32:               #if the enemy is at coordinate width - (image pixel size) or greater than width - (image pixel size)  i.e leaving the screen
        enemyXPositionChange = -1.5                  #then change its position with speed of 0.3 i.e in left side direction
        enemyYPosition += enemyYPositionChange       #when it collides the right wall, then bring it down by enemyYposChange value i.e. 40







    # --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    player(playerXPosition, playerYPosition)  # Call the player function after the screen is created (IMP)
    enemy(enemyXPosition,enemyYPosition)      # Call the enemy function after the screen is created (IMP)
    # --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


    pygame.display.update()  # Updating the screen is imp because it changes the screen for each cycle or events or the loop


