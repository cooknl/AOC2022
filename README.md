# AOC2022

My personal attempts at the 2022 Advent of Code <https://adventofcode.com/2022>

Each day is in a two-digit day numbered folder

The *.py file is my code

## `advent-of-code-data`

<https://pypi.org/project/advent-of-code-data/>

A slick way to download the puzzle data and submit answers

## AOC Journal

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
