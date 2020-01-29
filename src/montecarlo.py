from backtracking import NQueenBackTracking
import random

class NQueenMonteCarloBackTracking(NQueenBackTracking):
    
    def __init__(self, n_count, block_size):
        super().__init__(n_count, block_size)
    
    def montecarlo(self, numbers=1):
        result = 0
        loop = numbers
        while loop:
            self.queens = {}
            i, m, numnodes, mprod = 0, 1, 1, 1

            while m != 0 and i != self.get_count:
                mprod *= m
                numnodes += mprod * self.get_count
                valid = {}
                m = 0
        
                for j in range(0, self.get_count):
                    self.queens[i] = j
                    if self.is_promising(i, k=0):
                        m += 1
                        valid[m] = j
                
                if m != 0:
                    j = random.choice(list(valid.keys()))
                    self.queens[i] = valid[j]
                
                i += 1
                            
            result += numnodes
            loop -= 1

        return int((result/numbers)) # avg
        
    def run(self):
        print(self.montecarlo(numbers=1000))