import pygame,sys
from game import Game
from colors import Colors

class TetrisGame:
    def __init__(self,game_speed, high_score):
        pygame.init()
        self.game_speed = game_speed
        self.high_score = high_score
        self.title_font = pygame.font.Font("assets/font.ttf", 25)
        self.score_surface = self.title_font.render("Score", True, Colors.white)
        self.next_surface = self.title_font.render("Next", True, Colors.white)
        self.game_over_surface = self.title_font.render("GAME \nOVER!", True, Colors.white)
        self.title_font_2 = pygame.font.Font("assets/font.ttf", 10)
        self.instruct = self.title_font_2.render("R-Ctrl to reset \n \n  Esc to Main", True, Colors.white)
        self.score_rect = pygame.Rect(320, 55, 170, 60)
        self.next_rect = pygame.Rect(320, 215, 170, 180)
        self.screen = pygame.display.set_mode((500, 620))
        pygame.display.set_caption("Tetris")
        self.clock = pygame.time.Clock()
        self.game = Game()

        self.GAME_UPDATE = pygame.USEREVENT
        pygame.time.set_timer(self.GAME_UPDATE, game_speed)
    
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if self.game.game_over == True:
                        if event.key == pygame.K_RCTRL:
                            self.game.game_over = False
                            self.game.reset()
                        if event.key == pygame.K_ESCAPE:
                            from lobby import MainMenu
                            main = MainMenu()
                            main.main_menu()
                    if event.key == pygame.K_LEFT and self.game.game_over == False:
                        self.game.move_left()
                    if event.key == pygame.K_RIGHT and self.game.game_over == False:
                        self.game.move_right()
                    if event.key == pygame.K_SPACE and self.game.game_over == False:
                        self.game.hard_drop()
                    if event.key == pygame.K_DOWN and self.game.game_over == False:
                        self.game.move_down()
                    if event.key == pygame.K_UP and self.game.game_over == False:
                        self.game.rotate()
                    if event.key == pygame.K_ESCAPE and self.game.game_over == False:
                        pygame.mixer.music.pause()
                        from lobby import MainMenu
                        main = MainMenu()
                        main.main_menu()
                if event.type == self.GAME_UPDATE and self.game.game_over == False:
                    self.game.move_down()

            score_value_surface = self.title_font.render(str(self.game.score), True, Colors.white)

            self.screen.blit(pygame.image.load("assets/BG.jpg"), (0, 0))
            self.screen.blit(self.score_surface, (340, 20, 50, 50))
            self.screen.blit(self.next_surface, (360, 180, 50, 50))

            if self.game.game_over:
                pygame.mixer.music.pause()
                self.screen.blit(self.game_over_surface, (360, 450, 50, 50))
                self.screen.blit(self.instruct, (340, 520, 50, 50))
                if self.game.score > self.high_score:
                    self.high_score = self.game.score
                    with open("score/highscore.txt", "w") as file:
                        file.write(str(self.high_score))
            pygame.draw.rect(self.screen, Colors.dark_grey, self.score_rect, 0, 10)
            self.screen.blit(score_value_surface, score_value_surface.get_rect(centerx=self.score_rect.centerx,centery=self.score_rect.centery))
                                                                     
            pygame.draw.rect(self.screen, Colors.dark_grey, self.next_rect, 0, 10)
            self.game.draw(self.screen)

            pygame.display.update()
            self.clock.tick(60)
