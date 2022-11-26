import pygame
from screens import BaseScreen

class GameOver(BaseScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        game_over_sound = pygame.mixer.Sound('audio/game_over.wav')
        game_over_sound.play()
        self.game_over_background = pygame.image.load('images/game_over_bg.png')
        self.start_button = pygame.image.load('images/buttons/start_button.png')
        self.quit_button = pygame.image.load('images/buttons/quit_button.png')
        # scale the buttons
        self.start_button = pygame.transform.rotozoom(self.start_button, 0, 0.5)
        self.quit_button = pygame.transform.rotozoom(self.quit_button, 0, 0.5)
        # set the buttons side by side near the bottom of the screen
        self.start_button_rect = self.start_button.get_rect(center=(100,450))
        self.quit_button_rect = self.quit_button.get_rect(center=(300,450))
        # game over text
        self.game_over_text = pygame.image.load('images/game_over.png')
        self.game_over_text = pygame.transform.rotozoom(self.game_over_text, 0, 0.75)
        # put the gama over text in the middle of the screen
        self.game_over_text_rect = self.game_over_text.get_rect(center=(200,250))

    def update(self):
        pass

    def draw(self):
        self.window.blit(self.game_over_background, (0,0))
        # display the start button and quit button
        self.window.blit(self.start_button, self.start_button_rect)
        self.window.blit(self.quit_button, self.quit_button_rect)
        # display the game over text
        self.window.blit(self.game_over_text, self.game_over_text_rect)
            
    def manage_event(self, event):
        # when start button is clicked move to game screen
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.start_button_rect.collidepoint(event.pos):
                self.next_screen = "game"
                self.running = False
            # when quit button is clicked quit the game
            if self.quit_button_rect.collidepoint(event.pos):
                pygame.quit()
                exit()