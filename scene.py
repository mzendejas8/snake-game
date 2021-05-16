
import pygame
import rgbcolors
import os

import json
import datetime as dt

SCORE = 0
NAME = 'Player1'
DIFF = 5


class Scene:
    def __init__(self, screen):
        self._screen = screen
        self._background = pygame.Surface(self._screen.get_size())
        self._background.fill(rgbcolors.purple)
        self._is_valid = True

    def draw(self):

        self._screen.blit(self._background, (0, 0))
    def process_event(self, event):

        print(str(event))
        if event.type == pygame.QUIT:
            print('Good Bye!')
            self._is_valid = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            print('Bye bye!')
            self._is_valid = False
    def is_valid(self):

        return self._is_valid

    def play_music(self):

        pass
    def stop_music(self):

        pass
    def update(self):

        pass
    def unload_song(self):
        
        pass
   

class TitleScene(Scene):
    def __init__(self, screen, title, title_color, title_size):
        super().__init__(screen)
        self._background.fill(title_color)
        press_any_key_font = pygame.font.Font(pygame.font.get_default_font(), 18)
        self._press_any_key = press_any_key_font.render('Press any key.', True, rgbcolors.black)
        (w, h) = self._screen.get_size()
        self._press_any_key_pos = self._press_any_key.get_rect(center=(w/2, h - 50))
        self._image_folder_path = os.getcwd() + '/Images/SNAKE-2.png'
        self._title = pygame.image.load(self._image_folder_path)
        self._title_pos = (225, w/3)

    def draw(self):
        super().draw()
        self._screen.blit(self._title, self._title_pos)
        self._screen.blit(self._press_any_key, self._press_any_key_pos)
    
    def process_event(self, event):
        super().process_event(event)
        if event.type == pygame.KEYDOWN:
            self._is_valid = False


class InstructionScene(Scene):

    def __init__(self, screen, title, title_color, title_size):
        super().__init__(screen)
        self._background.fill(title_color)
        inst_font = pygame.font.Font(pygame.font.get_default_font(), 17)
        inst_message = "Move the snake using the arrow keys and collect as many apples as possible."
        inst_message2 = "Try to avoid hiting the boudary or the snake crashing into itself."
        self._inst1 = inst_font.render(inst_message, True, rgbcolors.black)
        self._inst2 = inst_font.render(inst_message2, True, rgbcolors.black)
        press_any_key_font = pygame.font.Font(pygame.font.get_default_font(), 18)
        self._press_any_key = press_any_key_font.render('Press e for easy, n for normal, and h for hard.', True, rgbcolors.black)
        (w, h) = self._screen.get_size()
        self._press_any_key_pos = self._press_any_key.get_rect(center = (w / 2, h - 50))
        self._inst1_pos = self._inst1.get_rect(center = (w - 400, h - 700))
        self._inst2_pos = self._inst2.get_rect(center = (w - 400, h - 650))
    
    def draw(self):
        super().draw()
        self._screen.blit(self._press_any_key, self._press_any_key_pos)
        self._screen.blit(self._inst1, self._inst1_pos)
        self._screen.blit(self._inst2, self._inst2_pos)
        
    def process_event(self, event):
        global DIFF
        super().process_event(event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                DIFF = 3
                self._is_valid = False

            elif event.key == pygame.K_n:
                DIFF = 5
                self._is_valid = False
            elif event.key == pygame.K_h:
                DIFF = 9
                self._is_valid = False
        elif event.type == pygame.QUIT:
            pygame.quit()


class GameLevel(Scene):

    def __init__(self, screen, snake, apple):
        super().__init__(screen)
        self._background.fill(rgbcolors.aquamarine)
        self._screen = screen
        self._snake = snake
        self._apple = apple
        global SCORE
        score_font = pygame.font.Font(pygame.font.get_default_font(), 30)
        self._score = score_font.render(f'Score:  {SCORE}', True, rgbcolors.yellow)
        self._score_pos = self._score.get_rect(center = (600, 20))
        self._folder_path = os.getcwd() + '/Sounds/'
        self._sound = pygame.mixer.Sound(self._folder_path + 'eatingsound.wav')
        self._sound2 = pygame.mixer.Sound(self._folder_path + 'crash.wav')
        (w, h) = screen.get_size()
        self._dimension = (w/16, h/16)
        self._boundary_rect = pygame.Rect((0, 0), (w, h))

    def draw_border(self):
        (w, h) = self._screen.get_size()
        pygame.draw.rect(self._screen, rgbcolors.red, self._boundary_rect, (w//100), (h//200))

    def draw(self):
        super().draw()
        self._snake.draw()
        self._apple.draw()
        self._screen.blit(self._score, self._score_pos)
        self.draw_border()
        
    def process_event(self, event):
        super().process_event(event)
        self._snake.process_event(event)



    def write_json(self ,filename, name, score):
        time = 0
        date = dt.date.today()
        d = {'name': name, 'score':score, 'time': str(time), 'date': str(date) } 
        
        print(d)
        with open(filename, 'r+') as fh:
            file_data = json.load(fh)
            file_data.append(d)
            fh.seek(0)
            json.dump(file_data, fh)   

    def update(self):

        global SCORE
        global DIFF
        global NAME
        self._snake.move()
        clock = pygame.time.Clock()
        clock.tick(DIFF)
        if pygame.Rect.collidepoint(self._apple._avatar, (self._snake._snake_body[0]['x'], self._snake._snake_body[0]['y'])):
            self._sound.play()
            self._apple.apple_reset()
            self._snake.grow()
            SCORE += 1
            score_font = pygame.font.Font(pygame.font.get_default_font(), 30)
            self._score = score_font.render(f'Score:  {SCORE}', True, rgbcolors.yellow)
            self._score_pos = self._score.get_rect(center = (600, 20))
        
    def is_valid(self):
        if self._snake.detect_off_screen() or self._snake.detect_snake_collision():
            self._sound2.play()
            self.write_json('scores.json', NAME, SCORE)
            return False
        else:
            return True
    
    def play_music(self):
        pygame.mixer.music.load(self._folder_path + 'game_music.wav')
        pygame.mixer.music.play(-1)
    def stop_music(self):
        pygame.mixer.music.stop()
        pygame.mixer.music.unload()

 
class GameOverScreen(Scene):
    def __init__(self, screen, title, title_color, title_size):
        super().__init__(screen)
        global SCORE
        self._background.fill(rgbcolors.red)
        title_font = pygame.font.Font(pygame.font.get_default_font(), title_size)
        self._title = title_font.render(title, True, rgbcolors.gray)
        press_any_key_font = pygame.font.Font(pygame.font.get_default_font(), 18)
        self._press_any_key = press_any_key_font.render('Press any Key. Your Score: ' + str(SCORE), True, rgbcolors.black)
        (w, h) = self._screen.get_size()
        self._title_pos = self._title.get_rect(center=(w/2, h/2))
        self._press_any_key_pos = self._press_any_key.get_rect(center=(w/2, h - 50))
        self._folder_path = os.getcwd() + '/Sounds'
    
    def draw(self):
        super().draw()
        self._screen.blit(self._title, self._title_pos)
        self._screen.blit(self._press_any_key, self._press_any_key_pos)

    def process_event(self, event):
        super().process_event(event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self._is_valid = False
            if event.key == pygame.K_r:
                self._restart = True
                self._is_valid = False
                
    def play_music(self):
        pygame.mixer.music.load(self._folder_path+'/game_over_sound.wav')
        pygame.mixer.music.play()

    def stop_music(self):
        pass
        pygame.mixer.music.stop()
        pygame.mixer.music.unload()
    def update(self):
        global NAME
        (w, h) = self._screen.get_size()
        press_any_key_font = pygame.font.Font(pygame.font.get_default_font(), 18)
        self._press_any_key = press_any_key_font.render(NAME + '\'s  Score: ' + str(SCORE), True, rgbcolors.black)
        self._title_pos = self._title.get_rect(center=(w/2, h/2))


class enterNameScreen(Scene):
    def __init__(self, screen, title, title_color, title_size):
        super().__init__(screen)
        
        self._background.fill(rgbcolors.purple)
        self._base_font = pygame.font.Font(pygame.font.get_default_font(), 40)
        self._user_text = ''
        self._text_surface = self._base_font.render(self._user_text, True, rgbcolors.black)
        self._input_rect = pygame.Rect(100, 400, 500, 50)
        self._active = False

        message = 'Click on the box and enter your name to keep'
        message2 = 'track of your scores.Press enter when done.'
        self._prompt_font = pygame.font.Font(pygame.font.get_default_font(), 30)
        self._prompt1 = self._prompt_font.render(message, True, rgbcolors.white)
        self._prompt2 = self._prompt_font.render(message2, True, rgbcolors.white)
        
    def draw(self):
        super().draw()
        pygame.draw.rect(self._screen, rgbcolors.white, self._input_rect)
        self._input_rect.w = max(500,self._text_surface.get_width() + 10)
        self._text_surface = self._base_font.render(self._user_text, True, rgbcolors.black)
        self._screen.blit(self._text_surface, (self._input_rect.x + 5, self._input_rect.y + 5))
        self._screen.blit(self._prompt1, (50, 300))
        self._screen.blit(self._prompt2, (50, 350))
        
    def process_event(self,event):
        global NAME
        super().process_event(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self._input_rect.collidepoint(event.pos):
                self._active = True

        if event.type == pygame.KEYDOWN:
            if self._active:
                if event.key == pygame.K_BACKSPACE:
                    self._user_text = self._user_text[:-1]
                elif event.key == pygame.K_RETURN:
                    if not self._user_text:
                        NAME = 'Player1'
                    else:    
                        NAME = self._user_text
                    self._is_valid = False
                else:
                    self._user_text += event.unicode
        self.draw()

    def update(self):
        pass
    def play_music(self):
        pass
    def stop_music(self):
        pass
class highScores(Scene):
    def __init__(self, screen, title, title_size):
        super().__init__(screen)

        self._background.fill(rgbcolors.grey)

    