
import pygame
import rgbcolors
import time 

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
    
    def update(self):
        pass

class TitleScene(Scene):
    def __init__(self, screen, title, title_color, title_size):
        super().__init__(screen)
        self._background.fill(rgbcolors.green3)
        title_font = pygame.font.Font(pygame.font.get_default_font(), title_size)
        self._title = title_font.render(title, True, rgbcolors.gray)
        press_any_key_font = pygame.font.Font(pygame.font.get_default_font(), 18)
        self._press_any_key = press_any_key_font.render('Press any key.', True, rgbcolors.black)
        (w, h) = self._screen.get_size()
        self._title_pos = self._title.get_rect(center=(w/2, h/2))
        self._press_any_key_pos = self._press_any_key.get_rect(center=(w/2, h - 50))
    
    def draw(self):
        super().draw()
        self._screen.blit(self._title, self._title_pos)
        self._screen.blit(self._press_any_key, self._press_any_key_pos)
    
    def process_event(self, event):
        super().process_event(event)
        if event.type == pygame.KEYDOWN:
            self._is_valid = False



class GameOverScreen(Scene):
    def __init__(self, screen, title, title_color, title_size):
        super().__init__(screen)
        self._background.fill(rgbcolors.red)
        title_font = pygame.font.Font(pygame.font.get_default_font(), title_size)
        self._title = title_font.render(title, True, rgbcolors.gray)
        press_any_key_font = pygame.font.Font(pygame.font.get_default_font(), 18)
        self._press_any_key = press_any_key_font.render('Press any Key', True, rgbcolors.black)
        (w, h) = self._screen.get_size()
        self._title_pos = self._title.get_rect(center=(w/2, h/2))
        self._press_any_key_pos = self._press_any_key.get_rect(center=(w/2, h - 50))
    
    def draw(self):
        super().draw()
        self._screen.blit(self._title, self._title_pos)
        self._screen.blit(self._press_any_key, self._press_any_key_pos)
    
    def process_event(self, event):
        super().process_event(event)
        if event.type == pygame.KEYDOWN:
            self._is_valid = False
    



class GameLevel(Scene):
    def __init__(self, screen, snake, apple):
        super().__init__(screen)
        self._background.fill(rgbcolors.aquamarine)
        self._screen = screen
        self._snake = snake
        self._apple = apple

        self._game_score = 0

        score_font = pygame.font.Font(pygame.font.get_default_font(),30)
        self._score = score_font.render(f'Score:  {self._game_score}', True, rgbcolors.yellow)
        self._score_pos = self._score.get_rect(center = (600,20))


    
    
    def draw(self):
        super().draw()
        self._snake.draw()
        self._apple.draw()
        self._screen.blit(self._score,self._score_pos)
    
    def process_event(self, event):
        super().process_event(event)
        self._snake.process_event(event)


    def update(self):
        self._snake.move()
        time.sleep(0.3)
        if pygame.Rect.collidepoint(self._apple._avatar,(self._snake._worm_body[0]['x'],self._snake._worm_body[0]['y'])):
            self._apple.apple_reset()
            self._snake.grow()
            self._game_score +=1
            score_font = pygame.font.Font(pygame.font.get_default_font(),30)
            self._score = score_font.render(f'Score:  {self._game_score}', True, rgbcolors.yellow)
            self._score_pos = self._score.get_rect(center = (600,20))

        
    def is_valid(self):
        if self._snake.detect_off_screen():
            return False
        else:
            return True

            
            


        
    
class GameLevelX(Scene):
    def __init__(self, screen, snake, food_frequency, snake_speed, hazard_list, level_time, bonus_frequency, portal_list):
        pass
    
    def draw(self):
        super().draw()
        snake.draw()
    
    def process_event(self, event):
        super().process_event(event)
        
    def update(self):
        super().update()
        # does the snake intersect itself
        # did the snake eat food?
        # did the snake grow?
        # where did the snake move to?
        # Is there a new piece of food?
        # Is there a new bonus?
        # How much time has passed?
        # Has the nake left the board?
        
    