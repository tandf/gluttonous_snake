class Settings:
    def __init__(self):
        # 屏幕属性
        self.bit = (450, 450)
        self.scoreboard_height = 30
        self.len = 15
        self.bg_color = (0, 0, 0)

        self.x = self.bit[0] / self.len
        self.y = self.bit[1] / self.len

        # 时间参数
        self.interval = 0.1

        # 长度
        self.primary_length = 3
        self.bonus_cut_length = 20

        # 食物量
        self.food_limit = 3
        self.bonus_food = 30

        # 分数
        self.normal_points = 10.0
        self.big_points = 100.0
        self.bonus_points = 200.0

        self.levelup_foods = 10

        # 大食物几率
        self.big_food_chance = 10
