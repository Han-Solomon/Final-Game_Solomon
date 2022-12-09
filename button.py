import pygame.font


class Button:
    def __init__(self, vv_game, msg):
        # Initializing the code
        self.screen = vv_game.screen
        self.screen_rect = self.screen.get_rect()

        # Settings the dimensions of the button and its properties
        self.width, self.height = 200, 50
        self.button_color = (255, 0, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Centering the Button
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # Only making the button once
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        # Turning the message into an actual image
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        # Making a blank button then a message
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
