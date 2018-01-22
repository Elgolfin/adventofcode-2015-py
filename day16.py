"""Day 16 puzzle solutions"""

import sys
import day16_lib

with open(sys.argv[1], 'r') as inputFile:
    AUNTS = inputFile.read()

TICKER_TAPE = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1
}

print("Day16 --- Part One --- result is: {}".format(day16_lib.find_aunt(TICKER_TAPE, AUNTS, False)))
print("Day16 --- Part Two --- result is: {}".format(day16_lib.find_aunt(TICKER_TAPE, AUNTS, True)))
