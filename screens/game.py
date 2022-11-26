import pygame
import random
from screens import BaseScreen
from components import Player, MAX_WIDTH, MAX_HEIGHT, Balloon, Projectile

class GameScreen(BaseScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sky_surf = pygame.image.load('images/background.png')
        self.player = Player(MAX_WIDTH / 2, MAX_HEIGHT - 50)
        self.balloon = Balloon(MAX_WIDTH / 2, 130)
        self.projectiles = []
        self.player_health = 10
        self.test_font = pygame.font.Font('font/Pixeltype.ttf', 50)
        self.start_time = 0
        self.health_text = self.test_font.render(f'Health: {self.player_health}', True, (0, 0, 0))
        self.score = 0
        self.start_time = pygame.time.get_ticks() // 1000
        self.speed_increase = 10
        self.balloon_speed = 1

    def get_score(self):
        self.score = (pygame.time.get_ticks() // 1000) - self.start_time
        # if score is greater than speed increase and balloon speed is >
        if self.score > self.speed_increase and self.score > 0 and self.balloon.speed > 0:
            self.balloon.speed -= 1
            self.balloon_speed += 1
            self.balloon.speed = self.balloon_speed
            self.speed_increase *= 2

    def shoot(self):
        x_pos = self.balloon.rect.center[0]
        chance = random.randint(1, 100)
        if chance % 15 == 0:
            projectile = Projectile(x_pos, 200, 'fireball')
            projectile.update(self.window)
            self.projectiles.append(projectile)
        elif chance % 100 == 0:
            projectile = Projectile(x_pos, 200, 'donut')
            projectile.update(self.window)
            self.projectiles.append(projectile)

    def draw(self):
        self.window.blit(self.sky_surf, (0, 0))
        self.player.update(self.window)
        self.balloon.draw(self.window)
        for p in self.projectiles:
            p.update(self.window)
        # draw the health to the top right of the screen
        self.window.blit(self.health_text, (MAX_WIDTH - 150, 10))
        # draw the score to the top left of the screen
        self.window.blit(self.test_font.render(f'Score: {self.score}', True, (0, 0, 0)), (10, 10))

    def remove_projectile(self):
        for p in self.projectiles:
            if p.rect.y > 600:
                self.projectiles.remove(p)
            if p.rect.colliderect(self.player.rect) and p.projectile_type == 'fireball':
                chance = random.randint(1, 2)
                if chance == 1:
                    pygame.mixer.Sound('audio/homer_doh.wav').play()
                self.projectiles.remove(p)
                self.player_health -= 1
                self.health_text = self.test_font.render(f'Health: {self.player_health}', True, (0, 0, 0))
                if self.player_health == 0:                 
                    self.start_time += pygame.time.get_ticks() // 1000
                    self.score = 0
                    # change the screen to the game over screen
                    self.next_screen = 'game_over'
                    self.running = False
                    
            elif p.rect.colliderect(self.player.rect) and p.projectile_type == 'donut':
                chance = random.randint(1, 2)
                if chance == 1:
                    pygame.mixer.Sound('audio/mmmdonuts.wav').play()
                self.projectiles.remove(p)
                self.player_health += 1
                self.health_text = self.test_font.render(f'Health: {self.player_health}', True, (0, 0, 0))

    def update(self):
        self.shoot()
        self.remove_projectile()
        self.get_score()
        self.player.movement()
        self.balloon.update()
        
    def manage_event(self, event):
        if event.type == pygame.QUIT:
            self.next_screen = False
            self.running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            self.next_screen = False
            self.running = False