import pygame
from sys import exit
from player import Player



SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
homer = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 150)

def main():
    pygame.init()
    # Create sceen and set size
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # Set the name of the window
    pygame.display.set_caption('Jump Man')

    clock = pygame.time.Clock()

    # load image of sky
    sky_surf = pygame.image.load('images/sky.png')

    running = True
    while running:
        for event in pygame.event.get():
            
            # close the game
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        screen.blit(sky_surf, (0,0))

        # Draw player
        homer.draw(screen)

        # update display window
        pygame.display.update()


        # run game at a maximum of 60fps
        clock.tick(60)

if __name__ == '__main__':
    main()