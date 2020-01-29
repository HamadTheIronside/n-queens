from game_manager import GameManager
import random, collections

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class NQueenGeneticAlgorithm(GameManager):
    
    environment = []
    goal_index = None
    goal = None
    data = []
    
    def __init__(self, n_count, block_size):
        self.n_count = n_count
        super().__init__(n_count, block_size)
    
    def generate_dna(self):
        '''
        generating a gen of n queens with random postitions
        '''
        
        dna = list(range(self.n_count))
        
        random.shuffle(dna)
        while dna in self.environment:
            random.shuffle(dna)

        return dna
        
    def isgoal_gen(self, gen):
        '''
        checking if a gen has no hits
        '''
        return True if self.utility_gen(gen) == 0 else False
    
    def initilize_first_gen(self):
        '''
        generating the first generations [500 gens]
        '''
        for i in range(100):
            self.environment.append(self.generate_dna()) 
    
    def utility_gen(self, gen):
        '''
            check the hits of a generation
        '''
                
        hits = 0
        
        for i in range(self.n_count):
            for j in range(self.n_count):
                if i != j:
                    if abs(j - i) == abs(gen[j] - gen[i]):
                        hits += 1
            
        return hits
             
    def crossover_gen(self, first_gen, second_gen):
        '''
            cross overing two gens (it could be good or bad)
        '''
        for i in range(1, self.n_count):
            if abs(first_gen[i - 1] - first_gen[i]) < 2:
                first_gen[i], second_gen[i] = second_gen[i], first_gen[i]
                
            if abs(second_gen[i - 1] - second_gen[i]) < 2:
                first_gen[i], second_gen[i] = second_gen[i], first_gen[i]
        
        return first_gen, second_gen
    
    def mutate_gen(self, gen):
        '''
            as we know we have some duplicated y's in our generation [e.g: (4,6,1,3,6,8,2,1)],
            we have to fix it to decress the hits
            also we switch a y from left to the right randomly
        '''
        new_generation = list(dict.fromkeys(gen))
        
        half = int(self.n_count/2)
        left = random.randint(0, half)
        right = random.randint(half, self.n_count - 1)
        
        for y in range(self.n_count):
            if y not in new_generation:
                new_generation.append(y)
        
        new_generation[left], new_generation[right] = new_generation[right], new_generation[left]
                
        return new_generation
    
    def fight(self):
        '''
            picking the best gens out of all in the environment
        '''
        
        gen_hits = []
        new_environment = []
        # get the hits of all generations
        for gen in self.environment:
            gen_hits.append(self.utility_gen(gen))
            
        # check if we have the goal gen (hit == 0)
        min_hits = min(gen_hits)
        self.data.append([min(gen_hits), max(gen_hits)])
        
        if min_hits == 0:
            self.goal_index = gen_hits.index(min_hits)
            return 
        
                
        # pick the gens with the minimum hits
        while len(new_environment) != 100:
            min_hits = min(gen_hits)
            
            gen = gen_hits.index(min_hits)
            gen = self.environment[gen]
            
            new_environment.append(gen)
            
            gen_hits.remove(min_hits)
            self.environment.remove(gen)
        
        self.environment = new_environment
        
    def handle(self):
        '''
            start solving the problem
            1: initilize the first gen
            2: check if we have the solution already 
            3: if not continue
            4: cross over two gens
            5: mutate them
            6: adding them to the env again
            7: fight
            8: check if we got the solution
            9: if not then repeat from step 4
        '''
        
        
        self.initilize_first_gen()
        
        for gen in self.environment:
            if self.isgoal_gen(gen):
                self.goal = gen
                return
        
        self.counter = 0 
        
        while True:
            for index in range(1, len(self.environment), 2):
                first_gen, second_gen = self.environment[index-1], self.environment[index]

                self.crossover_gen(first_gen, second_gen)
        
                first_gen = self.mutate_gen(first_gen)
                second_gen = self.mutate_gen(second_gen)
                
                self.environment.append(first_gen)
                self.environment.append(second_gen)
                
            self.counter += 1
            self.fight()
            
            if self.goal_index:
                self.goal = self.environment[self.goal_index]
                return

    def convertor(self, gen):
        '''
        convert the generation and put it into queens to show it on the page
        '''
        self.queens = {i: gen[i] for i in gen}
    
    def run(self):
        self.handle()
    
    def show_progress(self):
        sns.set()

        d = pd.DataFrame(data=self.data)

        sns.lineplot(data=d, palette='tab10', linewidth=2.5)

        plt.ylabel("Hits of the Generation")
        plt.xlabel("Environments")
        plt.show()
    
    def finish(self):
        self.convertor(self.goal)
        
        super().finish()