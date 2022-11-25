import pygame
from components import MAX_WIDTH
from .projectiles import Projectile

class Balloon(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('images/balloon.png')
        self.image = pygame.transform.rotozoom(self.image,0,0.45)
        self.image = pygame.transform.flip(self.image, True, False)
        # create a rectangle and set the position to the top, center of screen
        self.rect = self.image.get_rect(center=(x,y))
        self.x = 1
        self.flip = False



    # def shoot_projectile(self):
    #     self.projectile.rect.center = self.rect.center


    def movement(self):
        # make the balloon automatically move to the right or left
        self.rect.x += self.x

        # if the balloon reaches the edge of the screen, change direction and flip the image
        if self.rect.left >= 300 or self.rect.right <= 100:
            self.x *= -1
            self.flip = not self.flip
        
    def update(self, window):
        window.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)
        # self.projectiles.update(window)
        