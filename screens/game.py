import pygame
import random
from screens import BaseScreen
from components import Player, MAX_WIDTH, MAX_HEIGHT, Balloon


class GameScreen(BaseScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sky_surf = pygame.image.load('images/sky.png')
        self.player = Player(MAX_WIDTH / 2, MAX_HEIGHT - 50)
        self.balloon = Balloon(MAX_WIDTH / 2, 130)

    def update(self):
        self.player.movement()
        self.balloon.movement()
        
    def draw(self):
        self.window.blit(self.sky_surf, (0, 0))
        self.player.update(self.window)
        self.balloon.update(self.window)
    
    def manage_event(self, event):
        if event.type == pygame.QUIT:
            self.next_screen = False
            self.running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            self.next_screen = False
            self.running = False


        