import pygame

class Projectile(pygame.sprite.Sprite):
    """
    This class represents the projectiles.

    Args:
        pygame (_type_): This is the pygame module.
    """
    def __init__(self, x: int, y: int, projectile_type: str):
        super().__init__()
        # projectile type
        self.projectile_type = projectile_type
        if self.projectile_type == 'fireball':
            self.image = pygame.image.load('images/fireball.png')
            self.image = pygame.transform.rotozoom(self.image,0,0.5)
        else:
            self.image = pygame.image.load('images/donut.png')
            self.image = pygame.transform.rotozoom(self.image,0,0.1)
        self.rect = self.image.get_rect(center=(x,y))
 
    def update(self, window):
        """
        This method updates the projectile's position.

        Args:
            window (_type_): This is the window object.
        """
        # move the projectile
        self.rect.y += 5
        window.blit(self.image, self.rect)
        
