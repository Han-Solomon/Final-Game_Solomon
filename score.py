import pygame.font


class Scoreboard:
    def __init__(self, vv_game):
        self.score_image_two = None
        self.score_image = None
        self.score_rect_two = None
        self.score_rect = None
        self.health_rect = None
        self.health_rect_two = None
        self.health_image = None
        self.health_image_two = None
        self.screen = vv_game.screen
        self.screen_rect = vv_game.screen.get_rect()
        self.settings = vv_game.settings

        self.text_color = (255, 0, 0)
        self.bg_color = (0, 0, 0)
        self.text_color_two = (255, 255, 0)
        self.font = pygame.font.SysFont(None, 48)
        self.prep_score(vv_game)
        self.prep_score_two(vv_game)

    def prep_score(self, vv_game):
        # Displays Red Score Value
        score_str = str(vv_game.settings.score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.bg_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

        # Red score Text
        self.rscore_color = (255, 0, 0)
        self.rscore_image = self.font.render("Score:", True, self.rscore_color, self.bg_color)
        self.rscore_rect = self.rscore_image.get_rect()
        self.rscore_rect.right = self.screen_rect.right - 80
        self.rscore_rect.top = 20

        # Displays' Red health value
        health_str = str(vv_game.settings.lives_one)
        self.health_image = self.font.render(health_str, True, self.text_color, self.bg_color)
        self.health_rect = self.health_image.get_rect()
        self.health_rect.right = self.screen_rect.right - 20
        # self.health_rect.topright = self.screen_rect.topright - 20
        self.health_rect.top = 100

        # Red health Text
        self.rhealth_color = (255, 0, 0)
        self.rhealth_image = self.font.render("Health:", True, self.rhealth_color, self.bg_color)
        self.rhealth_rect = self.rhealth_image.get_rect()
        self.rhealth_rect.right = self.screen_rect.right - 80
        self.rhealth_rect.top = 100

    def prep_score_two(self, vv_game):
        # Yellow Score value
        score_str_two = str(vv_game.settings.score_two)
        self.score_image_two = self.font.render(score_str_two, True, self.text_color_two, self.bg_color)
        self.score_rect_two = self.score_image_two.get_rect()
        self.score_rect_two.left = self.screen_rect.left + 280
        self.score_rect_two.top = 20

        # Yellow score text
        # Red score Text
        self.yscore_color = (255, 255, 0)
        self.yscore_image = self.font.render("Score:", True, self.yscore_color, self.bg_color)
        self.yscore_rect = self.yscore_image.get_rect()
        self.yscore_rect.left = self.screen_rect.left + 20
        self.yscore_rect.top = 20

        # Yellow Health Value
        health_str_two = str(vv_game.settings.lives_two)
        self.health_image_two = self.font.render(health_str_two, True, self.text_color_two, self.bg_color)
        self.health_rect_two = self.health_image_two.get_rect()
        self.health_rect_two.left = self.screen_rect.left + 280
        self.health_rect_two.top = 100

        # Yellow Health Text
        self.yhealth_color = (255, 255, 0)
        self.yhealth_image = self.font.render("Health:", True, self.yhealth_color, self.bg_color)
        self.yhealth_rect = self.yhealth_image.get_rect()
        self.yhealth_rect.left = self.screen_rect.left + 20
        self.yhealth_rect.top = 100

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.rscore_image, self.rscore_rect)
        self.screen.blit(self.score_image_two, self.score_rect_two)
        self.screen.blit(self.yscore_image, self.yscore_rect)
        self.screen.blit(self.health_image, self.health_rect)
        self.screen.blit(self.rhealth_image, self.rhealth_rect)
        self.screen.blit(self.health_image_two, self.health_rect_two)
        self.screen.blit(self.yhealth_image, self.yhealth_rect)
