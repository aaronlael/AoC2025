from input import day5


example = """3-5
10-14
16-20
12-18

1
5
8
11
17
32"""


def formatter(inp):
    puzzle_data = {}
    fresh, ingredients = inp.split("\n\n")
    puzzle_data['fresh'] = sorted([range(int(x.split("-")[0]),int(x.split("-")[1]) +1) for x in fresh.splitlines()],key=lambda item: item[0])
    puzzle_data['ingredients'] = [int(x) for x in ingredients.splitlines()]
    return puzzle_data

puzzle_data = formatter(day5)

# part 1

fresh_count = 0

for ingredient in puzzle_data['ingredients']:
    for r in puzzle_data['fresh']:
        if ingredient in r:
            fresh_count += 1
            break

print(fresh_count)

# part 2


def merge_ranges(range_objects):
    range_tuples = [(r.start, r.stop) for r in range_objects]
    merged = []
    current_start, current_stop = range_tuples[0]
    for next_start, next_stop in range_tuples[1:]:
        if next_start <= current_stop:
            current_stop = max(current_stop, next_stop)
        else:
            merged.append((current_start, current_stop))
            current_start, current_stop = next_start, next_stop

    merged.append((current_start, current_stop))
    return merged

total_unique = 0
for m_r in merge_ranges(puzzle_data['fresh']):
    total_unique += len(range(m_r[0], m_r[1]))

print(total_unique)


