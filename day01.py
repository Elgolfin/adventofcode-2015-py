"""Day 01 puzzle solutions"""

with open('inputs/day01.txt', 'r') as inputFile:
    INSTRUCTIONS = inputFile.read()

def walk_through_floors(instructions):
    """Returns the final floor and the position that causes to first enter the basement"""
    floor = 0
    position = 0
    enter_basement_at = 0
    for instruction in instructions:
        position += 1
        if instruction == '(':
            floor += 1
        else:
            floor -= 1
        if floor == -1 and enter_basement_at == 0:
            enter_basement_at = position
    return floor, enter_basement_at

FLOOR, POSITION = walk_through_floors(INSTRUCTIONS)
print "Day01 --- Part One --- result is: {0}".format(FLOOR)
print "Day01 --- Part Two --- result is: {0}".format(POSITION)
