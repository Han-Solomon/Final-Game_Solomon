class Settings:

    def __init__(self):
        self.lives_left_one = None
        self.lives_left_two = None
        self.game_active = False
        # Making the background colors
        self.bottom_color = (101, 67, 33)
        self.bg_color = (52, 225, 235)

        # This controls the car's speed and log's speed
        self.speed = 8
        self.lives_one = 3
        self.lives_two = 3
        self.logs_speed = 4
        self.allowed = 4

        # This controls the coin/heart speed
        self.coin_speed = 4
        self.heart_speed = 4

        self.reset_one()
        self.reset_two()

    # Initializing stats
    def reset_one(self):
        self.lives_left_one = self.lives_one
        self.score = 0
        self.lives_one = 3

    def reset_two(self):
        self.lives_left_two = self.lives_two
        self.score_two = 0
        self.lives_two = 3

