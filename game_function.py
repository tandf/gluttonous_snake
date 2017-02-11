import sys
import time
from random import randint

import pygame

from snake import SnakePart
from food import Food


def draw_screen(settings, stats, screen, scoreboard, snake_head, snake_parts, foods, info):
    screen.fill(settings.bg_color)

    if stats.game_active:
        snake_parts.draw(screen)
        snake_head.blitme()
        foods.draw(screen)
        draw_countdown(foods)
        draw_scoreboard(stats, scoreboard)

    else:
        info.show()

    pygame.display.flip()

    if stats.bonus:
        time.sleep(1)
        bonus(settings, screen, stats, snake_head, snake_parts, foods)
        stats.bonus = False


def draw_scoreboard(stats, scoreboard):
    scoreboard.draw_bg()
    scoreboard.show_score(stats)


def draw_countdown(foods):
    for food in foods:
        if food.style == 'big':
            food.show_countdown()


def update_snake(screen, stats, snake_head, snake_parts):
    # 依据长度删除多余的身体
    for part in snake_parts.copy():
        if not part.check_alive(stats.snake_length):
            snake_parts.remove(part)

    # 产生新的身体部分
    snake_part = SnakePart(snake_head, screen)
    snake_parts.add(snake_part)

    # 生成尾部图像
    change_image = find_the_last_part(snake_parts)
    change_image.image = change_image.tail_image

    snake_head.update()


def update_food(settings, stats, screen, snake_head, snake_parts, foods):
    # 生成食物
    while len(foods) < settings.food_limit:
        food = Food(screen, settings)
        food.random_pos(snake_head, snake_parts, foods)

        # 变大？
        if len(foods) == settings.food_limit - 1 and not check_big_food(foods):
            if randint(1, settings.big_food_chance) == 1:
                food.become_big(snake_head, snake_parts, foods)
        foods.add(food)

        # 产生bonus？
        if check_bonus(settings, food, foods):
            stats.bonus = True

    # 加载大食物的countdown
    for food in foods:
        if food.style == 'big':
            food.update_countdown()
            if food.existing_time > 9:
                foods.remove(food)
            break


def check_event(stats, snake_head, snake_parts, foods):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_key_down(event, stats, snake_head, snake_parts, foods)


def check_key_down(event, stats, snake_head, snake_parts, foods):
    if event.key == pygame.K_ESCAPE:
        sys.exit()
    elif event.key == pygame.K_p:
        if stats.game_active:
            if stats.pause_game:
                stats.pause_game = False
            else:
                stats.pause_game = True
        else:
            stats.game_active = True
            stats.first_start = False

            initialize_game(stats, snake_head, snake_parts, foods)

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
        time.sleep(2)
        stats.game_active = False

    # 检测吃到食物
    food = pygame.sprite.spritecollideany(snake_head, foods)
    if food:
        stats.snake_length += 1
        stats.foods_eaten += 1
        stats.score += food.points * stats.level
        foods.remove(food)

        stats.update_level(settings)


def check_bonus(settings, food, foods):
    if len(foods) == settings.food_limit:
        food_style1 = food.style
        for food in foods:
            if food.style != food_style1:
                return False
        return True


def check_big_food(foods):
    for food in foods:
        if food.style == 'big':
            return True
    return False


def find_the_last_part(snake_parts):
    for part in snake_parts:
        the_last = True
        for part_to_compare in snake_parts:
            if part.life < part_to_compare.life:
                the_last = False
                break
        if the_last:
            return part


def bonus(settings, screen, stats, snake_head, snake_parts, foods):
    # 加分
    stats.score += settings.bonus_points * stats.level

    # 增加食物
    while len(foods) < settings.bonus_food:
        food = Food(screen, settings)
        food.random_pos(snake_head, snake_parts, foods)
        foods.add(food)

    # 将蛇长度缩短
    if stats.snake_length > settings.bonus_cut_length:
        stats.snake_length -= settings.bonus_cut_length
    else:
        stats.snake_length = 1

    for part in snake_parts.copy():
        if not part.check_alive(stats.snake_length):
            snake_parts.remove(part)


def initialize_game(stats, snake_head, snake_parts, foods):
    stats.initialize()
    snake_head.initialize()
    snake_parts.empty()
    foods.empty()
