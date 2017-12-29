"""Day 01 puzzle solutions"""

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