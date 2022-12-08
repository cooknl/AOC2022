from aocd.models import Puzzle
from pathlib import Path
import sys
from itertools import groupby
import copy

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

stacks, directions = [list(sub) for ele, sub in groupby(txt.splitlines(), key = bool) if ele]

stack_labels = set(stacks.pop(-1))
stack_labels.remove(' ')
stack_count = max(map(int,stack_labels))

stack_trans = [[] for _ in range(len(stacks[0]))]

for ridx, row in enumerate(stacks[::-1]):
    for cidx, col in enumerate(row):
        if col not in ' ':
            stack_trans[cidx].append(col)

real_rows = [i*4 + 1 for i in range(stack_count)]
stack_trans = [ stack_trans[i] for i in real_rows ]

directions_num = [ tuple(map(int,e.replace('move ', '').replace(' from ', ',').replace(' to ', ',').split(','))) for e in directions]

stack_trans_a = copy.deepcopy(stack_trans)
stack_trans_b = copy.deepcopy(stack_trans)

for d_n in directions_num:
    stack_trans_b[d_n[2] - 1].extend(stack_trans_b[d_n[1] - 1][-(d_n[0]):])
    for i_pop in range(d_n[0]):
        stack_trans_a[d_n[2] - 1].append(stack_trans_a[d_n[1] - 1].pop(-1))
        stack_trans_b[d_n[1] - 1].pop(-1)

ans_a_str = ''
ans_b_str = ''
for stack in stack_trans_a:
    ans_a_str += stack[-1]

for stack in stack_trans_b:
    ans_b_str += stack[-1]



print(ans_a_str)
print(ans_b_str)


if dataset in 'input':
    puzzle.answer_a = ans_a_str
    puzzle.answer_b = ans_b_str



