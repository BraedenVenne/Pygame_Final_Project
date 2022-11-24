import pygame
from components.globals import SCREEN_WIDTH, SCREEN_HEIGHT

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        # walking images
        homer_walk_1 = pygame.image.load('images/homer_walk1.png').convert_alpha()
        homer_walk_2 = pygame.image.load('images/homer_walk2.png').convert_alpha()
        homer_walk_3 = pygame.image.load('images/homer_walk3.png').convert_alpha()
        homer_walk_4 = pygame.image.load('images/homer_walk4.png').convert_alpha()
        homer_walk_5 = pygame.image.load('images/homer_walk5.png').convert_alpha()
        homer_walk_6 = pygame.image.load('images/homer_walk6.png').convert_alpha()
        homer_walk_7 = pygame.image.load('images/homer_walk7.png').convert_alpha()
        self.homer_walk = [homer_walk_1, homer_walk_2, homer_walk_3, homer_walk_4, homer_walk_5, homer_walk_6, homer_walk_7]
        self.homer_index = 0
        self.homer = self.homer_walk[self.homer_index]
        self.rect = self.homer.get_rect(center=(x, y))
        self.flip = False
        self.vel_y = 0
        self.jump = False
        self.gravity = 1

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
        
        if self.jump == False and keys[pygame.K_SPACE]:
            self.jump = True
            
        if self.jump == True:
            y -= self.vel_y*4
            self.vel_y -= self.gravity
            self.homer = pygame.image.load('images/homer_jump2.png').convert_alpha()
            if self.vel_y < -20:
                self.jump = False
                self.vel_y = 20
        else:
            self.homer = pygame.image.load('images/homer_stand.png').convert_alpha()
            if keys[pygame.K_d] or keys[pygame.K_a]:
                self.homer_index += 0.2
                if self.homer_index >= len(self.homer_walk):
                    self.homer_index = 0
                self.homer = self.homer_walk[int(self.homer_index)]
        
        # set boundary on the floor
        if self.rect.bottom + y >= SCREEN_HEIGHT:
            y = 0
            self.jump = False
            self.vel_y = 10

        # set movement
        self.rect.x += x
        self.rect.y += y

        # Screen boundaries
        if self.rect.x > SCREEN_WIDTH:
            self.rect.x = 0
        elif self.rect.x < 0:
            self.rect.x = SCREEN_WIDTH
        
       

        

    def update(self, window):
        window.blit(pygame.transform.flip(self.homer, self.flip, False), self.rect)

