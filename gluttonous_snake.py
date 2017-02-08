import time

import pygame

from settings import Settings
import game_function as gf

from snake import SnakeHead

def run_game():
    # 初始化游戏
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode(settings.bit)
    pygame.display.set_caption("Gluttonous Snake")

    snake_head = SnakeHead(settings, screen)

    last_time = time.time()

    # 开始游戏主循环
    while True:

        gf.check_event(settings, screen, snake_head)
        if time.time() - last_time >= settings.interval:
            gf.update_screen(settings, screen, snake_head)
            last_time = time.time()

run_game()
