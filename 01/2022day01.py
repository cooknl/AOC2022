from pathlib import Path

n = '2022day01input.txt' #'2022day01toy.txt'
p = Path(__file__).with_name(n)

with p.open() as f:
    txt = f.read().splitlines()

idxs = [idx for idx, value in enumerate(txt) if value == '']

idxs.append(None)

start = 0
chunks = []

top_three = []

def txt_sum(sublist):
    return sum(list(map(int,sublist)))

for end in idxs:
    cals = txt_sum(txt[start:end])
    chunks.append(cals)
    if end:
        start = end + 1
    if (len(top_three) < 3):
        top_three.append(cals)
    elif (len(top_three) == 3) & (cals > min(top_three)):
        top_three.remove(min(top_three))
        top_three.append(cals)
            



most_cal = max(chunks)
most_cal_elf = chunks.index(most_cal) + 1
print("Part 1 Answer: The total Calories of the Elf carrying the most Calories is ", most_cal)
print("Part 2 Answer: Top three sum is ", top_three, " Sum is ", sum(top_three))
