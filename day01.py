"""Day 01 puzzle solutions"""

import sys
import day01_lib

with open(sys.argv[1], 'r') as inputFile:
    INSTRUCTIONS = inputFile.read()

FLOOR, POSITION = day01_lib.walk_through_floors(INSTRUCTIONS)
print("Day01 --- Part One --- result is: {0}".format(FLOOR))
print("Day01 --- Part Two --- result is: {0}".format(POSITION))
