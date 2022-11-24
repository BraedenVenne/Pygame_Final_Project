import pygame
from screens.base_screen import BaseScreen
from components import Player, SCREEN_WIDTH, SCREEN_HEIGHT

class GameScreen(BaseScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sky_surf = pygame.image.load('images/sky.png')
        self.player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 100)

    def update(self):
        self.player.movement()
        
    def draw(self):
        self.window.blit(self.sky_surf, (0, 0))
        self.player.update(self.window)


    
        