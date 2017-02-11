import pygame.font


class ScoreBoard:
    def __init__(self, settings, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.settings = settings

        # 背景
        self.bg_color = (20, 20, 20)

        # 显示得分信息时使用的字体设置
        self.score_color = (150, 150, 150)
        self.level_color = (200, 10, 10)
        self.font = pygame.font.SysFont(None, 40)


    def draw_bg(self):
        self.rect = pygame.Rect(0, 0, self.settings.bit[0], self.settings.scoreboard_height)
        self.screen.fill(self.bg_color, self.rect)

    def show_score(self, stats):
        score_str = "{:,}".format(int(stats.score))
        self.score_image = self.font.render(score_str, True, self.score_color)
        self.score_rect = self.score_image.get_rect()

        self.score_rect.right = self.screen_rect.right - 2
        self.score_rect.bottom = self.settings.scoreboard_height

        self.screen.blit(self.score_image, self.score_rect)

    def show_high_score(self, stats):
        high_score_str = "{:,}".format(int(stats.high_score))
        self.high_score_image = self.font.render("HIGHEST: " + high_score_str, True, self.score_color)
        self.high_score_rect = self.high_score_image.get_rect()

        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.bottom = self.settings.scoreboard_height

        self.screen.blit(self.high_score_image, self.high_score_rect)

    def show_level(self, stats):
        self.level_image = self.font.render('X' + str(round(stats.level, 1)), True, self.level_color)
        self.level_rect = self.level_image.get_rect()

        self.level_rect.left = self.screen_rect.left + 2
        self.level_rect.bottom = self.settings.scoreboard_height

        self.screen.blit(self.level_image, self.level_rect)
