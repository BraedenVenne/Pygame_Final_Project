import pygame
import random
from screens import BaseScreen
from components import Player, MAX_WIDTH, MAX_HEIGHT, Balloon, Projectile

class GameScreen(BaseScreen):
    """
    This class represents the game screen

    Args:
        BaseScreen (_type_): This is the base screen class that all other screens will inherit from.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sky_surf = pygame.image.load('images/background.png')
        self.player = Player(MAX_WIDTH / 2, MAX_HEIGHT - 50)
        self.balloon = Balloon(MAX_WIDTH / 2, 130)
        self.projectiles = []
        self.player_health = 5
        self.health_text = self.test_font.render(f'Health: {self.player_health}', True, (0, 0, 0))
        self.speed_increase = 10
        self.balloon_speed = 1
        self.donut_count = 0
        self.final_score = 0

    def balloon_speed_increase(self):
        """
        This method will increase the speed of the balloon as the game progresses.
        """
        if self.score > self.speed_increase and self.score > 0 and self.balloon.speed > 0:
            self.balloon.speed -= 1
            self.balloon_speed += 1
            self.balloon.speed = self.balloon_speed
            self.speed_increase += 20

    def shoot_chance(self):
        """
        This method will randomly generate a number between 1 and 100. 
        If the number is 1, then the balloon will shoot a projectile.
        """
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
        """
        This method will draw the background, player, balloon, and projectiles to the screen.
        """
        self.window.blit(self.sky_surf, (0, 0))
        self.player.update(self.window)
        self.balloon.draw(self.window)
        for p in self.projectiles:
            p.update(self.window)
        # draw the health to the top right of the screen
        self.window.blit(self.health_text, (MAX_WIDTH - 150, 10))
        # draw the score to the top left of the screen
        self.window.blit(self.test_font.render(f'Score: {self.score}', True, (0, 0, 0)), (10, 10))

    def shoot(self):
        """
        This method handles the projectile collisions. 
        """
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
                    # change the screen to the game over screen
                    self.final_score = self.score
                    self.next_screen = 'game_over'
                    self.running = False
                    
            elif p.rect.colliderect(self.player.rect) and p.projectile_type == 'donut':
                self.projectiles.remove(p)
                self.donut_count += 1
                if self.donut_count == 2:
                    pygame.mixer.Sound('audio/mmmdonuts.wav').play()
                    # if player has 2 donuts, then heal the player
                    self.player_health += 1
                    self.health_text = self.test_font.render(f'Health: {self.player_health}', True, (0, 0, 0))
                    self.donut_count = 0

    def update(self):
        """
        This function will update the game screen.
        """
        self.shoot_chance()
        self.shoot()
        self.score = (pygame.time.get_ticks() // 1000) - self.start_time
        self.balloon_speed_increase()
        self.player.movement()
        self.balloon.update()
        
    def manage_event(self, event):
        """
        This method will handle the events for the game screen.

        Args:
            event (_type_): This is the event that is passed in from the main loop.
        """
        if event.type == pygame.QUIT:
            self.next_screen = False
            self.running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            self.next_screen = False
            self.running = False