import sys
import pygame


class AlienInvasion:
    def __init__(self):
        # initialize game
        pygame.init()
        # display window
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")
        # background
        self.bg_color = (230, 230, 230)

    def run_game(self):
        # start main loop
        while True:
            # watch for keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.bg_color)
            # make most recently drawn screen visible
            pygame.display.flip()

    if __name__ == "__main__":
        # make game and run
        ai = AlienInvasion()
        ai.run_game()
