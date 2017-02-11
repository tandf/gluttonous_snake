import pygame.font


class ScoreBoard:
    """显示得分信息的类"""

    def __init__(self, settings, screen, stats):
        """初始化显示得分涉及的属性"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.settings = settings

        # 背景
        self.bg_color = (20, 20, 20)

        # 显示得分信息时使用的字体设置
        self.text_color = (150, 150, 150)
        self.font = pygame.font.SysFont(None, 40)


    def draw_bg(self):
        self.rect = pygame.Rect(0, 0, self.settings.bit[0], self.settings.scoreboard_height)
        self.screen.fill(self.bg_color, self.rect)

    def show_score(self, stats):
        """在屏幕上显示得分"""
        score_str = "{:,}".format(int(stats.score))
        self.score_image = self.font.render(score_str, True, self.text_color)

        # 将得分放在屏幕右上角
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 2
        self.score_rect.bottom = self.settings.scoreboard_height

        self.screen.blit(self.score_image, self.score_rect)
