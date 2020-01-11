import pygame
import time
import random

# initializing the pygame
pygame.init()

display_width = 800
display_height = 600

#color of the screen
black = (0,0,0)
white = (255,255,255)
#color of the button
red = (200, 0, 0)
green = (0, 200, 0)
blue = ( 0, 0, 200)

bright_red = (255, 0, 0)
bright_green = (0, 255, 0)
bright_blue = (0, 0, 255)

block_color = (0,255,255)

car_width = 45
#create screen and caption
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('A bit Racey')
clock = pygame.time.Clock()

carImg = pygame.image.load('car5.png')
gameIcon = pygame.image.load('car1.png')




pygame.display.set_icon(gameIcon)

pause = False

#scoreboard
def things_dodged(count):
    font = pygame.font.SysFont("comicsansms", 25)
    text = font.render("score: " + str(count), True, black)
    gameDisplay.blit(text, (0, 0))

def game_level(num):
    font = pygame.font.SysFont("comicsansms", 25)
    texta = font.render("level: " + str(num), True, black)
    gameDisplay.blit(texta, (650, 0))


#object fall on the screen
def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])

# blit draw the image
def car(x, y):
    gameDisplay.blit(carImg, (x, y))

# function called on crash
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def crash():
    largeText = pygame.font.SysFont("comicsansms", 115)
    TextSurf, TextRect = text_objects("You Crashed", largeText)
    TextRect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(TextSurf, TextRect)

    while True:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # gameDisplay.fill(white)
        button("Play Again", 150, 450, 100, 50, green, bright_green, game_loop)
        button("Quit", 550, 450, 100, 50, red, bright_red, quitgame)

  # Display will update until the while loop is true
        pygame.display.update()
        clock.tick(15)


def button(msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    # print(click)
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))
    smallText= pygame.font.SysFont("comicsansms", 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x + (w / 2)), (y + (h / 2)))
    gameDisplay.blit(textSurf, textRect)


def help():
    gameDisplay.fill(white)
    pygame.help()
    help()


def quitgame():
    pygame.quit()
    quit()


def unpause():
    global pause
    pause = False

# Press p button to pause
def paused():
    largeText = pygame.font.SysFont("comicsansms", 115)
    TextSurf, TextRect = text_objects("Paused", largeText)
    TextRect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(TextSurf, TextRect)

    while pause:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # gameDisplay.fill(white)
        button("Continue", 150, 450, 100, 50, green, bright_green, unpause)
        button("Quit", 550, 450, 100, 50, red, bright_red, quitgame)

        pygame.display.update()
        clock.tick(15)

#opening screen of the game
def game_intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)
        largeText = pygame.font.SysFont("comicsansms", 115)
        TextSurf, TextRect = text_objects("A bit Racey", largeText)
        TextRect.center = ((display_width / 2), (display_height / 2))
        gameDisplay.blit(TextSurf, TextRect)

        button("Help", 350, 450, 100, 50, blue,bright_blue, help)
        button("GO!", 150, 450, 100, 50, green, bright_green, game_loop)
        button("Quit", 550, 450, 100, 50, red, bright_red, quitgame)

        pygame.display.update()
        clock.tick(15)

# game starts
def game_loop():
    global pause
    x = (display_width * 0.45)
    y = (display_height * 0.8)

    x_change = 0
# object shape and size
    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 5
    thing_width = 80
    thing_height = 80

    thingCount = 1
    level = 1
    score = 0

    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            # movement keys
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5
                if event.key == pygame.K_p:
                    pause = True
                    paused()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change
        gameDisplay.fill(white)

        # things(thingx, thingy, thingw, thingh, color)
        things(thing_startx, thing_starty, thing_width, thing_height, block_color)

        thing_starty += thing_speed
        car(x, y)
        num = level
        game_level(num)
        count = score
        things_dodged(count)
        if x > display_width - car_width or x < 0:
            crash()

        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0, display_width)
            score += 5
            thing_speed += 0.7
            thing_width += (score * 0.2)
        if score == 100:
            while True:
                level += 1
                for event in pygame.event.get():
                    # print(event)
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()

                gameDisplay.fill(white)
                largeText = pygame.font.SysFont("comicsansms", 115)
                TextSurf, TextRect = text_objects("you win", largeText)
                TextRect.center = ((display_width / 2), (display_height / 2))
                gameDisplay.blit(TextSurf, TextRect)

                button("level 2", 150, 450, 100, 50, green, bright_green, game_loop)
                button("Quit", 550, 450, 100, 50, red, bright_red, quitgame)


                pygame.display.update()
                clock.tick(15)

        if y < thing_starty + thing_height:
            print('y crossover')

            if x > thing_startx and x < thing_startx + thing_width or x + car_width > thing_startx and x + car_width < thing_startx + thing_width:
                print('x crossover')
                crash()

        pygame.display.update()
        clock.tick(50)


game_intro()
game_loop()
pygame.quit()
quit()
