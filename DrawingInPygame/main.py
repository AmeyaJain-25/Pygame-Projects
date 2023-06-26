import pygame

pygame.init()

#Colors
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)

#Dimension
width = 800
height = 600

#Screen
screen = pygame.display.set_mode((width, height))

#Pixel Array
pixArray = pygame.PixelArray(screen)   #To draw.....We are getting pixels in the screen......i.e. pixel array in (screen)
pixArray[10][20] = blue   #Pixel at position (10, 20) is drawn in blue color....It appears as a tiny point

#Draw a LINE
pygame.draw.line(screen, blue, (100, 200), (300, 450), 5)          # (surface, color, startPos, endPos, width(in pixels))

#Draw a RECTANGLE OUTLINE
pygame.draw.rect(screen, blue, (400, 40, 50, 25), 5)       # (surface, color, rect(startXPos, startYPos, width, height), width of the outer line of the rectangle)

#Draw a filled RECTANGLE
pygame.draw.rect(screen, blue, (400, 200, 50, 25))       # (surface, color, rect(startXPos, startYPos, width, height),  NO width for FILLED rectangle

#Draw a CIRCLE OUTLINE
pygame.draw.circle(screen, blue, (20, 20), 25, 5)             # (surface, color, CENTERposition(startPosCntr, endPosCntr), radius, width)

#Draw a FILLED CIRCLE
pygame.draw.circle(screen, blue, (250, 200), 55)             # (surface, color, CENTERposition(startPosCntr, endPosCntr), radius)

#Draw a POLYGON
pygame.draw.polygon(screen, blue, ((200, 300), (268, 450), (384, 556), (499, 300)), 3)   # (surface, color, pointList(tuple of the polygon points), width[ONLY FOR OUTLINE])


#Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    pygame.display.update()