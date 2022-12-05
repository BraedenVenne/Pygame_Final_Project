import pygame
from  screens import StartScreen, GameScreen, GameOver
from components import MAX_WIDTH, MAX_HEIGHT

class Game:
    """Main class for the application"""
    def __init__(self):
        # Creates the window
        self.window = pygame.display.set_mode((MAX_WIDTH, MAX_HEIGHT))
    def run(self):
        pygame.init()
        """Main method, manages interaction between screens"""

        # These are the available screens
        screens = {
            "start": StartScreen,
            "game": GameScreen,
            "game_over": GameOver,
        }

        # Start the loop
        running = True
        final_score = 0
        current_screen = "start"
        while running:
            # Obtain the screen class
            screen_class = screens.get(current_screen)
            if not screen_class:
                raise RuntimeError(f"Screen {current_screen} not found!")

            # pass final score to game over screen
            if current_screen == "game_over":
                screen = screen_class(self.window, final_score)
            else:
                screen = screen_class(self.window)

            # Run the screen
            screen.run()    

            # When the `run` method stops, we should have a `next_screen` setup
            if screen.next_screen is False:
                running = False
            # Switch to the next screen
            current_screen = screen.next_screen

            if screen.final_score != 0:
                final_score = screen.final_score

if __name__ == "__main__":
    donut_jump = Game()
    donut_jump.run()