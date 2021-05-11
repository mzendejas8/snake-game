
import pygame
import rgbcolors
import time 

LEVELDIFF = 12

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
        # title_font = pygame.font.Font(pygame.font.get_default_font(), title_size)
        # self._title = title_font.render(title, True, rgbcolors.gray)
        press_any_key_font = pygame.font.Font(pygame.font.get_default_font(), 18)
        self._press_any_key = press_any_key_font.render('Press any key.', True, rgbcolors.black)
        (w, h) = self._screen.get_size()
        # self._title_pos = self._title.get_rect(center=(w/2, h/2))
        self._press_any_key_pos = self._press_any_key.get_rect(center=(w/2, h - 50))
        self._title = pygame.image.load('SNAKE-2.png')
        self._title_pos = (225,w/3)


    
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
        # title_font = pygame.font.Font(pygame.font.get_default_font(), title_size)
        # self._title = title_font.render(title, True, rgbcolors.gray)
        press_any_key_font = pygame.font.Font(pygame.font.get_default_font(), 18)
        self._press_any_key = press_any_key_font.render('Press any key.', True, rgbcolors.black)
        (w, h) = self._screen.get_size()
        # self._title_pos = self._title.get_rect(center=(w/2, h/2))
        self._press_any_key_pos = self._press_any_key.get_rect(center=(w/2, h - 50))
        self._title = pygame.image.load('SNAKE-2.png')
        self._title_pos = (225,w/3)


    
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

        self._sound = pygame.mixer.Sound('eatingsound.mp3')
        self._sound2 = pygame.mixer.Sound('crash.mp3')


        (w,h) = screen.get_size()
        self._dimension = (w/16,h/16)

        
        
        


    def draw_border(self):
        
        for i in range(0, 800,50):
            border = pygame.Rect((-46,i),self._dimension)
            pygame.draw.rect(self._screen,rgbcolors.red,border)
        for i in range(0, 800,50):
            border = pygame.Rect((796,i),self._dimension)
            pygame.draw.rect(self._screen,rgbcolors.red,border)

        for i in range(0, 800,50):
            border = pygame.Rect((i,-46),self._dimension)
            pygame.draw.rect(self._screen,rgbcolors.red,border)
        for i in range(0, 800,50):
            border = pygame.Rect((i,796),self._dimension)
            pygame.draw.rect(self._screen,rgbcolors.red,border)


    
    
    def draw(self):
        super().draw()
        self._snake.draw()
        self._apple.draw()
        self._screen.blit(self._score,self._score_pos)

        self.draw_border()
        
    
    def process_event(self, event):
        super().process_event(event)
        self._snake.process_event(event)


    def update(self):
        
        self._snake.move()
        
        # time.sleep(0.9)
        clock = pygame.time.Clock()
        clock.tick(LEVELDIFF)
        if pygame.Rect.collidepoint(self._apple._avatar,(self._snake._snake_body[0]['x'],self._snake._snake_body[0]['y'])):
            self._sound.play()
            self._apple.apple_reset()
            self._snake.grow()
            self._game_score +=1
            score_font = pygame.font.Font(pygame.font.get_default_font(),30)
            self._score = score_font.render(f'Score:  {self._game_score}', True, rgbcolors.yellow)
            self._score_pos = self._score.get_rect(center = (600,20))

        
    def is_valid(self):
        if self._snake.detect_off_screen() or self._snake.detect_snake_collision():
            self._sound2.play()
            return False
        else:
            return True
    
    def play_music(self):
        pygame.mixer.music.load('game_music.mp3')
        pygame.mixer.music.play(-1)
    def stop_music(self):
        pygame.mixer.music.stop()
        pygame.mixer.music.unload()


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

    def play_music(self):
        pygame.mixer.music.load('game_over_sound.mp3')
        pygame.mixer.music.play()

    def stop_music(self):
        pass
        pygame.mixer.music.stop()
        pygame.mixer.music.unload()

            
            


        
    
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
        
    