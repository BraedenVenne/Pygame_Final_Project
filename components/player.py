import pygame
from components.globals import SCREEN_WIDTH, SCREEN_HEIGHT

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        homer_surf = pygame.image.load('images/jump.png').convert_alpha()
        self.homer = pygame.transform.rotozoom(homer_surf, 0, 0.75)
        self.rect = self.homer.get_rect(center=(x, y))
        self.flip = False
        
    def movement(self):
        """
        Handles the player's movement
        """
        # distance variables
        x = 0
        y = 0

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            x = -10
            self.flip = True
        if keys[pygame.K_d]:
            x = 10
            self.flip = False

        # Screen boundaries
        if self.rect.x > SCREEN_WIDTH:
            self.rect.x = 0
        elif self.rect.x < 0:
            self.rect.x = SCREEN_WIDTH
        
        # screen position
        self.rect.x += x
        self.rect.y += y


    def update(self, window):
        window.blit(pygame.transform.flip(self.homer, self.flip, False), self.rect)

