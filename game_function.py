import sys

import pygame

from snake import SnakePart
from food import Food


def update_screen(settings, screen, snake_head, snake_parts, foods):
    screen.fill(settings.bg_color)

    snake_parts.draw(screen)
    snake_head.blitme()
    foods.draw(screen)

    pygame.display.flip()


def update_snake(settings, screen, stats, snake_head, snake_parts):
    # 依据长度删除多余的身体
    for part in snake_parts.copy():
        if not part.check_alive(stats.snake_length):
            snake_parts.remove(part)

    # 产生新的身体部分
    snake_part = SnakePart(snake_head, screen)
    snake_parts.add(snake_part)

    snake_head.update()


def update_food(settings, screen, snake_head, snake_parts, foods):
    while len(foods) < settings.food_limit:
        food = Food(screen, settings)
        food.random_pos(snake_head, snake_parts)
        foods.add(food)


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


def check_collision(settings, stats, snake_head, snake_parts, foods):
    # 检测头部撞到身体
    if pygame.sprite.spritecollideany(snake_head, snake_parts):
        stats.game_active = False

    # 检测吃到食物
    food = pygame.sprite.spritecollideany(snake_head, foods)
    if food:
        stats.snake_length += 1
        foods.remove(food)
