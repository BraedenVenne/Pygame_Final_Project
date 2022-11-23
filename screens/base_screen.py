import pygame

class BaseScreen:
    """Base class for all game screens"""

    def __init__(self, window):
        # window surface
        self.window = window
        # By default, there is no next screen (= game quits)
        self.next_screen = False

    def run(self):

        clock = pygame.time.Clock()
        self.running = True
        while self.running:
            # tick the clock
            clock.tick(60)
            # update the screen
            self.update()
            # draw the objects on the screen
            self.draw()
            # update the display
            pygame.display.update()

            # Event loop
            for event in pygame.event.get():
                # Quit the game
                if event.type == pygame.QUIT:
                    self.running = False
                    self.next_screen = False
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    self.running = False
                    self.next_screen = False
                    
    @property
    def rect(self):
        """Useful property to check for boundaries and dimensions"""

        return self.window.get_rect()

    def draw(self):
        """Child classes should override this method"""

        print("You should override the DRAW method in your class...")

    def update(self):
        """Child classes should override this method"""

        print("You should override the UPDATE method in your class...")

    def manage_event(self, event):
        """Child classes should override this method"""

        print("You should override the MANAGE_EVENT method in your class...")
