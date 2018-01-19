"""Day 09 puzzle solutions"""

import sys
import day09_lib

with open(sys.argv[1], 'r') as inputFile:
    INPUT = inputFile.read()

CITIES, DISTANCES = day09_lib.parse_input(INPUT)
SHORTEST_DIST, LONGEST_DIST = day09_lib.get_distances(CITIES, DISTANCES)

print("Day09 --- Part One --- result is: {0}".format(SHORTEST_DIST))
print("Day09 --- Part Two --- result is: {0}".format(LONGEST_DIST))
