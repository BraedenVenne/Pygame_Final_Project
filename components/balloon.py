import pygame
from components import MAX_WIDTH

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

    def movement(self):
        # make the balloon automatically move to the right or left
        self.rect.x += self.x

        # if the balloon reaches the edge of the screen, change direction and flip the image
        
        if self.rect.right >= MAX_WIDTH or self.rect.left <= 0:
            self.x *= -1
            self.flip = not self.flip
        
    
    def boundary(self):
        if self.rect.right + self.x >= MAX_WIDTH:
            self.x = MAX_WIDTH - self.rect.right
        elif self.rect.left + self.x <= 0:
            self.x = -self.rect.left
    
    def update(self, window):
        self.boundary()
        window.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)