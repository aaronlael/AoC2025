from input import day2
import re

example = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"""


# part 1
invalid_total = 0

for id_range in day2.split(","):
    start, end = id_range.split("-")
    for i in range(int(start), int(end) + 1):
        str_i = str(i)
        if not (len(str_i) % 2):
            if str_i[:int(len(str_i)/2)] == str_i[int(len(str_i)/2):]:
                invalid_total += i

print(invalid_total)

# part 2
invalid_total_part2 = 0

for id_range in day2.split(","):
    start, end = id_range.split("-")
    for i in range(int(start), int(end) + 1):
        pattern = re.compile(r"^(\d+)\1+$")
        if re.search(pattern, str(i)):
            invalid_total_part2 += i

print(invalid_total_part2)