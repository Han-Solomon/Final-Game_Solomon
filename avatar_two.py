import pygame
from pygame.sprite import Sprite


class Avatar_two(Sprite):
    def __init__(self, vv_game):
        # This will initialize the code or the second player character
        super().__init__()
        self.halfup = None
        self.screen = vv_game.screen
        self.settings = vv_game.settings
        self.screen_rect = vv_game.screen.get_rect()

        # Loading Car number 2
        self.image = pygame.image.load('images/car2.bmp')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # This initial movement of the car (stationary)
        self.moving_up = False
        self.moving_down = False
        self.moving_right = False
        self.moving_left = False

    def update(self):
        # This defines the movement the second car

        # Movement for the car going right
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.speed

        # Movement for the car going downwards
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.speed

        # Movement in the left direction
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.speed

        # Movement going up but not past the halfway mark on the screen
        self.halfup = float(self.rect.top - (self.rect.centery/1.141))
        if self.moving_up and self.halfup > 0:
            self.y -= self.settings.speed

        # This will constantly update the position of the car
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        # This will put the physical image onto the screen
        self.screen.blit(self.image, self.rect)
