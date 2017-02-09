class Settings:
    def __init__(self):
        # 屏幕属性
        self.bit = (600, 600)
        self.len = 15
        self.bg_color = (0, 0, 0)
        self.x = self.bit[0] / self.len
        self.y = self.bit[1] / self.len

        # 时间参数
        self.interval = 0.1

        # 初始长度
        self.primary_length = 3

        # 最多食物量
        self.food_limit = 3
