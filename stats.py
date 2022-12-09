class GameStats:
    # This is for tracking game statistics
    def __init(self, vv_game):
        # Initializing Statistics
        self.game_active = False
        self.settings = vv_game.settings
        self.reset_stats_one()
        self.reset_stats_two()

    def reset_stats_one(self):
        self.lives_left_one = self.settings.lives_one

    def reset_stats_two(self):
        self.lives_left_two = self.settings.lives_two
