from aocd.models import Puzzle
from pathlib import Path
import sys
from collections import Counter

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

def get_start_of_packet(datastream, distinct):
    past_distinct = list(datastream[:distinct])
    for i, c in enumerate(datastream[distinct:]):
        b = Counter(past_distinct)
        if b.most_common(1)[0][1] == 1:
            return i + distinct
        else:
            past_distinct.append(c)
            past_distinct.pop(0)
    return None

if dataset in 'toy':
    t_lines = txt.splitlines()
    print(t_lines)
    for l in t_lines:
        print(l, ": ", get_start_of_packet(l))

if dataset in 'input':
    puzzle.answer_a = get_start_of_packet(txt, 4)
    puzzle.answer_b = get_start_of_packet(txt, 14)