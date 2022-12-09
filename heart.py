import pygame
from pygame.sprite import Sprite
import random


class Heart(Sprite):
    def __init__(self, vv_game):
        # This is the game to initialize the code
        super().__init__()
        self.screen = vv_game.screen
        self.settings = vv_game.settings
        self.screen_rect = vv_game.screen.get_rect()

        # Loading the image of the heart as a rectangle
        self.image = pygame.image.load('images/heart.bmp')
        self.rect = self.image.get_rect()

        # Loading the position of the hearts on the same level as the coins
        self.rect.x = self.rect.width / 5
        self.rect.y = self.rect.height / 0.5

        # Storing the position of the hearts as floats
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Hearts movement
        self.moving_down = True

        # Initializing Hearts
        self.heart_two = None
        self.heart_three = None
        self.heart_four = None
        self.heart_five = None
        self.heart_width = None
        self.ht_list = None
        self.htpp_list = None

    def update(self):
        self.y += self.settings.heart_speed
        self.rect.y = self.y
