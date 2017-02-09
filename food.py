from random import randint

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
        self.points = settings.normal_points

    def random_pos(self, snake_head, snake_parts, foods):
        while True:
            self.rect.left = randint(0, self.settings.x - 1) * self.settings.len
            self.rect.top = randint(0, self.settings.y - 1) * self.settings.len + self.settings.scoreboard_height

            # 随机位置直到不与蛇、其他食物重叠
            if not pygame.sprite.spritecollideany(self, snake_parts)\
                    and not self.rect.colliderect(snake_head)\
                    and not pygame.sprite.spritecollideany(self, foods):
                break
