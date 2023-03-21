# importing the brick,ball and reflector class
import pygame
from reflector import Reflector
from ball import Ball
from brick import Brick
import math
import sys

pygame.init()
mainClock = pygame.time.Clock()
from pygame.locals import *
 
# Height and width of the Main window
WIDTH, HEIGHT = 850, 550

win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("BRICS Game")

reflector_width = 100
velocity=5
REFLECTOR_HEIGHT = 15

# No. of rows of brick in the GamePlay_window
nbrick=2

BALL_RADIUS = 10

# Universal fonts that is used every where the code
LIVES_FONT = pygame.font.SysFont("comicsans", 30)
font = pygame.font.SysFont(None, 30)
clock = pygame.time.Clock()

#initial lives the score
lives = 3
score = 0

def draw(win, reflector, ball, bricks, lives):
    '''This function is draw each component of the GamePlay_window'''
    win.fill("white") 
    reflector.draw(win)  # draw function from reflector.py
    ball.draw(win)

    for brick in bricks:
        brick.draw(win)

    lives_text = LIVES_FONT.render(f"Lives: {lives}", 1, "red")
    score_text = LIVES_FONT.render(f"Score: {score}", 1, "#013220")
    win.blit(lives_text, (10, HEIGHT - lives_text.get_height() - 10))
    win.blit(score_text, (WIDTH - 10 - score_text.get_width(), HEIGHT - lives_text.get_height() - 10))
    pygame.display.update()

# Sets the ball coordinate to initial coordinates after collision
def ball_collision(ball):
    if ball.x - BALL_RADIUS <= 0 or ball.x + BALL_RADIUS >= WIDTH:
        ball.set_vel(ball.x_vel * -1, ball.y_vel)
    if ball.y + BALL_RADIUS >= HEIGHT or ball.y - BALL_RADIUS <= 0:
        ball.set_vel(ball.x_vel, ball.y_vel * -1)


def ball_reflector_collision(ball, reflector):
    '''ball reflector collision mechanism'''
    if not (ball.x <= reflector.x + reflector.width and ball.x >= reflector.x):
        return
    if not (ball.y + ball.radius >= reflector.y):
        return

    reflector_center = reflector.x + reflector.width/2
    distance_to_center = ball.x - reflector_center

    percent_width = distance_to_center / reflector.width
    angle = percent_width * 90
    angle_radians = math.radians(angle)

    x_vel = math.sin(angle_radians) * ball.VEL
    y_vel = math.cos(angle_radians) * ball.VEL * -1

    ball.set_vel(x_vel, y_vel)


def generate_bricks(rows, cols):
    '''for generating bricks in the GamePlay_window'''
    gap = 2
    brick_width = WIDTH // cols - gap
    brick_height = 25

    bricks = []
    for row in range(rows):
        for col in range(cols):
            brick = Brick(col * brick_width + gap * col, row * brick_height +
                          gap * row, brick_width, brick_height, 2, [(82, 217, 239), (255, 186, 197)])
            bricks.append(brick)

    return bricks

def display_text(text, color):
    ''' Used to display text in menus'''
    text_render = LIVES_FONT.render(text, 1, color)
    win.blit(text_render, (WIDTH/2 - text_render.get_width() /
                           2, HEIGHT/2 - text_render.get_height()/2))
    pygame.display.update()
    pygame.time.delay(3000)

# Used to display text in menus
def draw_text(text, font, color, surface, x, y):
    '''This function is created to show text, used in option() function'''
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    win.blit(textobj, textrect)

click = False

def options():
    ''' This function defines the Level_window'''
    global reflector_width
    global nbrick
    global velocity
    running = True
    while running:

        win.fill("white")
        draw_text('LEVEL', font, (0,0,0),win, 395, 80)

        #creating buttons
        button_1 = pygame.Rect(320, 140, 200, 50)
        button_2 = pygame.Rect(320, 230, 200, 50)
        button_3 = pygame.Rect(320, 325, 200, 50)

        #defining functions when a certain button is pressed
        
                # running=False

        pygame.draw.rect(win,"#D27685", button_1)
        pygame.draw.rect(win, "#D27685", button_2)
        pygame.draw.rect(win, "#D27685", button_3)
        #writing text on top of button
        draw_text('Easy', font, (255,255,255), win, 400, 155)
        draw_text('Medium', font, (255,255,255), win, 385, 250)
        draw_text('Hard', font, (255,255,255), win, 400, 340)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                click=True
                mx, my = pygame.mouse.get_pos()
                if button_1.collidepoint((mx, my)):
                    if click:
                        reflector_width = 120
                        nbrick=2
                        running=False
                if button_2.collidepoint((mx, my)):
                    if click:
                        reflector_width = 90
                        nbrick=4
                        velocity=7
                        running=False
                if button_3.collidepoint((mx, my)):
                    if click:
                        reflector_width = 70
                        nbrick=7
                        velocity=9
                        running=False
       
        pygame.display.update()
        mainClock.tick(60)

def drawmainmenu():
    ''' This function defines mainMenu_window'''
    global reflector_width
    global nbrick
    global velocity
    st=True
    while st:
        win.fill("white")
        draw_text('Main Menu', font, (0,0,0),win, 365, 80)
        mx, my = pygame.mouse.get_pos()
        #creating buttons
        button_1 = pygame.Rect(315, 140, 200, 50)
        button_2 = pygame.Rect(315, 230, 200, 50)
        button_3 = pygame.Rect(315, 325, 200, 50)

        #defining functions when a certain button is pressed
        if button_1.collidepoint((mx, my)):
            if click:
                st=False
        if button_2.collidepoint((mx, my)):
            if click:
                options()
                st=False
        if button_3.collidepoint((mx, my)):
            if click:
                pygame.quit()
                sys.quit()
        pygame.draw.rect(win,"#D27685", button_1)
        pygame.draw.rect(win, "#D27685", button_2)
        pygame.draw.rect(win, "#D27685", button_3)
 
        #writing text on top of button
        draw_text('PLAY', font, (255,255,255), win, 385, 155)
        draw_text('LEVEL', font, (255,255,255), win, 385, 250)
        draw_text('EXIT', font, (255,255,255), win, 385, 340)

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
 
        pygame.display.update()
        mainClock.tick(60)

def reset():
    '''It resets the game when game is over'''
    reflector.x = reflector_x
    reflector.y = reflector_y
    ball.x = WIDTH/2
    ball.y = reflector_y - BALL_RADIUS

# Initializing 
drawmainmenu()
reflector_x = WIDTH/2 - reflector_width/2
reflector_y = HEIGHT - REFLECTOR_HEIGHT - 5
ball = Ball(WIDTH/2, reflector_y - BALL_RADIUS, BALL_RADIUS, "black",velocity)
bricks = generate_bricks(nbrick, 10)
reflector = Reflector(reflector_x, reflector_y, reflector_width, REFLECTOR_HEIGHT, (60, 63, 65))


# Main execution of the program
run = True
while run:

    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and reflector.x - reflector.VEL >= 0:
        reflector.move(-1)
    if keys[pygame.K_RIGHT] and reflector.x + reflector.width + reflector.VEL <= WIDTH:
        reflector.move(1)

    ball.move()
    ball_collision(ball)
    ball_reflector_collision(ball, reflector)

    for brick in bricks[:]:
        brick.collide(ball)

        if brick.health <= 0:
            bricks.remove(brick)
            score += 1

        # lives check
    if ball.y + ball.radius >= HEIGHT:
        lives -= 1
        pygame.time.delay(1000)
        ball.x = reflector.x + reflector.width/2
        ball.y = reflector.y - BALL_RADIUS
        ball.set_vel(0, ball.VEL * -1)

    if lives <= 0:
        bricks = generate_bricks(nbrick, 10)
        lives = 3
        score = 0
        display_text("GAME OVER", "red")

        reset()
        
    if len(bricks) == 0:
        bricks = generate_bricks(nbrick, 10)
        lives = 3
        score=0
        display_text("YOU WON", "green")
        reset()

    draw(win, reflector, ball, bricks, lives)

pygame.quit()
quit()
