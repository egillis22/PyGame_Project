import sys
import pygame


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

    def run_game(self):
        # start main loop
        while True:
            # watch for keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.settings.bg_color)
            # make most recently drawn screen visible
            pygame.display.flip()

    if __name__ == "__main__":
        # make game and run
        ai = AlienInvasion()
        ai.run_game()
