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

# display
WIDTH, HEIGHT = 1920, 1080
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cookie Clicker")

# clock
clock = pygame.time.Clock()

# fonts
font = pygame.font.Font(None, 36)

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# variables
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

# images
cookie_img = pygame.image.load(os.path.join("cookie_clicker_os_game", "assets", "cookie.png"))
cookie_img = pygame.transform.scale(cookie_img, (200, 200))

# sounds
click_sound = pygame.mixer.Sound(os.path.join("cookie_clicker_os_game", "assets", "click.wav"))
click_sound.set_volume(0.5)
buy_sound = pygame.mixer.Sound(os.path.join("cookie_clicker_os_game", "assets", "buy.wav"))
buy_sound.set_volume(0.5)

# functions
def draw_text(text, font, color, x, y):
    img = font.render(text, True, color)
    screen.blit(img, (x, y))

# main menu
def main_menu():
    while True:
        screen.fill(WHITE)
        draw_text("Main Menu", font, BLACK, 20, 20)

        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 - 50, 200, 50)
        button_2 = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 + 50, 200, 50)

        if button_1.collidepoint((mx, my)):
            if click:
                game()
        if button_2.collidepoint((mx, my)):
            if click:
                pygame.quit()
                sys.exit()

        pygame.draw.rect(screen, RED, button_1)
        pygame.draw.rect(screen, RED, button_2)

        draw_text("Start", font, BLACK, WIDTH // 2 - 30, HEIGHT // 2 - 40)
        draw_text("Quit", font, BLACK, WIDTH // 2 - 30, HEIGHT // 2 + 60)

        click = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        clock.tick(30)

# shop
def shop():
    global cookie_count, click_power, click_power_cost, auto_clicker_cost, auto_clicker_power, auto_clicker, auto_clicker_time, auto_clicker_time_cost, auto_clicker_time_max, auto_clicker_time_min

    running = True
    while running:
        screen.fill(WHITE)
        draw_text("Shop", font, BLACK, 20, 20)

        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 - 100, 200, 50)
        button_2 = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 - 50, 200, 50)
        button_3 = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2, 200, 50)
        button_4 = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 + 50, 200, 50)
        button_5 = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 + 100, 200, 50)
        button_6 = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 + 150, 200, 50)

        if button_1.collidepoint((mx, my)):
            if click:
                if cookie_count >= click_power_cost:
                    click_power += 1
                    cookie_count -= click_power_cost
                    click_power_cost = math.ceil(click_power_cost * 1.5)
                    buy_sound.play()
        if button_2.collidepoint((mx, my)):
            if click:
                if cookie_count >= auto_clicker_cost:
                    auto_clicker += 1
                    cookie_count -= auto_clicker_cost
                    auto_clicker_cost = math.ceil(auto_clicker_cost * 1.5)
                    buy_sound.play()
        if button_3.collidepoint((mx, my)):
            if click:
                if cookie_count >= auto_clicker_time_cost:
                    auto_clicker_time += 1
                    cookie_count -= auto_clicker_time_cost
                    auto_clicker_time_cost = math.ceil(auto_clicker_time_cost * 1.5)
                    buy_sound.play()
        if button_4.collidepoint((mx, my)):
            if click:
                if auto_clicker_time > auto_clicker_time_min:
                    auto_clicker_time -= 1
                    cookie_count += auto_clicker_time_cost // 2
                    auto_clicker_time_cost = math.ceil(auto_clicker_time_cost / 1.5)
                    buy_sound.play()
        if button_5.collidepoint((mx, my)):
            if click:
                running = False
        if button_6.collidepoint((mx, my)):
            if click:
                pygame.quit()
                sys.exit()

        pygame.draw.rect(screen, RED, button_1)
        pygame.draw.rect(screen, RED, button_2)
        pygame.draw.rect(screen, RED, button_3)
        pygame.draw.rect(screen, RED, button_4)
        pygame.draw.rect(screen, RED, button_5)
        pygame.draw.rect(screen, RED, button_6)

        draw_text("Upgrade Click Power - " + str(click_power_cost), font, BLACK, WIDTH // 2 - 90, HEIGHT // 2 - 90)
        draw_text("Buy Auto Clicker - " + str(auto_clicker_cost), font, BLACK, WIDTH // 2 - 90, HEIGHT // 2 - 40)
        draw_text("Upgrade Auto Clicker Time - " + str(auto_clicker_time_cost), font, BLACK, WIDTH // 2 - 90, HEIGHT // 2 + 10)
        draw_text("Sell Auto Clicker Time - " + str(auto_clicker_time_cost // 2), font, BLACK, WIDTH // 2 - 90, HEIGHT // 2 + 60)
        draw_text("Back", font, BLACK, WIDTH // 2 - 30, HEIGHT // 2 + 110)
        draw_text("Quit", font, BLACK, WIDTH // 2 - 30, HEIGHT // 2 + 160)

        click = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        clock.tick(30)

# game

def game():
    global cookie_count, click_power, auto_clicker_cost, auto_clicker_power, auto_clicker, auto_clicker_time, auto_clicker_time_cost, auto_clicker_time_max, auto_clicker_time_min

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

    last_auto_click_time = pygame.time.get_ticks()

    running = True
    while running:
        screen.fill(WHITE)
        draw_text("Cookie Count: " + str(cookie_count), font, BLACK, 20, 20)
        draw_text("Click Power: " + str(click_power), font, BLACK, 20, 60)
        draw_text("Auto Clicker: " + str(auto_clicker), font, BLACK, 20, 100)
        draw_text("Auto Clicker Time: " + str(auto_clicker_time), font, BLACK, 20, 140)

        mx, my = pygame.mouse.get_pos()

        cookie_rect = cookie_img.get_rect(center = (WIDTH // 2, HEIGHT // 2))
        screen.blit(cookie_img, cookie_rect)

        button_1 = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 + 100, 200, 50)
        button_2 = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 + 150, 200, 50)
        button_3 = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 + 200, 200, 50)

        if button_1.collidepoint((mx, my)):
            if click:
                cookie_count += click_power
                click_sound.play()
        if button_2.collidepoint((mx, my)):
            if click:
                cookie_count += auto_clicker_power
                click_sound.play()
        if button_3.collidepoint((mx, my)):
            if click:
                shop()

        pygame.draw.rect(screen, RED, button_1)
        pygame.draw.rect(screen, RED, button_2)
        pygame.draw.rect(screen, RED, button_3)

        draw_text("Click", font, BLACK, WIDTH // 2 - 30, HEIGHT // 2 + 110)
        draw_text("Auto Click", font, BLACK, WIDTH // 2 - 50, HEIGHT // 2 + 160)
        draw_text("Shop", font, BLACK, WIDTH // 2 - 30, HEIGHT // 2 + 210)

        click = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if auto_clicker > 0:
            current_time = pygame.time.get_ticks()
            if current_time - last_auto_click_time >= auto_clicker_time * 1000:
                cookie_count += auto_clicker_power * auto_clicker
                last_auto_click_time = current_time

        pygame.display.update()
        clock.tick(30)
main_menu()


pygame.quit()
sys.exit()
