class Stats:
    def __init__(self, settings):
        # 游戏运行状态
        self.pause_game = False
        self.game_active = True

        self.snake_length = settings.primary_length
        self.moved = False
