import pygame

from .globals import MAX_HEIGHT

class Projectile(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('images/fireball.png')
        self.image = pygame.transform.rotozoom(self.image,0,0.5)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
    # def shoot_projectile(self):
    #     y = 5
    #     self.rect.y += y

    def remove(self):
        if self.rect.y >= 100:
            self.kill()



    def update(self, window):
        self.rect.y += 5
        window.blit(self.image, self.rect)
        self.remove()
