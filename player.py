import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        player_surf = pygame.image.load('images/jump.png')
        self.image = pygame.transform.rotozoom(player_surf, 0, 0.75)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)
        pygame.draw.rect(screen, (255, 255, 255), self.rect, 2)