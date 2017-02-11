from random import randint
import time

import pygame
from pygame.sprite import Sprite


class Food(Sprite):
    def __init__(self, screen, settings):
        super(Food, self).__init__()
        self.screen = screen
        self.settings = settings

        # 获取图像
        self.style = str(randint(1, 7))
        self.image = pygame.image.load('images/food' + str(self.style) + '.bmp')
        self.rect = self.image.get_rect()

        # 初始化位置
        self.rect.topleft = (0, 0)

        # 获取分值
        self.points = self.settings.normal_points

    def random_pos(self, snake_head, snake_parts, foods):
        while True:
            if self.style != 'big':
                self.rect.left = randint(0, self.settings.x - 1) * self.settings.len
                self.rect.top = randint(0, self.settings.y - 1) * self.settings.len + self.settings.scoreboard_height
            else:
                self.rect.left = randint(0, self.settings.x - 4) * self.settings.len
                self.rect.top = randint(0, self.settings.y - 4) * self.settings.len + self.settings.scoreboard_height

            # 随机位置直到不与蛇、其他食物重叠
            if not pygame.sprite.spritecollideany(self, snake_parts)\
                    and not self.rect.colliderect(snake_head)\
                    and not pygame.sprite.spritecollideany(self, foods):
                break

    def become_big(self, snake_head, snake_parts, foods):
        self.image = pygame.image.load('images/big_food.bmp')
        self.rect = self.image.get_rect()

        # 获取分值
        self.points = self.settings.big_points
        self.style = 'big'
        self.random_pos(snake_head, snake_parts, foods)

        # 初始化倒计时
        self.start_time = time.time()
        self.existing_time = 0
        self.font = pygame.font.SysFont(None, 45)

    def update_countdown(self):
        self.existing_time = int((time.time() - self.start_time) / 0.3)
        msg = str(10 - self.existing_time)

        self.msg_image = self.font.render(msg, True, (50, 50, 50))
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

        self.points = self.settings.big_points * (10 - self.existing_time) / 10

    def show_countdown(self):
        self.screen.blit(self.msg_image, self.msg_image_rect)

    def bonus_mode(self):
        self.image = pygame.image.load('images/food_bonus.bmp')
        self.style = 'bonus'
