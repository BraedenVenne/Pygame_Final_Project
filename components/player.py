import pygame
from .globals import MAX_WIDTH, MAX_HEIGHT


class Player(pygame.sprite.Sprite):
    """
    This is the Player class. It handles
    the player's movement and animation. It also
    handles the player's jumping and gravity.
    """
    def __init__(self, x, y):
        super().__init__()
        # walking animation images
        self.homer_walk = []
        for i in range(1,8):
            img = pygame.image.load(f'images/homer/homer_walk{i}.png').convert_alpha()
            self.homer_walk.append(img)
        self.homer_index = 0
        self.homer = self.homer_walk[self.homer_index]
        self.rect = self.homer.get_rect(center=(x, y))
        self.flip = False
        self.vel_y = 0
        self.jump = False
        self.gravity = 1

    def movement(self):
        """
        This method handles the player's movement.
        """
        # distance variables
        x = 0
        y = 0

        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            x = -7
            self.flip = True
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            x = 7
            self.flip = False
        
        if self.jump == False and keys[pygame.K_SPACE]:
            self.jump = True
            
        if self.jump == True:
            y -= self.vel_y*2.5
            self.vel_y -= self.gravity
            self.homer = pygame.image.load('images/homer/homer_jump.png').convert_alpha()
            if self.vel_y < -20:
                self.jump = False
                self.vel_y = 20
        else:
            self.homer = pygame.image.load('images/homer/homer_stand.png').convert_alpha()
            if keys[pygame.K_d] or keys[pygame.K_a] or keys[pygame.K_RIGHT] or keys[pygame.K_LEFT]:
                self.homer_index += 0.2
                if self.homer_index >= len(self.homer_walk):
                    self.homer_index = 0
                self.homer = self.homer_walk[int(self.homer_index)]
        
        # set boundary on the floor
        if self.rect.bottom + y >= MAX_HEIGHT:
            y = 0
            self.jump = False
            self.vel_y = 10

        # set movement
        self.rect.x += x
        self.rect.y += y

    def boundary(self):
        """
        This method handles the player's boundary.
        """
    # set boundaries so player cant walk off screen
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= MAX_WIDTH:
            self.rect.right = MAX_WIDTH
        
    def update(self, window):
        """
        This method updates the player's movement and animation.
        """
        self.boundary()
        window.blit(pygame.transform.flip(self.homer, self.flip, False), self.rect)