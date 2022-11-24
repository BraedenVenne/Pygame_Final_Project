import pygame
from  screens import StartScreen, GameScreen
from components.globals import SCREEN_WIDTH, SCREEN_HEIGHT

class Game:
    """Main class for the application"""

    def __init__(self):
        # Creates the window
        self.window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    def run(self):
        """Main method, manages interaction between screens"""

        # These are the available screens
        screens = {
            "start": StartScreen,
            "game": GameScreen,
        }

        # Start the loop
        running = True
        current_screen = "start"
        while running:
            # Obtain the screen class
            screen_class = screens.get(current_screen)
            if not screen_class:
                raise RuntimeError(f"Screen {current_screen} not found!")

            # Create a new screen object, "connected" to the window
            screen = screen_class(self.window)

            # Run the screen
            screen.run()

            # When the `run` method stops, we should have a `next_screen` setup
            if screen.next_screen is False:
                running = False
            # Switch to the next screen
            current_screen = screen.next_screen


if __name__ == "__main__":
    jump_man = Game()
    jump_man.run()
