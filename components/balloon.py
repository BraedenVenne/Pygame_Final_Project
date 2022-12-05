import pygame

class Balloon(pygame.sprite.Sprite):
    """
    This class represents the balloon enemy.

    Args:
        pygame (_type_): This is the pygame module.
    """
    def __init__(self, x, y):
        super().__init__()
        # balloon image
        self.image = pygame.image.load('images/balloon.png')
        self.image = pygame.transform.rotozoom(self.image,0,0.45)
        self.image = pygame.transform.flip(self.image, True, False)
        self.rect = self.image.get_rect(center=(x,y))
        self.speed = 1
        self.flip = False

    def movement(self):
        """
        This method handles the balloon's movement.
        """
        # automatically move the balloon to the right or left
        self.rect.x += self.speed

        # cahnge the direction of the balloon when it hits the edge of the screen
        if self.rect.left + self.speed >= 300 or self.rect.right +self.speed <= 100:
            self.speed *= -1
            self.flip = not self.flip
        
    def update(self):  
        """
        This method updates the balloon's movement and animation.
        """    
        self.movement()
    
    def draw(self, window):
        """
        This method draws the balloon to the screen.
        """
        window.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)
        