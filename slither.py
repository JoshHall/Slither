import pygame
import random

pygame.init()

black = pygame.Color("black")
honeydew = pygame.Color("honeydew")
peachpuff = pygame.Color("peachpuff")
red = pygame.Color("red")
green = pygame.Color('green')
grannysmith = (150,222,140)
bloodred = (132,3,3)
bg = pygame.image.load("images/sand.jpg")
snakehead = pygame.image.load("images/snakehead.png")
snaketail = pygame.image.load("images/snaketail.png")
snakebody = pygame.image.load("images/snakebody.png")
apple = pygame.image.load("images/apple.png")

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Slither')

clock = pygame.time.Clock()

block_size = 20
FPS = 12
direction = "right"
randfont = pygame.font.SysFont('comicsansms', 25)




def random_color():
    aList =[0,1,2]
    for color in aList:
        randindex = random.randrange(0, 100)
        newcolor = randindex
        aList[color] = newcolor
    r = aList[0]
    g = aList[1]
    b = aList[2]
    randomColor = (r,g,b)
    return randomColor


def random_size():
    sizes = []
    for i in range(12,51):
        sizes.append(i)
    randind = random.randrange(0, len(sizes))
    randNum = sizes[randind]
    return randNum


def random_font():
    global randfont
    allfonts = pygame.font.get_fonts()
    randindex = random.randrange(0, len(allfonts))
    randfont = allfonts[randindex]
    return randfont

randomfont = pygame.font.SysFont(random_font(),random_size())
smallfont = pygame.font.SysFont('commicsansms', 25)
medfont = pygame.font.SysFont('commicsansms', 50)
largefont = pygame.font.SysFont('commicsansms', 70)

rand_Color = random_color()

def randAppleGen():
    randAppleX = round(random.randrange(0, display_width - block_size))# / 10) * 10
    randAppleY = round(random.randrange(0, display_height - block_size))# / 10) * 10

    return randAppleX, randAppleY

def pause(snakeLength):
    paused = True

    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
        gameDisplay.fill(peachpuff)
        message_to_screen("Paused", black, -100, "large")
        message_to_screen("Press C to continue or Q to quit", black, 35)
        message_to_screen("________________________________", black, 15)
        message_to_screen("Score: " + str(snakeLength -1), rand_Color, 0 ,"large")
        pygame.display.update()
        clock.tick(5)

def score(score):
    text = smallfont.render('Score: '+str(score), True, black)
    gameDisplay.blit(text, [0,0])


def game_intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        gameDisplay.fill(peachpuff)
        message_to_screen('Welcome to Slither', green , -100, 'large')
        message_to_screen('The Objective of the game is to eat the apples', black , -30)
        message_to_screen('The more apples you eat, the longer you get', black , 10)
        message_to_screen('If you run into the edges or yourself, you die!', black , 50)
        message_to_screen('Press C to play, P to Pause, or Q to quit', black , 180)
        pygame.display.update()
        clock.tick(15)


def snake(block_size, snakeList):
    if direction == 'right':
        head = pygame.transform.rotate(snakehead, 270)
        tail = pygame.transform.rotate(snaketail, 270)
        body = pygame.transform.rotate(snakebody, 270)
    elif direction == 'left':
        head = pygame.transform.rotate(snakehead, 90)
        tail = pygame.transform.rotate(snaketail, 90)
        body = pygame.transform.rotate(snakebody, 90)
    elif direction == 'up':
        head = snakehead
        tail = snaketail
        body = snakebody
    elif direction == 'down':
        head = pygame.transform.rotate(snakehead, 180)
        tail = pygame.transform.rotate(snaketail, 180)
        body = pygame.transform.rotate(snakebody, 180)

    gameDisplay.blit(head, (snakeList[-1][0],snakeList[-1][1]))

    for XnY in snakeList[:-1]:
        if snakeList[0][0] == XnY[0] and snakeList[0][1] == XnY[1]:
            gameDisplay.blit(tail, (snakeList[0][0],snakeList[0][1]))
        else:
            gameDisplay.blit(body, (XnY[0],XnY[1]))

def text_objects(text, color, size):
    if size == "small":
        textSurface = smallfont.render(text, True, color)
    elif size == "medium":
        textSurface = medfont.render(text, True, color)
    elif size == "large":
        textSurface = largefont.render(text, True, color)
    elif size == "random":
        textSurface = randomfont.render(text, True, color)
    return textSurface, textSurface.get_rect()

def message_to_screen(msg, color, y_displace = 0, size = "small"):
    textSurface, textRect = text_objects(msg, color, size)
    textRect.center = (display_width/2), (display_height/2) + y_displace
    gameDisplay.blit(textSurface, textRect)

def gameLoop():
    global direction, largefont, smallfont, medfont, randomfont, rand_Color
    gameExit = False
    gameOver = False

    lead_x = display_width/2
    lead_y = display_height/2

    lead_x_change = block_size
    lead_y_change = 0

    snakeList = []
    snakeLength = 1

    randAppleX,randAppleY=randAppleGen()

    randomfont = pygame.font.SysFont(random_font(),random_size())
    smallfont = pygame.font.SysFont('commicsansms', 25)
    medfont = pygame.font.SysFont('commicsansms', 50)
    largefont = pygame.font.SysFont('commicsansms', 70)

    rand_Color = random_color()
    direction = "right"

    while not gameExit:

        while gameOver == True:
            # gameDisplay.fill(peachpuff, rect=[(display_width* 0.25),(display_height/2.15),display_width/2,50])
            gameDisplay.fill(peachpuff)
            message_to_screen("Game Over", red, y_displace = -30, size= "large")
            message_to_screen('Press C to play again or Q to quit', rand_Color, 50, 'medium')
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = False
                    gameExit = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    elif event.key == pygame.K_c:
                        gameLoop()
                        random_size()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    direction = "left"
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    direction = "right"
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    direction = "up"
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    direction = "down"
                    lead_y_change = block_size
                    lead_x_change = 0
                elif event.key == pygame.K_p:
                    pause(snakeLength)

        if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0:
            gameOver = True

        lead_x += lead_x_change
        lead_y += lead_y_change

        gameDisplay.blit(bg, (0, 0))


        appleThickness = 15
        # where you want to draw, color, rectangle[where on the surface, <--, width, height]
        # pygame.draw.rect(gameDisplay, grannysmith, [randAppleX, randAppleY,appleThickness,appleThickness])
        gameDisplay.blit(apple, (randAppleX, randAppleY))

        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)

        if len(snakeList) > snakeLength:
            del snakeList[0]

        for eachSegment in snakeList[:-1]:
            if eachSegment == snakeHead:
                gameOver = True

        snake(block_size, snakeList)

        score(snakeLength-1)

        pygame.display.update()

        if lead_x < randAppleX + appleThickness and lead_x + block_size > randAppleX and lead_y < randAppleY + appleThickness and lead_y + block_size > randAppleY:
            randAppleX,randAppleY=randAppleGen()
            snakeLength += 1

        clock.tick(FPS)

    pygame.quit()
    quit()

game_intro()
gameLoop()


#####  Bonus things   ###########

# ~~~~~~~~~~~~ Move while pressed ~~~~~~~~~~~~~~~~
# if event.type == pygame.KEYDOWN:
#     if event.key == pygame.K_LEFT or event.key == pygame.K_a:
#         lead_x_change = -10
#     if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
#         lead_x_change = 10
#     if event.key == pygame.K_UP or event.key == pygame.K_w:
#         lead_y_change = -10
#     if event.key == pygame.K_DOWN or event.key == pygame.K_s:
#         lead_y_change = 10
# if event.type == pygame.KEYUP:
#     if event.key == pygame.K_LEFT or event.key == pygame.K_a or event.key == pygame.K_RIGHT or event.key == pygame.K_d:
#         lead_x_change = 0
#     if event.key == pygame.K_UP or event.key == pygame.K_w or event.key == pygame.K_DOWN or event.key == pygame.K_s:
#         lead_y_change = 0

# ~~~~~ Using fill to make shapes
# gameDisplay.fill(honeydew, rect=[200,200,50,50])
# pygame.draw.rect(gameDisplay, bloodred, [XnY[0],XnY[1],block_size,block_size])
