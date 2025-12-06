from input import day3

example = """987654321111111
811111111111119
234234234234278
818181911112111"""


# part 1

joltage = 0

for row in day3.splitlines():
    int_row = [int(x) for x in list(row)]
    max_val = max(int_row[:-1])
    max_val_location = int_row.index(max_val)
    sub_max_val = max(int_row[max_val_location +1:])
    joltage += max_val * 10 + sub_max_val

print(joltage)

# part 2
joltage_12 = 0

for row in day3.splitlines():
    bank_joltage = ""
    last_idx = 0
    int_row = [int(x) for x in list(row)]
    for i in range(12,0, -1):
        i -=1
        if i <= 0:
            i = -len(int_row)
        max_temp = max(int_row[last_idx:-(i)])
        last_idx += int_row[last_idx:-(i)].index(max_temp) + 1
        bank_joltage += str(max_temp)
    joltage_12 += int(bank_joltage)


print(joltage_12)
        
