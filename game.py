import sys
import os
import pygame
from settings import Settings
from avatar import Avatar
from avatar_two import Avatar_two
from obstacle import Obstacle
import random
from coin import Coin
from heart import Heart
from button import Button
from score import Scoreboard
import time


# This is the code to generate the background screen (that is then half-covered by the brown background)
TILE_SIZE = 64
WINDOW_SIZE = 15 * TILE_SIZE
screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
bg = pygame.image.load('images/bg.bmp')
bg_rect = bg.get_rect()
screen_rect = screen.get_rect()


# This is the class for the entire Game
class VroomVroom:
    def __init__(self):
        # This is to initialize the game and game resources
        self.settings = Settings()
        pygame.init()
        pygame.mixer.init()

        # Making the Screen and window title
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Vroom Vroom")
        self.bottom_rect1 = pygame.Rect(0, (self.settings.screen_height / 2),
                                        self.settings.screen_width, (self.settings.screen_height/2))

        # Making the music
        s = 'sounds'
        music = pygame.mixer.music.load(os.path.join(s, 'music.mp3'))
        pygame.mixer.music.play(-1)

        # Initial identifying of the images
        self.avatar = Avatar(self)
        self.avatar_two = Avatar_two(self)
        self.obstacle = Obstacle(self)
        self.obstacles = pygame.sprite.Group()
        self.coin = Coin(self)
        self.coins = pygame.sprite.Group()
        self.heart = Heart(self)
        self.hearts = pygame.sprite.Group()
        self.play_button = Button(self, "Play")
        self.score = Scoreboard(self)
        self.log_buffer_init = 0
        self.log_buffer = 0
        self.log_buffer2_init = 0
        self.log_buffer2 = 0
        self.log_buffer3_init = 0
        self.log_buffer3 = 0
        self.log_buffer4_init = 0
        self.log_buffer4 = 0
        self.log_buffer5_init = 0
        self.log_buffer5 = 0
        self.log_buffer6_init = 0
        self.log_buffer6 = 0

    # This is the Main Loop for the Game (functions are called here in order to be run)
    def run_game(self):
        clock = pygame.time.Clock()
        while True:
            self._check_events()
            self.car_hit()
            self.score.prep_score(self)
            self.score.prep_score_two(self)
            if self.settings.game_active:
                screen.blit(bg, (0, 20))
                self._destroy_objects()
                self.avatar.update()
                self.avatar_two.update()
                self.obstacles.update()
                self.coins.update()
                self.hearts.update()
            self._update_screen()

            # clock.tick(30)

    def _check_events(self):
        # This is the code for checking certain events occur (i.e. keys being pressed)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_events_keydown(event)
            elif event.type == pygame.KEYUP:
                self._check_events_keyup(event)
            elif event.type == pygame.MOUSEBUTTONDOWN and not self.settings.game_active:
                mouse_pos = pygame.mouse.get_pos()
                self.check_play_button(mouse_pos)

    def _check_events_keydown(self, event):
        # This is for checking if the key's have been pressed down and what whill happen if they are pressed
        if event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_ESCAPE:
            sys.exit()
        elif event.key == pygame.K_RIGHT:
            self.avatar.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.avatar.moving_left = True
        elif event.key == pygame.K_UP:
            self.avatar.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.avatar.moving_down = True

        # Code for second car movement
        elif event.key == pygame.K_d:
            self.avatar_two.moving_right = True
        elif event.key == pygame.K_a:
            self.avatar_two.moving_left = True
        elif event.key == pygame.K_w:
            self.avatar_two.moving_up = True
        elif event.key == pygame.K_s:
            self.avatar_two.moving_down = True

    def _check_events_keyup(self, event):
        # This is for checking if the press has been released (If the key isn't being pressed anymore)
        if event.key == pygame.K_RIGHT:
            self.avatar.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.avatar.moving_left = False
        elif event.key == pygame.K_UP:
            self.avatar.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.avatar.moving_down = False

        # Code for second car movement
        elif event.key == pygame.K_d:
            self.avatar_two.moving_right = False
        elif event.key == pygame.K_a:
            self.avatar_two.moving_left = False
        elif event.key == pygame.K_w:
            self.avatar_two.moving_up = False
        elif event.key == pygame.K_s:
            self.avatar_two.moving_down = False

    def check_play_button(self, mouse_pos):
        # Start new game after click
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.settings.game_active:
            self._start_game()

    def _start_game(self):
        # Resetting the game statistics
        self.settings.reset_one()
        self.settings.reset_two()
        self.settings.game_active = True

        self.obstacles.empty()
        self.coins.empty()
        self.hearts.empty()
        self._create_objects()

    # This is the code that calls the function to create the logs
    def _create_objects(self):
        self.log_down()
        self.coin_down()
        self.heart_down()

    # This is the code that deals with removing the objects
    def _destroy_objects(self):
        # This removes the logs once they get off-screen
        for obstacle in self.obstacles:
            if obstacle.rect.top >= self.screen.get_height():
                self.obstacles.empty()
                self.log_down()

        # This removes the coins once they get off-screen
        for coin in self.coins:
            if coin.rect.top >= self.screen.get_height():
                self.coins.empty()
                self.coin_down()

        # This removes the hearts once they get off-screen and limit to one heart every ten seconds
        for heart in self.hearts:
            if heart.rect.top >= self.screen.get_height():
                self.hearts.empty()
                self.heart_down()

    def car_hit(self, ):
        # This is to check collisions between logs and Car 1
        if pygame.sprite.spritecollideany(self.avatar, self.obstacles):
            self.log_buffer = pygame.time.get_ticks()
            if (self.log_buffer - self.log_buffer_init) > 800:
                self.settings.lives_one -= 1
                self.log_buffer_init = pygame.time.get_ticks()

        # This is to check collisions between logs and Car 2
        if pygame.sprite.spritecollideany(self.avatar_two, self.obstacles):
            self.log_buffer2 = pygame.time.get_ticks()
            if (self.log_buffer2 - self.log_buffer2_init) > 800:
                self.settings.lives_two -= 1
                self.log_buffer2_init = pygame.time.get_ticks()

        # This is the code that check collisions between the coins and car 1
        if pygame.sprite.spritecollideany(self.avatar, self.coins):
            self.log_buffer3 = pygame.time.get_ticks()
            if (self.log_buffer3 - self.log_buffer3_init) > 800:
                self.settings.score += 10
                self.log_buffer3_init = pygame.time.get_ticks()

        # This is the code that checks collisions between the coins and car 2
        if pygame.sprite.spritecollideany(self.avatar_two, self.coins):
            self.log_buffer4 = pygame.time.get_ticks()
            if (self.log_buffer4 - self.log_buffer4_init) > 800:
                self.settings.score_two += 10
                self.log_buffer4_init = pygame.time.get_ticks()

        # Checking the collisions between the first car and the hearts
        if pygame.sprite.spritecollideany(self.avatar, self.hearts):
            self.log_buffer5 = pygame.time.get_ticks()
            if (self.log_buffer5 - self.log_buffer5_init) > 600:
                self.settings.lives_one += 1
                if self.settings.lives_one > 2:
                    self.settings.lives_one = 3
                    self.log_buffer5_init = pygame.time.get_ticks()
        if self.settings.lives_one == 0:
            self.game_over()

        # Checking the collisions between the second car and the hearts
        if pygame.sprite.spritecollideany(self.avatar_two, self.hearts):
            self.log_buffer6 = pygame.time.get_ticks()
            if (self.log_buffer6 - self.log_buffer6_init) > 700:
                self.settings.lives_two += 1
                if self.settings.lives_two > 2:
                    self.settings.lives_two = 3
                    self.log_buffer6_init = pygame.time.get_ticks()
        if self.settings.lives_two == 0:
            self.game_over()

    def game_over(self):
        # This is the end screen code
        self.settings.game_active = False
        self.settings.reset_one()
        self.settings.reset_two()
        self.avatar.blitme()
        self.avatar_two.blitme()
        self.avatar.update()
        self.avatar_two.update()

    def log_down(self):
        # A condensed function to create the logs in the correct places
        # This only controls where the logs are created
        log_border = 15
        self.obstacle = Obstacle(self)
        self.obstacle.obstacle_two = Obstacle(self)
        self.obstacle.obstacle_three = Obstacle(self)
        self.obstacle.obstacle_width = self.obstacle.rect.width
        self.obstacle.rect.x = log_border
        self.obstacle.obstacle_two.rect.x = self.obstacle.obstacle_width + (self.obstacle.obstacle_width / 3)
        self.obstacle.obstacle_three.rect.x = (self.obstacle.obstacle_width + self.obstacle.obstacle_width
                                               + (self.obstacle.obstacle_width / 2))

        # This controls the randomized selection of which logs appear on the screen
        self.obstacle.ob_list = [self.obstacle, self.obstacle.obstacle_two, self.obstacle.obstacle_three]
        self.obstacle.obpp_list = []
        self.obstacle.obpp_list.append(self.obstacle.ob_list.pop(random.randint(0, len(self.obstacle.ob_list)-1)))
        self.obstacle.obpp_list.append(self.obstacle.ob_list.pop(random.randint(0, len(self.obstacle.ob_list)-1)))
        self.obstacles.add(self.obstacle.obpp_list[0])
        self.obstacles.add(self.obstacle.obpp_list[1])
        self.obstacle.ob_list.append(self.obstacle.obpp_list.pop(0))
        self.obstacle.ob_list.append(self.obstacle.obpp_list.pop(0))

    def coin_down(self):
        # This controls the coins placement and locations
        coin_border = 7
        self.coin = Coin(self)
        self.coin.coin_two = Coin(self)
        self.coin.coin_three = Coin(self)
        self.coin.coin_four = Coin(self)
        self.coin.coin_five = Coin(self)
        self.coin.coin_six = Coin(self)
        self.coin.coin_width = self.coin.rect.width
        self.coin.rect.x = coin_border
        self.coin.coin_two.rect.x = self.coin.coin_width * 4
        self.coin.coin_three.rect.x = self.coin.coin_width * 8
        self.coin.coin_four.rect.x = self.coin.coin_width * 10
        self.coin.coin_five.rect.x = self.coin.coin_width * 13
        self.coin.coin_six.rect.x = self.coin.coin_width * 16

        # This will control the randomized selection of the coins that will appear on screen
        self.coin.cnpp_list = []
        self.coin.cn_list = [self.coin, self.coin.coin_two, self.coin.coin_three, self.coin.coin_four,
                             self.coin.coin_five, self.coin.coin_six]
        self.coin.cnpp_list.append(self.coin.cn_list.pop(random.randint(0, len(self.coin.cn_list) - 1)))
        self.coin.cnpp_list.append(self.coin.cn_list.pop(random.randint(0, len(self.coin.cn_list) - 1)))
        self.coin.cnpp_list.append(self.coin.cn_list.pop(random.randint(0, len(self.coin.cn_list) - 1)))
        self.coins.add(self.coin.cnpp_list[0])
        self.coins.add(self.coin.cnpp_list[1])
        self.coins.add(self.coin.cnpp_list[2])
        self.coin.cn_list.append(self.coin.cnpp_list.pop(0))
        self.coin.cn_list.append(self.coin.cnpp_list.pop(0))
        self.coin.cn_list.append(self.coin.cnpp_list.pop(0))

    def heart_down(self):
        heart_border = 10
        self.heart = Heart(self)
        self.heart.heart_two = Heart(self)
        self.heart.heart_three = Heart(self)
        self.heart.heart_four = Heart(self)
        self.heart.heart_five = Heart(self)
        self.heart.heart_width = self.heart.rect.width
        self.heart.rect.x = heart_border * 11
        self.heart.heart_two.rect.x = self.heart.heart_width * 12
        self.heart.heart_three.rect.x = self.heart.heart_width * 4
        self.heart.heart_four.rect.x = self.heart.heart_width * 6
        self.heart.heart_five.rect.x = self.heart.heart_width * 8

        # This is to ensure that only one random heart will be displayed on-screen
        self.heart.ht_list = [self.heart, self.heart.heart_two, self.heart.heart_three, self.heart.heart_four,
                              self.heart.heart_five]
        self.heart.htpp_list = []
        self.heart.htpp_list.append(self.heart.ht_list.pop(random.randint(0, len(self.heart.ht_list) - 1)))
        self.hearts.add(self.heart.htpp_list[0])
        self.heart.ht_list.append(self.heart.htpp_list.pop(0))

    def _update_screen(self):
        self.screen.fill((0, 0, 1))

        # screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
        bg = pygame.image.load('images/bg.bmp')
        bg_rect = bg.get_rect()
        screen_rect = self.screen.get_rect()
        self.screen.blit(bg, bg_rect)

        # This code is for the color of the screen
        pygame.draw.rect(self.screen, self.settings.bottom_color, self.bottom_rect1)

        # This is the code for displaying the objects on the screen
        if not self.settings.game_active:
            self.play_button.draw_button()
        else:
            self.avatar.blitme()
            self.avatar_two.blitme()
            self.obstacles.draw(self.screen)
            self.coins.draw(self.screen)
            self.hearts.draw(self.screen)
            self.score.show_score()
            self.score.prep_score(self)
            self.score.prep_score_two(self)
            self.car_hit()

        # This is to refresh the screen to the most recent version
        pygame.display.flip()

    def play_button(self):
        # Draw Button
        pass


if __name__ == '__main__':
    # Make a game instance to run the game
    vv = VroomVroom()
    vv.run_game()
