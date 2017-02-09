from random import randint

import pygame
from pygame.sprite import Sprite


class Food(Sprite):
    def __init__(self, screen, settings):
        super(Food, self).__init__()
        self.screen = screen
        self.settings = settings

        # 获取图像
        self.image = pygame.image.load('images/food' + str(randint(1, 7)) + '.bmp')
        self.rect = self.image.get_rect()

        # 初始化位置
        self.rect.topleft = (0, 0)

    def random_pos(self, snake_head, snake_parts):
        while True:
            self.rect.left = randint(0, self.settings.x - 1) * self.settings.len
            self.rect.top = randint(0, self.settings.y - 1) * self.settings.len
            if not pygame.sprite.spritecollideany(self, snake_parts)\
                    and not self.rect.colliderect(snake_head):
                break
