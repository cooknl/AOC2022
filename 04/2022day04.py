from aocd.models import Puzzle
from pathlib import Path
import sys
import operator
import math

this_f = Path(__file__).name
y = this_f[:4]
d = int(this_f[7:9])
puzzle = Puzzle(year=y, day=d)

def get_data(v='toy'):
    n = y + 'day' + f'{d:02d}' + v + '.txt' #'2022day01toy.txt'
    p = Path(__file__).with_name(n)

    if (Path(n).exists()):
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

ans_a_list = []
ans_b_list = []

for s in txt.splitlines():
    tups_pre = [ tuple(map(int,p.split('-'))) for p in s.split(',')  ]
    # Part 1
    tups = [(t[0], t[1]-t[0])  for t in tups_pre]    
    tups_sub = (tuple(map(operator.sub,tups[0],tups[1])))    
    ans_a_list.append( (abs(tups_sub[0]) <= abs(tups_sub[1])) and ( (math.prod(tups_sub) <= 0)))
    # Part 2
    tups_sort = sorted(tups_pre, key=lambda x: x[0])
    ans_b_list.append(tups_sort[0][1] >= tups_sort[1][0])

if dataset in 'input':
    puzzle.answer_a = ans_a_list.count(True)
    puzzle.answer_b = ans_b_list.count(True)



