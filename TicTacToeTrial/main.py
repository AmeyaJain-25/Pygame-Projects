import pygame

width = 600
height = 600

screen = pygame.display.set_mode((width, height))



XPlayerImg = pygame.image.load("close.png")
YPlayerImg = pygame.image.load("question.png")

#
# board = [0, 1, 2,
#          3, 4, 5,
#          6, 7, 8]



playerPlaying = "X"

def playing():
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()




running = True
while running:

    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()


    pygame.draw.line(screen, (0, 0, 0), (200, 10), (200, 590), 2)
    pygame.draw.line(screen, (0, 0, 0), (400, 10), (400, 590), 2)
    pygame.draw.line(screen, (0, 0, 0), (10, 200), (590, 200), 2)
    pygame.draw.line(screen, (0, 0, 0), (10, 400), (590, 400), 2)

    row = None
    column = None
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if 10 < mouse[0] and 200 > mouse[0]:
        row = 1
    if 200 < mouse[0] and 400 > mouse[0]:
        row = 2
    if 400 < mouse[0] and 590 > mouse[0]:
        row = 3

    if 10 < mouse[1] and 200 > mouse[1]:
        column = 1
    if 200 < mouse[1] and 400 > mouse[1]:
        column = 2
    if 400 < mouse[1] and 590 > mouse[1]:
        column = 3


    posXCrd, posYCrd = 0, 0


    if row == 1:
        posXCrd = 10
    if row == 2:
        posXCrd = 200
    if row == 3:
        posXCrd = 400

    if column == 1:
        posYCrd = 10
    if column == 2:
        posYCrd = 200
    if column == 3:
        posYCrd = 400



    if row == 1 and column == 1 and click[0] == 1:
        if playerPlaying == "X":
            playerPlaying = "O"
        elif playerPlaying == "O":
            playerPlaying = "X"
    # elif row == 1 and column == 2 and click[0] == 1:
    #     if playerPlaying == "X":
    #         screen.blit(XPlayerImg, posXCrd, posYCrd)
    #         playerPlaying = "O"
    #     elif playerPlaying == "O":
    #         screen.blit(YPlayerImg, posXCrd, posYCrd)
    #         playerPlaying = "X"
    # elif row == 1 and column == 3 and click[0] == 1:
    #     if playerPlaying == "X":
    #         screen.blit(XPlayerImg, posXCrd, posYCrd)
    #         playerPlaying = "O"
    #     elif playerPlaying == "O":
    #         screen.blit(YPlayerImg, posXCrd, posYCrd)
    #         playerPlaying = "X"
    # elif row == 2 and column == 1 and click[0] == 1:
    #     if playerPlaying == "X":
    #         screen.blit(XPlayerImg, posXCrd, posYCrd)
    #         playerPlaying = "O"
    #     elif playerPlaying == "O":
    #         screen.blit(YPlayerImg, posXCrd, posYCrd)
    #         playerPlaying = "X"
    # elif row == 2 and column == 2 and click[0] == 1:
    #     if playerPlaying == "X":
    #         screen.blit(XPlayerImg, posXCrd, posYCrd)
    #         playerPlaying = "O"
    #     elif playerPlaying == "O":
    #         screen.blit(YPlayerImg, posXCrd, posYCrd)
    #         playerPlaying = "X"
    # elif row == 2 and column == 3 and click[0] == 1:
    #     if playerPlaying == "X":
    #         screen.blit(XPlayerImg, posXCrd, posYCrd)
    #         playerPlaying = "O"
    #     elif playerPlaying == "O":
    #         screen.blit(YPlayerImg, posXCrd, posYCrd)
    #         playerPlaying = "X"
    # elif row == 3 and column == 1 and click[0] == 1:
    #     if playerPlaying == "X":
    #         screen.blit(XPlayerImg, posXCrd, posYCrd)
    #         playerPlaying = "O"
    #     elif playerPlaying == "O":
    #         screen.blit(YPlayerImg, posXCrd, posYCrd)
    #         playerPlaying = "X"
    # elif row == 3 and column == 2 and click[0] == 1:
    #     if playerPlaying == "X":
    #         screen.blit(XPlayerImg, posXCrd, posYCrd)
    #         playerPlaying = "O"
    #     elif playerPlaying == "O":
    #         screen.blit(YPlayerImg, posXCrd, posYCrd)
    #         playerPlaying = "X"
    # elif row == 3 and column == 3 and click[0] == 1:
    #     if playerPlaying == "X":
    #         screen.blit(XPlayerImg, posXCrd, posYCrd)
    #         playerPlaying = "O"
    #     elif playerPlaying == "O":
    #         screen.blit(YPlayerImg, posXCrd, posYCrd)
    #         playerPlaying = "X"


    if playerPlaying == "X":
        screen.blit(XPlayerImg, (posXCrd, posYCrd))
        
    elif playerPlaying == "O":
        screen.blit(YPlayerImg, (posXCrd, posYCrd))











    pygame.display.update()