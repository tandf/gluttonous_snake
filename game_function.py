import sys

import pygame

from snake import SnakeHead


def update_screen(settings, screen, snake_head):
    screen.fill(settings.bg_color)

    snake_head.update()
    snake_head.blitme()
    pygame.display.flip()


def check_event(settings, screen, snake_head):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                if snake_head.facing != "up":
                    snake_head.facing = "down"
            elif event.key == pygame.K_UP:
                if snake_head.facing != "down":
                    snake_head.facing = "up"
            elif event.key == pygame.K_LEFT:
                if snake_head.facing != "right":
                    snake_head.facing = "left"
            elif event.key == pygame.K_RIGHT:
                if snake_head.facing != "left":
                    snake_head.facing = "right"
