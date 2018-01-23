"""Day 17 puzzle solutions"""

import sys
import day17_lib

with open(sys.argv[1], 'r') as inputFile:
    CONTAINERS = day17_lib.parse_input(inputFile.read())

RES_PART_1 = day17_lib.get_exact_combinations(150, CONTAINERS)
RES_PART_2 = day17_lib.get_exact_combinations(150, CONTAINERS, True)
print("Day17 --- Part One --- result is: {}".format(RES_PART_1))
print("Day17 --- Part Two --- result is: {}".format(RES_PART_2))
