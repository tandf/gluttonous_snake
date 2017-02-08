import pygame


class Button:
    def __init__(self, screen, msg, pos):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # 按钮属性
        self.button_color = (0, 255, 0)
        self.text_color = (0, 0, 0)
        self.width, self.height = 100, 30
        self.font = pygame.font.SysFont(None, 28)

        # 在指定位置创建矩形
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.topleft = pos

        # 按钮信息
        self.msg = msg
        self.prep_msg()

    def prep_msg(self, msg):
        """将msg渲染为图像，并使其在按钮上居中"""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """绘制一个用颜色填充的按钮，再绘制文本"""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
