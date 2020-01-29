import json

consts = None
with open('config.json') as f:
    consts = json.load(f)
    
BG_IMG = consts['backgroundImg']
N_COUNT = consts['n_count']
QUEEN_IMG = consts['queenImg']
BROWN = consts['brown']
WHITE = consts['white']
BLOCK_SIZE = consts['blockSize']
QUEEN_SIZE = (consts['blockSize'], consts['blockSize'])
FIRST_LOC = (consts['blockSize'], consts['blockSize'])
NEXT_LOC = (consts['blockSize'], consts['blockSize'])