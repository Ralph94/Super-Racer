import pygame, random
from time import sleep

pygame.init()
# music/sounds
CarSound = pygame.mixer.Sound("image/CAR+Peels+Out.wav")
CarSound_two = pygame.mixer.Sound("image/racing01.wav")
CarSound_three = pygame.mixer.Sound("image/RACECAR.wav")
CarSound_four = pygame.mixer.Sound("image/formula+1.wav")
Crowds = pygame.mixer.Sound("image/cheer_8k.wav")
Crowds_two = pygame.mixer.Sound("image/applause7.wav")
Crowds_three = pygame.mixer.Sound("image/crowdapplause1.wav")
final_tone = pygame.mixer.Sound("image/Victory.wav")
music = pygame.mixer.music.load("image/Led Zeppelin - Rock And Roll (Alternate Mix) (Official Music Video).mp3")
pygame.mixer.music.play(-1)
bg = pygame.image.load('image/Crowds.png')
main_img = pygame.image.load("image/img4.png")
main_img2 = pygame.image.load("image/img5.png")
side_img = pygame.image.load("image/bull2.png")
side_img2 = pygame.image.load("image/fox.png")
pauseimg = pygame.image.load("image/pause2.png")



clock = pygame.time.Clock()

pause = False

# Setting up our colors that we are going to use
GREEN = (20, 255, 140)
GREY = (210, 210, 210)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)
BLACKWHITE = (96, 96, 96)
BLACK = (105, 105, 105)
RGREEN = (0, 66, 37)
LIGHT_RED = (200, 0, 0)
BRIGHT_GREEN = (0, 255, 0)
DARK_BLUE = (0, 0, 139)
BLUE = (0, 0, 255)
NAVY = (0, 0 , 128)
DARK_OLIVE_GREEN = (85, 107, 47)
YELLOW_AND_GREEN = (154, 205, 50)


SCREENWIDTH = 400
SCREENHEIGHT = 500

size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Car Racing")
Icon = pygame.image.load("image/redca_iconr.png")
pygame.display.set_icon((Icon))
# This will be a list that will contain all the sprites we intend to use in our game.
# all_sprites_list = pygame.sprite.Group()

# player
playerIMG = pygame.image.load("image/red_racecar.png")
playerX = 280
playerY = 450
playerCar_position = 0

# player2
playerIMG_two = pygame.image.load("image/greencar.png")
playerX_two = 150
playerY_two = 450
playerCar_position_two = 0

# player3
playerIMG_three = pygame.image.load("image/Orangecar.png")
playerX_three = 60
playerY_three = 450
playerCar_position_three = 0

# player4
playerIMG_four = pygame.image.load("image/yellowcar2.png")
playerX_four = 210
playerY_four = 450
playerCar_position_four = 0


# Putting cars to the screen
def player(x, y):
    screen.blit(playerIMG, (x, y))


def player_two(x, y):
    screen.blit(playerIMG_two, (x, y))


def player_three(x, y):
    screen.blit(playerIMG_three, (x, y))


def player_four(x, y):
    screen.blit(playerIMG_four, (x, y))


finish_text = ""
font2 = pygame.font.SysFont("Papyrus", 65)
players_finished = []
next_level = 0
placings = ["1st", "2nd", "3rd", "4th"]


smallfont = pygame.font.SysFont("Papyrus", 15)
normalfont = pygame.font.SysFont("arial", 25)
differntfont = pygame.font.SysFont("futura", 25)

def level(next_level):
    level = normalfont.render("Level: "+ str(next_level), True, BLACK)
    screen.blit(level, [250, 10])

def score(score):
    text = smallfont.render("Race cars passing: " + str(score), True, RGREEN)
    screen.blit(text, [145, 490])



def text_objects(text, font):
    textSurface = font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()


def message_display(text):
    largText = pygame.font.Font("Mulish-Regular.ttf", 15)
    TextSurf, TextRect = text_objects(text, largText)
    TextRect.center = ((SCREENWIDTH / 1), (SCREENHEIGHT / 1))
    screen.blit(TextSurf, TextRect)

text_two = normalfont.render("Start new game?", 5, (0, 66, 37))
time_to_blit = None

pygame.display.flip()


def button(msg, x, y, w, h, iC, aC, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(screen, iC, (x, y, w, h))
        if click[0] == 1 and action != None:
            if action == "Play":
                game_loop()

            if action == "unpause":
                unpause()

            elif action == "Quit":

                pygame.quit()
                quit()

    else:
        pygame.draw.rect(screen, aC, (x, y, w, h))

    newtext = pygame.font.SysFont("arial", 25)
    textSurf, textReact = text_objects(msg, newtext)
    textReact.center = ((x + (100 / 2))), (y + (h / 2))
    screen.blit(textSurf, textReact)

    newtext = pygame.font.SysFont("arial", 25)
    textSurf, textReact = text_objects("QUIT!", newtext)
    textReact.center = ((260 + (100 / 2))), (40 + (50 / 2))
    screen.blit(textSurf, textReact)

def unpause():
    global pause
    pause = False

def paused():
    newtext = pygame.font.SysFont("arial", 25)
    textSurf, textReact = text_objects("paused", newtext)
    textReact.center = ((100 + (100 / 2))), (100 + (100 / 2))
    screen.blit(textSurf, textReact)
    screen.fill(WHITE)

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        screen.blit(pauseimg, (0, 1))
        button("   Continue!?", 40, 40, 125, 50, DARK_BLUE, BLUE, "unpause")
        button("QUIT!", 260, 40, 100, 50, LIGHT_RED, RED, "Quit")

        pygame.display.update()
        clock.tick(15)


def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.fill(BLACK)
        text = normalfont.render("Super Racer!", 8, (0, 66, 37))
        new_text = normalfont.render("By Rafa94", 8, (0, 66, 37))
        screen.blit(text, (35 - (text.get_width() / 5), 5))
        screen.blit(new_text, (300 - (text.get_width() / 5), 5))
        screen.blit(main_img, (5,340))
        screen.blit(main_img2, (85, 115))
        screen.blit(side_img, (330, 455))
        screen.blit(side_img2, (5, 445))


        button("GO!", 60, 40, 100, 50, DARK_BLUE, BLUE, "Play")
        button("QUIT!", 260, 40, 100, 50, LIGHT_RED, RED, "Quit")
        pygame.display.update()
        clock.tick(15)


# Main game loop
def game_loop():
    global pause
    global playerCar_position, playerCar_position_two, playerCar_position_three, playerCar_position_four
    global playerY, playerY_two, playerY_three, playerY_four, playerX, playerX_two, playerX_three, playerX_four
    finish_line_rect = pygame.Rect(50, 70, 235, 32)
    finish_text = ""
    players_finished = 0
    next_level = 0
    time_to_blit = 0


    run = True
    while run:

        # Drawing on Screen
        screen.fill(BLACK)
        # Draw The Road
        pygame.draw.rect(screen, GREY, [40, 0, 300, 500])
        # Draw Line painting on the road
        pygame.draw.line(screen, WHITE, [185, 0], [185, 500], 5)
        # Finish line
        pygame.draw.rect(screen, BLACKWHITE, [50, 50, 280, 40])
        pygame.draw.line(screen, WHITE, [50, 70], [330, 70], 5)
        font = pygame.font.SysFont("Impact", 20)
        text = font.render("Finish line!", 2, (150, 50, 25))
        screen.blit(text, (185 - (text.get_width() / 2), 45))
        screen.blit(bg, (-236, -34))
        screen.blit(bg, (-236, -5))
        screen.blit(bg, (-235, 140))
        screen.blit(bg, (-235, 240))
        screen.blit(bg, (-235, 340))
        screen.blit(bg, (340, -60))
        screen.blit(bg, (340, -60))
        screen.blit(bg, (335, 5))
        screen.blit(bg, (335, 130))
        screen.blit(bg, (335, 230))
        screen.blit(bg, (335, 330))
        screen.blit(bg, (333, 330))


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                # Number of frames per secong e.g. 60
                clock.tick(60)

            keys = pygame.key.get_pressed()

            if keys[pygame.K_1]:
                CarSound.play()
                playerCar_position = -0.5
            if keys[pygame.K_q]:
                playerCar_position = 0.5
            if keys[pygame.K_2]:
                CarSound_two.play()
                playerCar_position_two = -0.5
            if keys[pygame.K_w]:
                playerCar_position_two = 0.5
            if keys[pygame.K_3]:
                CarSound_three.play()
                playerCar_position_three = -0.5
            if keys[pygame.K_e]:
                playerCar_position_three = 0.5
            if keys[pygame.K_4]:
                CarSound_four.play()
                playerCar_position_four = -0.5
            if keys[pygame.K_r]:
                playerCar_position_four = 0.5
            if keys[pygame.K_SPACE]:
                pause = True

                paused()




        # our functions
        playerY += playerCar_position
        playerY_two += playerCar_position_two
        playerY_three += playerCar_position_three
        playerY_four += playerCar_position_four

        player(playerX, playerY)
        player_two(playerX_two, playerY_two)
        player_three(playerX_three, playerY_three)
        player_four(playerX_four, playerY_four)



        # Did anyone cross the line?
        if (finish_line_rect.collidepoint(playerX, playerY)):
            if finish_text[:8] != "Player 1":  # so it doesnt do this every frame the car is intersecting
                finish_text = "Player 1 is " + placings[players_finished]
                players_finished += 1
                print("Player (one) has crossed into finish line!")
                Crowds.play()


        elif (finish_line_rect.collidepoint(playerX_two, playerY_two)):
            if finish_text[:8] != "Player 2":
                print("Player one has crossed into finish line first other car lost!")
                finish_text = "Player 2 is " + placings[players_finished]
                players_finished += 1
                Crowds_three.play()


        elif (finish_line_rect.collidepoint(playerX_three, playerY_three)):
            if finish_text[:8] != "Player 3":
                print("Player two has crossed into finish line first other car lost!")
                finish_text = "Player 3 is " + placings[players_finished]
                players_finished += 1

        elif (finish_line_rect.collidepoint(playerX_four, playerY_four)):
            if finish_text[:8] != "Player 4":
                print("Player two has crossed into finish line first other car lost!")
                finish_text = "Player 4 is " + placings[players_finished]
                players_finished += 1
                Crowds_two.play()

        if (players_finished and finish_text):
            #print("ft:", finish_text)

            font = pygame.font.SysFont("Impact", 17)
            textrect = font.render(finish_text, False, (0, 66, 37))
            #print('x', (SCREENWIDTH - text.get_width()) / 2)
            screen.blit(textrect, (65 - (text.get_width() / 5), -2))
            #screen.blit(textrect, ((SCREENWIDTH - textrect.get_width()) // 2, -5))

        if (finish_line_rect.collidepoint and players_finished):
            #pygame.mixer.final_tone.play(-1)
            final_tone.play()
            pygame.mixer.music.play(0)

        if (finish_text):
            font = pygame.font.SysFont("Impact", 20)
            text = font.render('Game Over!!!', 5, (0, 66, 37))
            screen.blit(text, (250 - (text.get_width() / 5), -2))

        if players_finished == 4:
            time_to_blit = pygame.time.get_ticks() + 5000

        if time_to_blit:
            screen.blit(text_two, (100, 345))
            #final_tone.play()
            if pygame.time.get_ticks() >= time_to_blit:
                time_to_blit = 0

        if players_finished == 4:
            next_level = 1

        score(players_finished)
        level(next_level)




        pygame.display.update()
        clock.tick(60)

game_intro()





pygame.quit()