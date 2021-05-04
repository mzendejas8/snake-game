
import pygame
import rgbcolors

class SnakePlayer:
    def __init__(self, screen):
        self._screen = screen
        (w, h) = screen.get_size()
        self._dimension = (w/16, h/16)



        self._snake_body = [{'x':400,'y': 400}]
        self._avatar = pygame.Rect((400, 400), self._dimension)
        self._direction = ''

    
    def grow(self):

        head_x = self._snake_body[0]['x']
        head_y = self._snake_body[0]['y']

        if self._direction == 'down':
            self._snake_body.insert(0,{'x': head_x,'y':head_y+50})

        elif self._direction == 'up':
            self._snake_body.insert(0,{'x': head_x,'y':head_y-50})
            
        elif self._direction == 'right':
            self._snake_body.insert(0,{'x': head_x+50,'y':head_y})

        elif self._direction == 'left':
            self._snake_body.insert(0,{'x': head_x-50,'y':head_y})  

        self.draw()
        

       
    
    def move(self):
        if self._direction == 'down':
            self._snake_body.insert(0, {'x':self._snake_body[0]['x'],'y':self._snake_body[0]['y']+50})
            self._snake_body.pop()

        elif self._direction == 'up':
            self._snake_body.insert(0, {'x':self._snake_body[0]['x'],'y':self._snake_body[0]['y']-50})
            self._snake_body.pop()            
            
        elif self._direction == 'right':
            self._snake_body.insert(0, {'x':self._snake_body[0]['x']+50,'y':self._snake_body[0]['y']})
            self._snake_body.pop()   

        elif self._direction == 'left':
            self._snake_body.insert(0, {'x':self._snake_body[0]['x']-50,'y':self._snake_body[0]['y']})
            self._snake_body.pop()   
    
        self.draw()
        
    
    def detect_off_screen(self):
        if self._snake_body[0]['x']>= 800 or self._snake_body[0]['x'] < 0 or self._snake_body[0]['y'] < 0 or self._snake_body[0]['y']>=800:
            return True
        else:
            return False
    
    def detect_snake_collision(self):
        for i in range(1,len(self._snake_body)):
            if self._snake_body[0]['x'] == self._snake_body[i]['x'] and  self._snake_body[0]['y'] == self._snake_body[i]['y']:
                return True



    def process_event(self, event):
        if event.type == pygame.QUIT:
            pygame.QUIT()

        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_RIGHT and self._direction != 'left':
                print('right arrow key pressed!')
                self._direction = 'right'
                
            elif event.key == pygame.K_LEFT and self._direction != 'right':
                print('left arrow key pressed!')
                self._direction = 'left'
                
            elif event.key == pygame.K_UP and self._direction != 'down':
                print('up arrow key pressed!')
                self._direction = 'up'
                
            elif event.key == pygame.K_DOWN and self._direction != 'up':
                print('down arrow key pressed!')
                self._direction = 'down'
            
               
        
    def draw(self):

        for wormcords in self._snake_body:
            self._avatar = pygame.Rect((wormcords['x'],wormcords['y'] ), self._dimension)
            pygame.draw.rect(self._screen, rgbcolors.green, self._avatar)


     

    


