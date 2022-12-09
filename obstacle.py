import pygame
from pygame.sprite import Sprite


class Obstacle(Sprite):
    def __init__(self, vv_game):
        # Initializing our code
        super().__init__()
        self.screen = vv_game.screen
        self.settings = vv_game.settings
        self.screen_rect = vv_game.screen.get_rect()

        # Loading the obstacles as an image
        self.image = pygame.image.load('images/log.bmp')
        edit_image = (350, 100)
        self.image = pygame.transform.scale(self.image, edit_image)
        self.rect = self.image.get_rect()

        # Loading the positions of each obstacle at the top of the mid-border
        self.rect.x = self.rect.width / 5
        self.rect.y = self.rect.height / 0.46
        self.width1 = self.rect.x, self.rect.y

        # Storing the exact horizontal positions as floats
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Updates the new self.rect.x/y with self.x/y
        self.rect.x = self.x
        self.rect.y = self.y

        # Log's movement
        self.moving_down = True

        # Initializing the logs
        self.obstacle_two = None
        self.obstacle_three = None
        self.ob_list = []
        self.obpp_list = []

    def update(self):
        # This is to move the obstacles down
        self.y += self.settings.logs_speed
        self.rect.y = self.y
