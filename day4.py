from input import day4

example = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""


look_around = {
    "up" : (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right" : (0, 1),
    "dl" : (1, -1),
    "dr" : (1, 1),
    "ul" : (-1, -1),
    "ur" : (-1, 1)
}


def formatter(inp):
    inp = inp.splitlines()
    return [list(x) for x in inp]


# part 1

puzzle_input = formatter(day4)
move_rolls = 0
for y in range(len(puzzle_input)):
    for x in range(len(puzzle_input[y])):
        if puzzle_input[y][x] == "@":
            rolls_near = 0
            for k in look_around:
                new_y = y + look_around[k][0]
                new_x = x + look_around[k][1]
                if new_y >= 0 and new_y < len(puzzle_input) and new_x >= 0 and new_x < len(puzzle_input[0]):
                    if puzzle_input[y + look_around[k][0]][x + look_around[k][1]] == "@":
                        rolls_near += 1
                        if rolls_near >= 4:
                            break
            else:
                move_rolls += 1

print(move_rolls)

# part 2

move_many_rolls = 0

def process_input(puzzle_input):
    global move_many_rolls
    for y in range(len(puzzle_input)):
        for x in range(len(puzzle_input[y])):
            if puzzle_input[y][x] == "@":
                rolls_near = 0
                for k in look_around:
                    new_y = y + look_around[k][0]
                    new_x = x + look_around[k][1]
                    if new_y >= 0 and new_y < len(puzzle_input) and new_x >= 0 and new_x < len(puzzle_input[0]):
                        if puzzle_input[y + look_around[k][0]][x + look_around[k][1]] == "@":
                            rolls_near += 1
                            if rolls_near >= 4:
                                break
                else:
                    move_many_rolls += 1
                    puzzle_input[y][x] = "X"
    return puzzle_input


interim_returned = "start"
while interim_returned != "end":
    start_many_rolls = move_many_rolls
    puzzle_input = process_input(puzzle_input)
    if move_many_rolls - start_many_rolls == 0:
        break

print(move_many_rolls)

