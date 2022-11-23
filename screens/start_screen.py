import pygame
from screens.base_screen import BaseScreen
from components import TextBox

class StartScreen(BaseScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sprites = pygame.sprite.Group()
        self.donut = pygame.image.load('images/donut.png')
        self.donut = pygame.transform.rotozoom(self.donut, 0, 0.5)
        self.button = TextBox(
            (200, 100), "Press SPACE",
              color=(255, 255, 255),
                bgcolor=(0, 0, 0)
        )
        self.sprites.add(self.button)

    def draw(self):
        self.window.fill((255, 255, 255))

        # display and center the donut.png on the screen
        self.window.blit(self.donut, self.donut.get_rect(center=(200,200)))


        self.button.rect.x = 100
        self.button.rect.y = 400
        self.sprites.draw(self.window)

    def update(self):
        pass

    def manage_event(self, event):
        print(event)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            self.next_screen = "game"
            self.running = False
