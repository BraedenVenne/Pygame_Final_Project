import pygame
from screens import BaseScreen
from components import TextBox
from sys import exit

class StartScreen(BaseScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sprites = pygame.sprite.Group()
        self.donut = pygame.image.load('images/donut.png')
        self.donut = pygame.transform.rotozoom(self.donut, 0, 0.5)
        # menu buttons 
        self.start_button = pygame.image.load('images/buttons/start_button.png')
        self.quit_button = pygame.image.load('images/buttons/quit_button.png')
        # scale the buttons
        self.start_button = pygame.transform.rotozoom(self.start_button, 0, 0.5)
        self.quit_button = pygame.transform.rotozoom(self.quit_button, 0, 0.5)
        # get the rect of the buttons
        self.start_button_rect = self.start_button.get_rect(center=(200,400))
        self.quit_button_rect = self.quit_button.get_rect(center=(200,500))
        
        # self.button = TextBox(
        #     (200, 100), "Press SPACE",
        #       color=(255, 255, 255),
        #         bgcolor=(0, 0, 0)
        # )
        # self.sprites.add(self.button)

    def draw(self):
        self.window.fill((255, 255, 255))

        # display and center the donut.png on the screen
        self.window.blit(self.donut, self.donut.get_rect(center=(200,200)))

        # display the start and quit buttons on the center bottom of the screen
        self.window.blit(self.start_button, self.start_button_rect)
        self.window.blit(self.quit_button, self.quit_button_rect)

        # self.button.rect.x = 100
        # self.button.rect.y = 400
        self.sprites.draw(self.window)

    def update(self):
        pass

    def manage_event(self, event):
        # print(event)
        # if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
        #     self.next_screen = "game"
        #     self.running = False
        # when start button is clicked move to game screen
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.start_button_rect.collidepoint(event.pos):
                self.next_screen = "game"
                self.running = False
            # when quit button is clicked quit the game
            if self.quit_button_rect.collidepoint(event.pos):
                pygame.quit()
                exit()