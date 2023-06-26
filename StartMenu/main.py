import pygame



pygame.init()

#Colors
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)

darkblue = (0, 0, 150)
lightblue = (0, 0, 255)

#Dimension
width = 800
height = 600

#Screen
screen = pygame.display.set_mode((width, height))


# GameIntro
def gameIntro():
    global intro
    intro = True
    while intro:  # while loop used because it should show intro menu continuously till we select PLAY button
        screen.fill(green)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        startButton()

        # StartMenu Writing
        font = pygame.font.Font("freesansbold.ttf", 40)
        introDetail = font.render("START MENU", True, blue)
        screen.blit(introDetail, (270, 400))

        pygame.display.update()


#Game loop
def gameLoop():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(blue)

        pygame.display.update()





def startButton():
    mouse = pygame.mouse.get_pos()  # It gets the position of the mouse in TUPLE (XPos, YPos)

    clicked = pygame.mouse.get_pressed()  # It gets a tuple value of clicking.....   #if clicked then 1 and if not clicked then 0 #(leftClick, Dontknow, rightClick)
    #print(clicked[0])          Left
    #print(clicked[1])          Dont know
    #print(clicked[2]           Right





    #Coord of RECTANGLE
    startXPos, startYPos, widthOfRect, heightOfRect = 350, 500, 100, 70

    #MouseClicking Condition
    if startXPos + widthOfRect  > mouse[0] and startXPos < mouse[0] and startYPos + heightOfRect > mouse[1] and startYPos < mouse[1]:         # if mouse's X-Coord is in range of Rect's X Coord      # and mouse's Y-Coord is in range of Rect's Y Coord
            print("Mouse")
            #then draw a dark rect so that the highlight will be displayed
            pygame.draw.rect(screen, darkblue, (startXPos, startYPos, widthOfRect,
                                                 heightOfRect))  # (surface, color, rect(startXPos, startYPos, width, height),  NO width for FILLED rectangle
            if clicked[0] == 1:  # If mouse left key is clicked
                gameLoop()  # Start the game loop i.e. the game
                global intro
                intro = False  # and exit the intro page

    else:
        # Draw a StartButtonRectangle which is of ORIGINAL COLOR
        pygame.draw.rect(screen, lightblue, (startXPos, startYPos, widthOfRect,
                                             heightOfRect))  # (surface, color, rect(startXPos, startYPos, width, height),  NO width for FILLED rectangle

    # Write start after the rectangle drawn
    startfont = pygame.font.Font("freesansbold.ttf", 12)
    startDetail = startfont.render("START", True, red)
    screen.blit(startDetail, (380, 530))






gameIntro()                #VERY IMMMMPPPPPP   #Call this function before the gaming while loop, so that game intro while loop works and next screen is not brought without PLAY button selected





