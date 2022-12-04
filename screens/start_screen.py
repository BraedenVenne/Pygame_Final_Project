import pygame
from screens import BaseScreen
from sys import exit

class StartScreen(BaseScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sprites = pygame.sprite.Group()
        # menu buttons 
        self.start_button = pygame.image.load('images/buttons/start_button.png')
        self.quit_button = pygame.image.load('images/buttons/quit_button.png')
        # scale the buttons
        self.start_button = pygame.transform.rotozoom(self.start_button, 0, 0.5)
        self.quit_button = pygame.transform.rotozoom(self.quit_button, 0, 0.5)
        # get the rect of the buttons
        self.start_button_rect = self.start_button.get_rect(center=(100,500))
        self.quit_button_rect = self.quit_button.get_rect(center=(300,500))
        # play the bg music
        bg_music = pygame.mixer.Sound('audio/theme.wav')
        bg_music.play(-1)
        self.final_score = None
        

    def draw(self):
        game_name = pygame.image.load('images/game_name.png')
        game_name = pygame.transform.rotozoom(game_name, 0, 0.75)
        game_name_rect = game_name.get_rect(center=(200,100))
        self.start_background = pygame.image.load('images/start_bg.png')
        self.window.blit(self.start_background, (0,0))
        self.window.blit(game_name, game_name_rect)

        # display the start button and quit button
        self.window.blit(self.start_button, self.start_button_rect)
        self.window.blit(self.quit_button, self.quit_button_rect)

    def update(self):
        pass

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