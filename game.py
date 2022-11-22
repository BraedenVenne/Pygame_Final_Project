import pygame
from sys import exit

pygame.init()
# Create sceen and set size
screen = pygame.display.set_mode((800,400))

while True:
    for event in pygame.event.get():
        # close the game
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
    # display screen and add elements to screen
    pygame.display.update()
