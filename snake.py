import pygame
from pygame.sprite import Sprite


class SnakeHead:
    def __init__(self, settings, screen):
        self.settings = settings
        self.screen = screen

        self.image_up = pygame.image.load('images/head_up.bmp')
        self.image_down = pygame.image.load('images/head_down.bmp')
        self.image_left = pygame.image.load('images/head_left.bmp')
        self.image_right = pygame.image.load('images/head_right.bmp')

        self.image = self.image_up
        self.rect = self.image.get_rect()

        self.rect.topleft = (settings.len * 20, settings.len * 20)
        self.facing = "up"

    def update(self):
        if self.facing == "up":
            self.rect.y -= self.settings.len
            self.image = self.image_up
            if self.rect.y < 0:
                self.rect.y += self.settings.bit[1]
        elif self.facing == "down":
            self.rect.y += self.settings.len
            self.image = self.image_down
            if self.rect.y >= self.settings.bit[1]:
                self.rect.y -= self.settings.bit[1]
        elif self.facing == "left":
            self.rect.x -= self.settings.len
            self.image = self.image_left
            if self.rect.x < 0:
                self.rect.x += self.settings.bit[0]
        elif self.facing == "right":
            self.rect.x += self.settings.len
            self.image = self.image_right
            if self.rect.x >= self.settings.bit[0]:
                self.rect.x -= self.settings.bit[0]

    def blitme(self):
        self.screen.blit(self.image, self.rect)


class SnakePart(Sprite):
    def __init__(self, snake_head, screen):
        super(SnakePart, self).__init__()
        self.screen = screen

        # 加载图像并获取rect
        self.image = pygame.image.load('images/body.bmp')
        self.rect = self.image.get_rect()

        # 加载尾部图像
        if snake_head.facing == "up":
            self.tail_image = pygame.image.load('images/tail_up.bmp')
        elif snake_head.facing == "down":
            self.tail_image = pygame.image.load('images/tail_down.bmp')
        elif snake_head.facing == "left":
            self.tail_image = pygame.image.load('images/tail_left.bmp')
        elif snake_head.facing == "right":
            self.tail_image = pygame.image.load('images/tail_right.bmp')

        # 身体的位置即为头的位置
        self.rect.topleft = snake_head.rect.topleft

        # 寿命
        self.life = 1

    def check_alive(self, snake_length):
        if self.life >= snake_length:
            return False
        else:
            self.life += 1
            if self.life == snake_length:
                self.image = self.tail_image
            return True
