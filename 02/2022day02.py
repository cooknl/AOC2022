# from aocd.models import Puzzle
# puzzle = Puzzle(year=2022, day=2)
from pathlib import Path

n = '2022day02input.txt'  #'2022day02toy.txt'

# own play is second in tuple
rules = { ('Rock','Rock'): 'Tie',
          ('Rock', 'Paper'): 'Win',
          ('Rock', 'Scissors'): 'Loss',
          ('Paper', 'Paper'): 'Tie',
          ('Paper', 'Scissors'): 'Win',
          ('Paper', 'Rock'): 'Loss',
          ('Scissors', 'Scissors'): 'Tie',
          ('Scissors', 'Rock'): 'Win',
          ('Scissors', 'Paper'): 'Loss', }

inv_rules = {('Rock','Draw'): 'Rock',
             ('Rock', 'Win'): 'Paper',
             ('Rock', 'Lose'): 'Scissors',
             ('Paper', 'Draw'): 'Paper',
             ('Paper', 'Win'): 'Scissors',
             ('Paper', 'Lose'): 'Rock',
             ('Scissors', 'Draw'): 'Scissors',
             ('Scissors', 'Win'): 'Rock',
             ('Scissors', 'Lose'): 'Paper', }

scores = {'shape': {'Rock': 1, 
                   'Paper': 2, 
                   'Scissors': 3},
         'round': {'Loss': 0, 
                   'Tie': 3, 
                   'Win': 6}}

decoder_part1 = {'A': 'Rock',
           'B': 'Paper',
           'C': 'Scissors',
           'X': 'Rock',
           'Y': 'Paper',
           'Z': 'Scissors'}

decoder_part2 = {'A': 'Rock',
           'B': 'Paper',
           'C': 'Scissors',
           'X': 'Lose',
           'Y': 'Draw',
           'Z': 'Win'}

turn = {'second': 1,
        'first': -1}

my_turn = turn['second'] # I go second



# Part 1
def prep_text(fname, part):
    p = Path(__file__).with_name(fname)
    with p.open() as f:
        txt = f.read()
    if part == 1:
        for old, new in decoder_part1.items():
            txt = txt.replace(old, new)
        rounds = [tuple(l.split()[::my_turn]) for l in txt.splitlines()]
    elif part == 2:
        for old, new in decoder_part2.items():
            txt = txt.replace(old, new)
        rounds = [ (tuple(l.split()[::my_turn])[0], inv_rules[tuple(l.split()[::my_turn])]) for l in txt.splitlines() ]
    return rounds

def calc_total_score(rounds):
    return (sum( # add all
                [ scores['shape'][r[1]] # the score due to the shape 
                + scores['round'][rules[r]] for r in rounds]))

print("Part 1: ", calc_total_score(prep_text(n, 1)))

# Part 2

print("Part 2: ", calc_total_score(prep_text(n, 2)))