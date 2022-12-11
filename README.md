# AOC2022

My personal attempts at the 2022 Advent of Code <https://adventofcode.com/2022>

Each day is in a two-digit day numbered folder

The *.py file is my code

## `advent-of-code-data`

<https://pypi.org/project/advent-of-code-data/>

A slick way to download the puzzle data and submit answers

## AOC Journal

### Day 07

PurePosixPath!


- 11 Dec, lagging a lot
- `/jssbn/lfrctthp/lfrctthp/` WHHYYYY!?!?!
- Thanks to [Rainow CSV VS Code Extension](https://marketplace.visualstudio.com/items?itemName=mechatroner.rainbow-csv) for enabling a rapid exploration of the dataset, although a momentary panic that `LIKE` wasn't supported was alleviated by the existence of `like(col, str)`
- Things I re-learned
  - If you don't update the value of a loop variable, it's not helpful
  - When concatenating strings with `+` you have to `str()` integers
  - `collections.defaultdict` is awesome
  - EXPLORE YOUR DATASET
- Things I learned
  - `pathlib.PurePosixPath` can be used to keep track of directories even if there's no actual file system!

### Day 06

Counter!

- 08 Dec, still lagging
- Things I re-learned
  - Can't chain `list.append()` with `list.pop()` because they both return `None`
- Things I learned
  - `Counter.most_common()`

### Day 05

Transposed Lists!

- 07 Dec, still lagging
- Things I re-learned
  - inplace list operations
- Things I learned
  - `itertools.groupby()`

### Day 04

Sorted Lists! Mapped Tuples!

- 06 Dec, still lagging
- Got `aocd` working on Ubuntu
- Things I re-learned
  - `sorted()` for lists
  - `list.count()`
- Things I learned
  - `(tuple(map(operator.sub,tups[0],tups[1])))` subtracts corresponding elements in a pair of tuples! 

### Day 03

Sets!

- 05 Dec, still lagging
- Didn't get around to debugging `aocd`
- Things I re-learned
  - `set.intersection()`
  - `string.isupper()`
- Things I learned
  - `reduce(lambda x,y: set(x)&set(y), list_of_strings)`

### Day 02

Dictionaries!

- Doubling up, 04 Dec
- Things I re-learned
  - `advent-of-code-data` is a thing!
  - Must get your AOC session token
- `urllib3.exceptions.SSLError: Can't connect to HTTPS URL because the SSL module is not available`

### Day 01

Lists!

- Started late, 04 Dec
- Things I re-learned
  - `from pathlib import Path`
  - `p = Path(__file__).with_name(n)`
  - `with p.open() as f: txt = f.read().splitlines()`
  - To add items to a list, `list.append()` for a non-iterable, `list.extend()` for items in an iterable
- Things I learned
  - You can use `None` in a variable when setting a stop slice index!
