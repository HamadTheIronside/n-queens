import pygame
import consts
import sys
import shutil
from datetime import datetime

class GameManager:
    screen = None
    start_time = None
    finish_time = None
    background_img = None

    queens = {}
    
    def __init__(self, n_count, block_size):
        self.block_size = block_size
        self.n_count = n_count
    
    @property
    def get_size(self):
        return (self.get_count_all * consts.BLOCK_SIZE, self.get_count_all * consts.BLOCK_SIZE)
    
    @property
    def get_image_name(self):
        return 'Chess{}_[{}x{}].png'.format(self.get_count, self.get_count_all, self.get_count_all)
    
    def set_up(self):
        '''
            set up the pygame
        '''
        pygame.init()
        
        self.screen = pygame.display.set_mode(self.get_size)
        
        self.brown = pygame.image.load(consts.BROWN)
        self.white = pygame.image.load(consts.WHITE)
        self.queenImg = pygame.image.load(consts.QUEEN_IMG)
        
        self.setup_draw_bg()
    
    @property
    def get_count(self):
        return self.n_count
    
    @property
    def get_count_all(self):
        return self.n_count + 2
    
    def setup_draw_bg(self):
        try:
            if not self.background_img:
                self.background_img = pygame.image.load(self.get_image_name)
        except Exception as e:
            self.table = []
            for i in range(self.get_count_all):
                self.table.append((i*self.block_size,0,True))
                self.table.append((0,i*self.block_size,True))
                self.table.append(((self.get_count+1)*self.block_size,i*self.block_size,True))
                self.table.append((i*self.block_size,(self.get_count+1)*self.block_size,True))
            
            for i in range(1,self.get_count+1):
                for j in range(1,self.get_count+1):
                    if (i+j) % 2 == 0:
                        self.table.append((i*self.block_size,j*self.block_size,True))
                    else:
                        self.table.append((i*self.block_size,j*self.block_size,False))
            
            for x, y, type in self.table:
                self.screen.blit(pygame.transform.scale(self.brown if type else self.white, consts.QUEEN_SIZE), (x,y))

            pygame.display.update()
            pygame.image.save(self.screen, self.get_image_name)
            self.background_img = pygame.image.load(self.get_image_name)

        finally:
            self.screen.blit(pygame.transform.scale(self.background_img, self.get_size), (0, 0))
        
        
    def handle_game_view(self, t=0):
        '''
            handle the pygame stuff such as if anykey pressed or showing the bg and the queens
        '''
        
        for event in pygame.event.get():
            if event.type in (pygame.QUIT, pygame.KEYDOWN):
                sys.exit()
                
        self.setup_draw_bg()
        self.draw_queens()
        
        pygame.display.update()
        pygame.time.wait(t)
        
    
    def finish(self):
        while True:
            self.handle_game_view()
            pygame.time.wait(200)
            
            
    def draw_queens(self):
        '''
            draws all the queens on the screen
        '''
        for queen in self.queens.items():
            self.screen.blit(pygame.transform.scale(self.queenImg, consts.QUEEN_SIZE), self.get_loc(queen))

    def get_loc(self, loc):
        '''
            gets x, y and turn it into pixel locations to put the img on the game
        '''
        return (loc[0] * consts.NEXT_LOC[0] + consts.FIRST_LOC[0], loc[1] * consts.NEXT_LOC[1] + consts.FIRST_LOC[1])
    
    def log(self):
        '''
            return time.now with all the queens location
        '''
        return (datetime.now().time(), self.queens)
    
    def run(self):
        pass