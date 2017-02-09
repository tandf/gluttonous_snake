class Stats:
    def __init__(self, settings):
        # 游戏运行状态
        self.pause_game = False
        self.game_active = True
        self.bonus = False
        self.moved = False

        self.snake_length = settings.primary_length
        self.foods_eaten = 0
        self.score = 0.0
