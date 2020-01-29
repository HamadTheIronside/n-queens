import consts
from backtracking import NQueenBackTracking
from ga import NQueenGeneticAlgorithm
from montecarlo import NQueenMonteCarloBackTracking

import time

def main():
    
    # game = NQueenBackTracking(consts.N_COUNT, consts.BLOCK_SIZE)
    # game.set_up()
    # game.run()
    # game.finish()
    
    game = NQueenGeneticAlgorithm(consts.N_COUNT, consts.BLOCK_SIZE)
    game.run()
    
    game.show_progress()
    
    game.set_up()
    game.finish()
    
    
if __name__ == "__main__":
    main()