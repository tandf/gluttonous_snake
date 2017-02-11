class Stats:
    def __init__(self, settings):
        self.settings = settings

        # 游戏运行状态
        self.first_start = True
        self.pause_game = False
        self.game_active = False
        self.bonus = False
        self.moved = False

        self.snake_length = self.settings.primary_length
        self.foods_eaten = 0
        self.score = 0.
        self.level = 1.0

    def initialize(self):
        self.pause_game = False
        self.bonus = False
        self.moved = False

        self.snake_length = self.settings.primary_length
        self.foods_eaten = 0
        self.score = 0.
        self.level = 1.0

    def update_level(self, settings):
        all_foods = self.foods_eaten
        self.level = 1.0
        while True:
            all_foods -= settings.levelup_foods
            if all_foods >= 0:
                self.level += 0.1
            else:
                break
