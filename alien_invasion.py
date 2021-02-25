import sys
import pygame
from settings import Settings
from ship import Ship


class AlienInvasion:
    def __init__(self):
        # initialize game
        pygame.init()
        self.settings = Settings()
        # display window
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Alien Invasion")
        # background
        self.ship = Ship(self)

    def run_game(self):
        # start main loop
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        # watch for keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        # make most recently drawn screen visible
        pygame.display.flip()


if __name__ == "__main__":
    # make game and run
    ai = AlienInvasion()
    ai.run_game()
