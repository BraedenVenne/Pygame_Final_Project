import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        homer_surf = pygame.image.load('images/jump.png')
        self.homer = pygame.transform.rotozoom(homer_surf, 0, 0.75)
        self.rect = self.homer.get_rect(center=(x, y))
        
    def key_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rect.x -= 10
        if keys[pygame.K_d]:
            self.rect.x += 10
    
    def update(self, window):
        window.blit(self.homer, self.rect)

