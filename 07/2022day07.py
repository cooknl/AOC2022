from aocd.models import Puzzle
from pathlib import Path, PurePosixPath
import sys
from collections import defaultdict


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

dir_sums = defaultdict(lambda: 0)
dir_tots = defaultdict(lambda: 0)
cwd = PurePosixPath()
dirs = set()
grand_total = 0
total_check = 0

for l in txt.splitlines():
    if '$ cd' in l:
        dir = l[5:]
        print(dir)
        if dir in '..':
            cwd = cwd.parent
        else:
            cwd = cwd / l[5:]
            dirs.add(l[5:])
            print(cwd)
    elif l[0].isnumeric():
        print(l)
        dir_sums[cwd] += int(l.split(' ')[0])
        grand_total += int(l.split(' ')[0])

for key in dir_sums.keys():
    for dir in dirs:
        if dir in str(key):
            dir_tots[dir] += dir_sums[key]

ans_a = 0

for k, v in dir_tots.items():
    # print(k, ': ', v)
    total_check += v
    if v <= 100000:
        # print('    ', v, ' <= 100000')
        ans_a += v

print(grand_total, " : ", total_check)

if dataset in 'input':
    puzzle.answer_a = ans_a
    # puzzle.answer_b = get_start_of_packet(txt, 14)

