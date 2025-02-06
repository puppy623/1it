# this is a clicker game made in python using the pygame library

import pygame
import sys
import os
import time
import random
import math
from pygame.locals import *

# initialize pygame
pygame.init()

# set up display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cookie Clicker")

# set up clock
clock = pygame.time.Clock()

# set up fonts
font = pygame.font.Font(None, 36)

# set up colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# set up variables
cookie_count = 0
click_power = 1
click_power_cost = 10
auto_clicker_cost = 100
auto_clicker_power = 1
auto_clicker = 0
auto_clicker_time = 1
auto_clicker_time_cost = 1000
auto_clicker_time_max = 10
auto_clicker_time_min = 1

# set up images
cookie_img = pygame.image.load(os.path.join("cookie_clicker_os_game", "assets", "cookie.png"))
cookie_img = pygame.transform.scale(cookie_img, (200, 200))

# set up sounds
click_sound = pygame.mixer.Sound(os.path.join("cookie_clicker_os_game", "assets", "click.wav"))
click_sound.set_volume(0.5)
buy_sound = pygame.mixer.Sound(os.path.join("cookie_clicker_os_game", "assets", "buy.wav"))
buy_sound.set_volume(0.5)

# set up functions
def draw_text(text, font, color, x, y):
    img = font.render(text, True, color)
    screen.blit(img, (x, y))



# main loop
run = True

while run:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                cookie_count += click_power
                click_sound.play()

    # fill the screen with white
    screen.fill(WHITE)

    # draw the cookie
    screen.blit(cookie_img, (WIDTH // 2 - 100, HEIGHT // 2 - 100))

    # draw the cookie count
    draw_text(f"Cookies: {cookie_count}", font, BLACK, 20, 20)

    # update the display
    pygame.display.update()

    # cap the frame rate
    clock.tick(60)