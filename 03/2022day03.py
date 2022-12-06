from pathlib import Path
from functools import reduce

n = '2022day03input.txt'  #'2022day02toy.txt'

p = Path(__file__).with_name(n)
with p.open() as f:
    txt = f.read().splitlines()

# Part 1

tups = [ ( l[:len(l)//2], l[len(l)//2:] ) for l in txt]

#print(txt)

uni = [ set(t[0]).intersection(set(t[1])).pop() for t in tups]

#print(uni)

def letter2pri(letter):
    if letter.isupper():
        offset = 38
    else:
        offset = 96
    return ord(letter) - offset

pri_sum = sum(map(letter2pri, uni))

print('Sum of priorities ', pri_sum)

# Part 2

trip = []
trips = []

for count, l in enumerate(txt):
    trip.append(l)
    if (count + 1) % 3 == 0:
        trips.append(reduce(lambda x,y: set(x)&set(y), trip).pop())
        trip = []

pri_sum = sum(map(letter2pri, trips))

print('Sum of priorities ', pri_sum)