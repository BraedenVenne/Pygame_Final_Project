import pygame
import random
from screens import BaseScreen
from components import Player, MAX_WIDTH, MAX_HEIGHT, Balloon, Projectile

class GameScreen(BaseScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sky_surf = pygame.image.load('images/sky.png')
        self.player = Player(MAX_WIDTH / 2, MAX_HEIGHT - 50)
        self.balloon = Balloon(MAX_WIDTH / 2, 130)
        self.projectiles = []
        self.player_health = 20

    def shoot(self):
        x_pos = self.balloon.rect.center[0]
        chance = random.randint(1, 50)
        if chance == 1:
            projectile = Projectile(x_pos, 200)
            projectile.update(self.window)
            self.projectiles.append(projectile)

    def update(self):
        self.player.movement()
        self.balloon.movement()
        self.shoot()
        self.remove()

    def draw(self):
        self.window.blit(self.sky_surf, (0, 0))
        self.player.update(self.window)
        self.balloon.update(self.window)
        for p in self.projectiles:
            p.update(self.window)

    def remove(self):
        for p in self.projectiles:
            if p.rect.y > 600:
                self.projectiles.remove(p)
            if p.rect.colliderect(self.player.rect):
                self.projectiles.remove(p)
                print('hit')
                self.player_health -= 1
    
    def manage_event(self, event):
        if event.type == pygame.QUIT:
            self.next_screen = False
            self.running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            self.next_screen = False
            self.running = False