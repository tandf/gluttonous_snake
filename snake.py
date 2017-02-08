import pygame
from pygame.sprite import Sprite


class SnakeHead:
    def __init__(self, settings, screen):
        self.settings = settings
        self.screen = screen

        self.image = pygame.image.load('images/bit.bmp')
        self.rect = self.image.get_rect()

        self.rect.topleft = (settings.len * 20, settings.len * 20)
        self.facing = "up"

    def update(self):
        if self.facing == "up":
            self.rect.y -= self.settings.len
            if self.rect.y < 0:
                self.rect.y += self.settings.bit[1]
        elif self.facing == "down":
            self.rect.y += self.settings.len
            if self.rect.y >= self.settings.bit[1]:
                self.rect.y -= self.settings.bit[1]
        elif self.facing == "left":
            self.rect.x -= self.settings.len
            if self.rect.x < 0:
                self.rect.x += self.settings.bit[0]
        elif self.facing == "right":
            self.rect.x += self.settings.len
            if self.rect.x >= self.settings.bit[0]:
                self.rect.x -= self.settings.bit[0]

    def blitme(self):
        self.screen.blit(self.image, self.rect)
