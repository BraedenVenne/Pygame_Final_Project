import pygame

from .globals import MAX_HEIGHT

class Projectile(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, projectile_type: str):
        super().__init__()
        self.projectile_type = projectile_type
        if self.projectile_type == 'fireball':
            self.image = pygame.image.load('images/fireball.png')
            self.image = pygame.transform.rotozoom(self.image,0,0.5)
        else:
            self.image = pygame.image.load('images/donut.png')
            self.image = pygame.transform.rotozoom(self.image,0,0.1)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
 
    def update(self, window):
        self.rect.y += 5
        window.blit(self.image, self.rect)
        
