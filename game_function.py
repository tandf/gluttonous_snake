import sys

import pygame

from snake import SnakePart


def update_screen(settings, screen, snake_head, snake_parts):
    screen.fill(settings.bg_color)

    snake_head.blitme()
    snake_parts.draw(screen)
    pygame.display.flip()


def update_snake(settings, screen, stats, snake_head, snake_parts):
    # 依据长度删除多余的身体
    for part in snake_parts.copy():
        if not part.check_alive(stats.snake_length):
            snake_parts.remove(part)

    # 产生新的身体部分
    snake_part = SnakePart(snake_head.rect.topleft, screen)
    snake_parts.add(snake_part)

    snake_head.update()


def check_event(settings, screen, stats, snake_head):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_key_down(event, stats, snake_head)


def check_key_down(event, stats, snake_head):
    if event.key == pygame.K_ESCAPE:
        sys.exit()
    elif event.key == pygame.K_p:
        if stats.pause_game:
            stats.pause_game = False
        else:
            stats.pause_game = True
    elif not stats.moved and not stats.pause_game:
        if event.key == pygame.K_s:
            if snake_head.facing != "up":
                snake_head.facing = "down"
                stats.moved = True
        elif event.key == pygame.K_w:
            if snake_head.facing != "down":
                snake_head.facing = "up"
                stats.moved = True
        elif event.key == pygame.K_a:
            if snake_head.facing != "right":
                snake_head.facing = "left"
                stats.moved = True
        elif event.key == pygame.K_d:
            if snake_head.facing != "left":
                snake_head.facing = "right"
                stats.moved = True
