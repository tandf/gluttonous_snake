import pygame


class Info:
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.text_color = (100, 100, 100)
        self.font = pygame.font.SysFont(None, 30)

        self.line1 = "Esc:          exit"
        self.line2 = "W A S D:      move"
        self.line3 = "P:            start/pause/resume"

        self.line1_image = self.font.render(self.line1, True, self.text_color)
        self.line1_rect = self.line1_image.get_rect()
        self.line2_image = self.font.render(self.line2, True, self.text_color)
        self.line2_rect = self.line1_image.get_rect()
        self.line3_image = self.font.render(self.line3, True, self.text_color)
        self.line3_rect = self.line1_image.get_rect()

        self.line1_rect.left = self.line2_rect.left = self.line3_rect.left = 50
        self.line1_rect.top = 250
        self.line2_rect.top = self.line1_rect.bottom + 10
        self.line3_rect.top = self.line2_rect.bottom + 10

    def show(self):
        self.screen.blit(self.line1_image, self.line1_rect)
        self.screen.blit(self.line2_image, self.line2_rect)
        self.screen.blit(self.line3_image, self.line3_rect)

