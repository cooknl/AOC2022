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



cwd = PurePosixPath()

list_of_path_file = []


for l in txt.splitlines():
    if '$ cd' in l:
        dir = l[5:]

        if dir in '..':
            cwd = cwd.parent
        else:
            cwd = cwd / l[5:]
    elif l[0].isnumeric():
        size, file = l.split(' ')
        list_of_path_file.append(','.join([str(cwd / file), size + '\n']))

with open(Path(__file__).with_name('2022day07explore.txt'),'w') as f:
    f.writelines(list_of_path_file)