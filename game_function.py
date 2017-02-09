import sys
import time

import pygame

from snake import SnakePart
from food import Food


def draw_screen(settings, stats, screen, scoreboard, snake_head, snake_parts, foods):
    screen.fill(settings.bg_color)

    snake_parts.draw(screen)
    snake_head.blitme()
    foods.draw(screen)
    scoreboard.show_score(stats)

    pygame.display.flip()

    if stats.bonus:
        time.sleep(1)
        bonus(settings, screen, stats, snake_head, snake_parts, foods)
        stats.bonus = False


def update_snake(settings, screen, stats, snake_head, snake_parts):
    # 依据长度删除多余的身体
    for part in snake_parts.copy():
        if not part.check_alive(stats.snake_length):
            snake_parts.remove(part)

    # 产生新的身体部分
    snake_part = SnakePart(snake_head, screen)
    snake_parts.add(snake_part)

    snake_head.update()


def update_food(settings, stats, screen, snake_head, snake_parts, foods):
    while len(foods) < settings.food_limit:
        food = Food(screen, settings)
        food.random_pos(snake_head, snake_parts, foods)
        foods.add(food)

        if check_bonus(settings, food, foods):
            stats.bonus = True


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
        stats.foods_eaten += 1
        stats.score += food.points * settings.level
        foods.remove(food)

        settings.update_level(stats)


def check_bonus(settings, food, foods):
    if len(foods) == settings.food_limit:
        food_style1 = food.style
        for food in foods:
            if food.style != food_style1:
                return False
        return True


def bonus(settings, screen, stats, snake_head, snake_parts, foods):
    # 加分
    stats.score += settings.bonus_points * settings.level

    # 增加食物
    while len(foods) < settings.bonus_food:
        food = Food(screen, settings)
        food.random_pos(snake_head, snake_parts, foods)
        foods.add(food)

    # 将蛇长度缩短
    for part in snake_parts.copy():
        if not part.check_alive(stats.snake_length - settings.bonus_cut_length):
            snake_parts.remove(part)
