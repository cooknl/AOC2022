from aocd.models import Puzzle
from pathlib import Path, PurePosixPath
import sys
import numpy as np
from io import StringIO



this_f = Path(__file__).name
y = this_f[:4]
d = int(this_f[7:9])
puzzle = Puzzle(year=y, day=d)


def get_data(v='toy'):
    n = y + 'day' + f'{d:02d}' + v + '.txt' 
    p = Path(__file__).with_name(n)

    if (p.exists()):
        with p.open() as f:
            return f.read()
    elif v in 'toy':
        sys.exit('Get the toy data')
    elif v in 'input':
        input_data = puzzle.input_data
        with p.open('w') as f:
            f.write(input_data)
        return input_data

dataset = 'input'
txt = get_data(v=dataset)

trees = np.genfromtxt(StringIO(txt), delimiter=1, dtype=int)

r, c = trees.shape

seen = np.zeros((r, c), dtype=bool)
scores = np.zeros((r,c), dtype=int)

def tall_to_be_seen(val, array):
    if array.size == 0:
        return True
    elif (val > array.max()):
        return True
    else:        
        return False

def dist_to_see(val, array):
    # print( val, array)
    view_count = 0
    if array.size == 0:
        return view_count
    for height in array:
        view_count += 1
        if val <= height:
            break
    # print(view_count)
    return view_count


for row in range(r):
    for col in range(c):
        current = False
        score = 1
        tree = trees[row,col]
        for arr in (np.flip(trees[row,:col]), trees[row,col+1:], np.flip(trees[:row,col]), trees[row+1:,col]):
            current = current or tall_to_be_seen(tree, arr)
            score *= dist_to_see(tree, arr)
        seen[row, col] = current
        scores[row, col] = score

# print(trees)
# print(seen)
# print(scores)


if dataset in 'input':
    puzzle.answer_a = np.count_nonzero(seen)
    puzzle.answer_b = np.amax(scores)
