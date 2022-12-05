import pygame
from screens import BaseScreen
from sys import exit
import datetime
import json

class GameOver(BaseScreen):
    """
    This class represents the game over screen.

    Args:
        BaseScreen (_type_): This class inherits from the BaseScreen class.
    """
    def __init__(self, window, score):
        super().__init__(window)
        # game over screen sound
        game_over_sound = pygame.mixer.Sound('audio/game_over.wav')
        game_over_sound.play()
        self.final_score = score 

        # default username
        self.username = ""

        # get the buttons
        self.start_button = pygame.image.load('images/buttons/start_button.png')
        self.quit_button = pygame.image.load('images/buttons/quit_button.png')

        # scale the buttons
        self.start_button = pygame.transform.rotozoom(self.start_button, 0, 0.5)
        self.quit_button = pygame.transform.rotozoom(self.quit_button, 0, 0.5)

        # textbox for the user to enter a username
        self.username_textbox = pygame.Rect(75, 300, 200, 50)
        self.type_username = False

        # rectangle for save button
        self.save_button = pygame.Rect(290, 300, 100, 50)

        # save button text
        self.save_text = self.test_font.render("Save", True, (255,255,255))
        self.save_text_rect = self.save_text.get_rect(center=(340,325))

        # variable to check if the score has been uploaded
        self.display_message = False

        with open('scores.json', 'r') as f:
            self.scores = json.load(f)

    def update(self):
        pass 

    def draw(self):
        """
        This method will draw the game over screen.
        """
        game_over_background = pygame.image.load('images/game_over_bg.png')

        # score text
        score_text = self.test_font.render(f"Score: {self.final_score}", True, (255,255,0))
        score_text = pygame.transform.rotozoom(score_text, 0, 1.75)
        score_text_rect = score_text.get_rect(center=(200,400))
        
        self.window.blit(game_over_background, (0,0))

        # game over text
        game_over_text = pygame.image.load('images/game_over.png')
        game_over_text = pygame.transform.rotozoom(game_over_text, 0, 0.75)

        # put the game over text in the middle of the screen
        game_over_text_rect = game_over_text.get_rect(center=(200,250))

        # set the buttons side by side near the bottom of the screen
        self.start_button_rect = self.start_button.get_rect(center=(100,475))
        self.quit_button_rect = self.quit_button.get_rect(center=(300,475))

        # display the start button and quit button
        self.window.blit(self.start_button, self.start_button_rect)
        self.window.blit(self.quit_button, self.quit_button_rect)

        # display the game over text
        self.window.blit(game_over_text, game_over_text_rect)

        # display the score text
        self.window.blit(score_text, score_text_rect)

        # textbox for the user to enter a username
        pygame.draw.rect(self.window, (255,255,255), self.username_textbox)
        username_text = self.test_font.render(self.username, True, (0,0,0))
        username_text_rect = username_text.get_rect(center=(175,325))
        self.window.blit(username_text, username_text_rect)

        # save button
        pygame.draw.rect(self.window, (0,0,0), self.save_button)
        self.window.blit(self.save_text, self.save_text_rect)

        # display a message if the score has been uploaded
        if self.display_message:
            uploaded_text = self.test_font.render("Score uploaded!", True, (255,255,0))
            uploaded_text = pygame.transform.rotozoom(uploaded_text, 0, 1.5)
            uploaded_text_rect = uploaded_text.get_rect(center=(200,325))
            self.window.blit(uploaded_text, uploaded_text_rect)
        

    def upload_score(self):
        """
        This method will upload the score to the scores.json file.
        """
        # upload the username and score to the database
                # if the username is empty self.username will be "Unknown"
        if self.username == "":
            self.username = "Unknown"
        # get the current date and time
        now = datetime.datetime.now()

        # format the date and time
        date = now.strftime("%Y-%m-%d %H:%M:%S")

        # add the username, score, and date to the database
        self.scores.append({"username": self.username, "score": self.final_score, "date": date})

        # sort the scores by the highest score
        self.scores = sorted(self.scores, key=lambda k: k['score'], reverse=True)
        # save the scores to the database
        with open('scores.json', 'w') as f:
            json.dump(self.scores, f, indent=4)
            
    def manage_event(self, event):
        """
        This method will manage the events for the game over screen.

        Args:
            event (_type_): This is the event that is passed in.
        """
        # when start button is clicked move to game screen
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.start_button_rect.collidepoint(event.pos):
                self.start_time += pygame.time.get_ticks() // 1000
                self.next_screen = "game"
                self.running = False

            # when quit button is clicked quit the game
            if self.quit_button_rect.collidepoint(event.pos):
                pygame.quit()
                exit()

        # when the user clicks on the textbox allow them to type a username
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.username_textbox.collidepoint(event.pos):
                self.type_username = True
            else:
                self.type_username = False

        # when the user types a username display it in the textbox
        if event.type == pygame.KEYDOWN:
            if self.type_username:
                if event.key == pygame.K_BACKSPACE:
                    self.username = self.username[:-1]
                elif event.unicode.isalnum() and len(self.username) < 10:
                    self.username += event.unicode

        # when user presses the save button upload the score to the database and remove the textbox and save button
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.save_button.collidepoint(event.pos):
                self.upload_score()
                
                # remove the username textbox and save button after the score is uploaded
                self.username_textbox = pygame.Rect(0,0,0,0)
                self.save_button = pygame.Rect(0,0,0,0)
                self.username = ""
                self.save_text_rect = self.save_text.get_rect(center=(0,0))

                # add a message saying the score was uploaded
                self.display_message = True