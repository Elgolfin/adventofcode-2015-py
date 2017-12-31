"""Day 13 puzzle solutions"""

import sys
import day13_lib

with open(sys.argv[1], 'r') as inputFile:
    INPUT = inputFile.read()

PEOPLE, HAPPINESS = day13_lib.parse_input(INPUT, False)
MAX_HAPPINESS = day13_lib.get_best_seating_arrangement(PEOPLE, HAPPINESS)
print "Day13 --- Part One --- result is: {0}".format(MAX_HAPPINESS)


PEOPLE_INCL_ME, HAPPINESS_INCL_ME = day13_lib.parse_input(INPUT, True)
MAX_HAPPINESS_INCL_ME = day13_lib.get_best_seating_arrangement(PEOPLE_INCL_ME, HAPPINESS_INCL_ME)
print "Day13 --- Part Two --- result is: {0}".format(MAX_HAPPINESS_INCL_ME)
