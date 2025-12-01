from input import day1

example = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82"""

# part 1
dial_start = 50
dial_size = 100

zero_hits = 0

def wrap_around(dial_start, move):
    dial_temp = dial_start + move
    if dial_temp > dial_size:
        dial_temp = dial_temp - dial_size
    elif dial_temp < 0:
        dial_temp = dial_size + dial_temp
    return dial_temp

def check_instruction(instruction, dial_start):
    number_val = instruction[1:]
    if len(number_val) > 2:
        number_val = number_val[-2:]
    if instruction[0] == "L":
        move = -int(number_val)
    elif instruction[0] == "R":
        move = int(number_val)

    new_dial = wrap_around(dial_start, move)
    return new_dial

for line in day1.splitlines():
    dial_start = check_instruction(line, dial_start)
    if dial_start == 100 or dial_start == 0:
        zero_hits += 1

print(zero_hits)
# end part 1


# part 2
def check_instruction_p2(instruction, dial_start):
    full_rotations, number_val = divmod(int(instruction[1:]), 100)
    if instruction[0] == "L":
        move = -int(number_val)
        if 0 in range(dial_start + move, dial_start + 1) and dial_start != 0:
            full_rotations += 1
    elif instruction[0] == "R":
        move = int(number_val)
        if 100 in range(dial_start, dial_start + move + 1) and dial_start != 100:
            full_rotations += 1
    new_dial = wrap_around(dial_start, move)
    return new_dial, full_rotations

rotations = 0
for line in day1.splitlines():
    dial_start, new_rotations = check_instruction_p2(line, dial_start)
    rotations += new_rotations

print(rotations)


