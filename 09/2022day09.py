from aocd.models import Puzzle
from pathlib import Path, PurePosixPath
import sys
import operator



this_f = Path(__file__).name
y = this_f[:4]
d = int(this_f[7:9])
puzzle = Puzzle(year=y, day=d)


def get_data(v='toya'):
    n = y + 'day' + f'{d:02d}' + v + '.txt' 
    p = Path(__file__).with_name(n)

    if (p.exists()):
        with p.open() as f:
            return f.read()
    elif v in 'toya':
        sys.exit('Get the toy a data')
    elif v in 'toyb':
        sys.exit('Get the toy b data')
    elif v in 'input':
        input_data = puzzle.input_data
        with p.open('w') as f:
            f.write(input_data)
        return input_data

dataset = 'toya'
txt = get_data(v=dataset)

# print(txt)


motions = [(l[0], int(l[2:]))  for l in txt.splitlines() ]

# print(motions)

def chebyshev(positions: list[tuple, tuple]) -> int:
    # https://towardsdatascience.com/9-distance-measures-in-data-science-918109d069fa
    # D(x, y) = max_i (|x_i - y_i|)
    return max(map(abs, map(operator.sub, positions[0], positions[1])))


origin = (0,0)
knots_part_a = [origin for _ in range(2)]
knots_part_b = [origin for _ in range(10)]
t_set = {origin}

print(knots_part_a)
print(knots_part_b)

def move_one_step(positions: list[tuple[int, int]], dir: str) -> list[tuple[int, int]]:
    old_head = positions[0]
    match dir:
        case 'U':
            positions[0] = (positions[0][0], positions[0][1] + 1)
        case 'D':
            positions[0] = (positions[0][0], positions[0][1] - 1)
        case 'L':
            positions[0] = (positions[0][0] - 1, positions[0][1])
        case 'R':
            positions[0] = (positions[0][0] + 1, positions[0][1])
    # print(chebyshev(positions))
    if chebyshev(positions) > 1:
        positions[1] = old_head
    return positions

def do_the_moves(rope: list[tuple[int, int]]) -> set:

    for motion in motions:
        for _ in range(motion[1]):
            rope = move_one_step(rope, motion[0]) #HERE
            t_set.add(rope[-1])
            # print(motion[0], current_pos)
    return t_set


print(len(do_the_moves(knots_part_a)))

if dataset in 'input':
    puzzle.answer_a = len(t_set)