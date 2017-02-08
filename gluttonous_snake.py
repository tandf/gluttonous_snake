import time

import pygame
from pygame.sprite import Group

from settings import Settings
from stats import Stats
import game_function as gf
from snake import SnakeHead


def run_game():
    # 初始化游戏
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode(settings.bit)
    pygame.display.set_caption("Gluttonous Snake")

    # 存储游戏信息的实例
    stats = Stats(settings)

    snake_head = SnakeHead(settings, screen)
    snake_parts = Group()

    last_time = time.time()

    # 开始游戏主循环
    while True:

        gf.check_event(settings, screen, stats, snake_head)

        if time.time() - last_time >= settings.interval and not stats.pause_game:
            gf.update_snake(settings, screen, stats, snake_head, snake_parts)
            last_time = time.time()
            stats.moved = False

        gf.update_screen(settings, screen, snake_head, snake_parts)

run_game()