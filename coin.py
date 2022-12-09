import pygame
from pygame.sprite import Sprite
import random


class Coin(Sprite):
    def __init__(self, vv_game):
        # Initializing the code
        super().__init__()
        self.screen = vv_game.screen
        self.settings = vv_game.settings
        self.screen_rect = vv_game.screen.get_rect()

        # Loading the coins as an image
        self.image = pygame.image.load('images/coin.bmp')
        self.rect = self.image.get_rect()

        # Loading the position of the coins below the logs
        self.rect.x = self.rect.width / 5
        self.rect.y = self.rect.height / 0.5

        # Storing the horizontal position of the coins as floats
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Coin's Movement
        self.moving_down = True

        # Initializing the Hearts
        self.coin_two = None
        self.coin_three = None
        self.coin_four = None
        self.coin_five = None
        self.coin_six = None
        self.coin_width = None
        self.cn_list = []
        self.cnpp_list = []

    def update(self):
        # This is to make the coins move down
        self.y += self.settings.coin_speed
        self.rect.y = self.y

    def update_(self):
        # This is to incorporate a different speed for the coins
        self.y += self.settings.coin_speed_
        self.rect.y = self.y

    def _update(self):
        # This is to incorporate another speed for the coins
        self.y += self.settings._coin_speed
        self.rect.y = self.y
