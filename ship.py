import pygame


class Ship:
    def __init__(self, ai_game):
        # initialize ship and start position
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.moving_right = False
        self.moving_left = False
        # load ship image and get its rect
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        # start each ship at bottom center
        self.rect.midbottom = self.screen_rect.midbottom

    def update(self):
        if self.moving_right:
            self.rect.x += 1
        if self.moving_left:
            self.rect.x -= 1

    def blitme(self):
        # draw ship at current location
        self.screen.blit(self.image, self.rect)
