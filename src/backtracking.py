from game_manager import GameManager

class NQueenBackTracking(GameManager):
    active = True
    def __init__(self, n_count, block_size):
        super().__init__(n_count, block_size)
        
    def is_promising(self, queen_index, k=0):
        '''
            check if the givin index is not under threat
        '''
        safe = True
        
        while safe and k < queen_index:
            if self.queens[k] == self.queens[queen_index] or abs(self.queens[k] - self.queens[queen_index]) == abs(k - queen_index):
                safe = False
            k += 1
        
        return safe
    
    def handle(self, i):
        '''
            check if the current queen is valid
            if not go to next column
            
            if all queens places rightfully:
                finish the game
        '''
        self.handle_game_view()
        if self.is_promising(i):
            if i != self.n_count - 1:
                for j in range(self.n_count):
                    self.queens[i + 1] = j
                    self.handle(i + 1)
                    if not self.active:
                        break
            else:
                self.finish()
        else:
            self.queens.pop(i)
            
    def run(self):
        self.handle(-1)
        
    def finish(self):
        self.active = False
        
        super().finish()