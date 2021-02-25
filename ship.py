import pygame


class Ship:
    def __init__(self, ai_game):
        # initialize ship and start position
        self.screen = ai_game.screen
        self.screen_rect = ai_game.get_rect()

        # load ship image
        self.image = pygame.image.load("images/ship.bmp")
        # start each ship at bottom center
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        # draw ship at current location
        self.screen.blit(self.image, self.rect)
