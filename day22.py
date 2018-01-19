"""Day 22 puzzle solutions"""

import sys
import day22_lib

PLAYER_HP = int(sys.argv[1])
PLAYER_MANA = int(sys.argv[2])

BOSS_HP = int(sys.argv[3])
BOSS_DAMAGE = int(sys.argv[4])

PART_1 = day22_lib.get_min_mana_to_win(PLAYER_HP, PLAYER_MANA, BOSS_HP, BOSS_DAMAGE, 0)
PART_2 = day22_lib.get_min_mana_to_win(PLAYER_HP, PLAYER_MANA, BOSS_HP, BOSS_DAMAGE, 1)
print("Day22 --- Part One --- result is: {0}".format(PART_1))
print("Day22 --- Part Two --- result is: {0}".format(PART_2))
