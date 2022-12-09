import pygame
from pygame.sprite import Sprite


class Avatar(Sprite):
    def __init__(self, vv_game):
        # Initializing the code for the Avatar
        super().__init__()
        self.halfup = None
        self.screen = vv_game.screen
        self.settings = vv_game.settings
        self.screen_rect = vv_game.screen.get_rect()

        # Loading the Car
        self.image = pygame.image.load('images/car.bmp')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Moving the Car
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        # To define the movement of the car once it is bound to key events
        # If the car is moving right but within the border of the screen
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.speed

        # Doesn't move past the bottom border of the screen
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.speed

        # Doesn't Move past the left border on the screen
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.speed

        # Doesn't Move above the halfway mark on the screen
        self.halfup = float(self.rect.top - (self.rect.centery/1.141))
        if self.moving_up and self.halfup > 0:
            self.y -= self.settings.speed

        # Updates the self.rect.__ with new self.x or self.y
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        # This will put the rectangular surface (the car) onto the screen
        self.screen.blit(self.image, self.rect)
