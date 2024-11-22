import pygame
import sys
from button import Button

class MainMenu:
    def __init__(self):
        self.game_speed = 200
        pygame.init()
        self.SCREEN = pygame.display.set_mode((500, 700))
        pygame.display.set_caption("Menu")
        self.BG = pygame.image.load("assets/BG.jpg")
        try:
            with open("score/highscore.txt", "r") as file:
                self.high_score = int(file.read())
        except FileNotFoundError:
            with open("score/highscore.txt", "w") as file:
                file.write("0")
            self.high_score = 0

    def get_font(self, size):
        return pygame.font.Font("assets/font.ttf", size)

    def play(self):
        from main import TetrisGame
        Game = TetrisGame(self.game_speed,self.high_score)
        Game.run()

    def options(self):
        while True:
            self.SCREEN.blit(self.BG, (0, 0))
            OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
            
            OPTIONS_SPEED = self.get_font(30).render("Game Speed Mode", True, "Yellow")
            OPTIONS_RECT1 = OPTIONS_SPEED.get_rect(center=(250, 100))
            self.SCREEN.blit(OPTIONS_SPEED, OPTIONS_RECT1)
          
            OPTIONS_EASY_SPEED = Button(image=None, pos=(250, 200),
                                            text_input="Easy", font=self.get_font(30), base_color="White",
                                            hovering_color="Green")
            OPTIONS_EASY_SPEED.changeColor(OPTIONS_MOUSE_POS)
            OPTIONS_EASY_SPEED.update(self.SCREEN)

            OPTIONS_MEDIUM_SPEED = Button(image=None, pos=(250, 300),
                                            text_input="Medium", font=self.get_font(30), base_color="White",
                                            hovering_color="Green")
            OPTIONS_MEDIUM_SPEED.changeColor(OPTIONS_MOUSE_POS)
            OPTIONS_MEDIUM_SPEED.update(self.SCREEN)

            OPTIONS_HARD_SPEED = Button(image=None, pos=(250, 400),
                                            text_input="Hard", font=self.get_font(30), base_color="White",
                                            hovering_color="Green")
            OPTIONS_HARD_SPEED.changeColor(OPTIONS_MOUSE_POS)
            OPTIONS_HARD_SPEED.update(self.SCREEN)

            OPTIONS_BACK = Button(image=None, pos=(250, 550),
                                  text_input="BACK", font=self.get_font(20), base_color="Yellow",
                                  hovering_color="Green")
            OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
            OPTIONS_BACK.update(self.SCREEN)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                        self.main_menu()
                    elif OPTIONS_EASY_SPEED.checkForInput(OPTIONS_MOUSE_POS):
                        self.game_speed = 350
                        self.main_menu()
                    elif OPTIONS_MEDIUM_SPEED.checkForInput(OPTIONS_MOUSE_POS):
                        self.game_speed = 200
                        self.main_menu()
                    elif OPTIONS_HARD_SPEED.checkForInput(OPTIONS_MOUSE_POS):
                        self.game_speed = 125
                        self.main_menu()
            pygame.display.update()

    def main_menu(self):
        while True:
            self.SCREEN.blit(self.BG, (0, 0))
            MENU_MOUSE_POS = pygame.mouse.get_pos()
            high_score_surface = self.get_font(20).render("Highest Score: " + str(self.high_score), True, "White")
            high_score_rect = high_score_surface.get_rect(center=(250, 190))
            self.SCREEN.blit(high_score_surface, high_score_rect)
            MENU_TEXT = self.get_font(50).render("MAIN MENU", True, "#F1C40F")
            MENU_RECT = MENU_TEXT.get_rect(center=(250, 120))
            PLAY_BUTTON = Button(image=None, pos=(250, 290),
                                 text_input="PLAY", font=self.get_font(35), base_color="#d7fcd4",
                                 hovering_color="Green")
            OPTIONS_BUTTON = Button(image=None, pos=(250, 400),
                                    text_input="OPTIONS", font=self.get_font(35), base_color="#d7fcd4",
                                    hovering_color="Green")
            QUIT_BUTTON = Button(image=None, pos=(250, 510),
                                 text_input="QUIT", font=self.get_font(35), base_color="#d7fcd4",
                                 hovering_color="Green")
            self.SCREEN.blit(MENU_TEXT, MENU_RECT)
            for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
                button.changeColor(MENU_MOUSE_POS)
                button.update(self.SCREEN)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                        self.play()
                    if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                        self.options()
                    if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                        with open("score/highscore.txt", "w") as file:
                            file.write("0")
                        pygame.quit()
                        sys.exit()
            pygame.display.update()

menu = MainMenu()
menu.main_menu()