import pygame


class Info:
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.text_color = (100, 100, 100)
        self.font = pygame.font.SysFont(None, 30)
        self.score_font = pygame.font.SysFont(None, 50)

        self.line1 = "Esc:             exit"
        self.line2 = "W A S D:      move"
        self.line3 = "P:                 start/pause/resume"

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

    def prep_score(self, stats):
        self.score_image = self.score_font.render("Your score: " + "{:,}".format(int(stats.score)),
                                                  True, self.text_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.centerx = self.screen_rect.centerx
        self.score_rect.bottom = self.high_score_rect.top - 10

    def prep_high_score(self, stats):
        self.high_score_image = self.font.render("HIGHEST: " + "{:,}".format(int(stats.high_score)),
                                                 True, self.text_color)
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.bottom = self.line1_rect.top - 50

    def show(self, stats):
        self.screen.blit(self.line1_image, self.line1_rect)
        self.screen.blit(self.line2_image, self.line2_rect)
        self.screen.blit(self.line3_image, self.line3_rect)

        if not stats.first_start:
            self.prep_high_score(stats)
            self.screen.blit(self.high_score_image, self.high_score_rect)
            self.prep_score(stats)
            self.screen.blit(self.score_image, self.score_rect)
