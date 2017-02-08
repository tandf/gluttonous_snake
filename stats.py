class Stats:
    def __init__(self, settings):
        # 游戏状态
        self.pause_game = False
        self.snake_length = settings.primary_length
        self.moved = False
