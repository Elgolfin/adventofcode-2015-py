"""Day 22 puzzle solutions"""

import sys
# import day13_lib

PLAYER_HP = int(sys.argv[1])
PLAYER_DAMAGE = int(sys.argv[2])

BOSS_HP = int(sys.argv[3])
BOSS_DAMAGE = int(sys.argv[4])

LOSE_HP = int(sys.argv[5])

MY_LIST = [{
    'player_hp': PLAYER_HP,
    'player_mana': PLAYER_DAMAGE,
    'mana_spent': 0,
    'player_armor': 0,
    'boss_hp': BOSS_HP,
    'boss_damage': BOSS_DAMAGE,
    'shield_timer': 0,
    'poison_timer': 0,
    'recharge_timer': 0
    }]

MANA_SPENT = {}
while len(MANA_SPENT.keys()) < 10:
    NEW_LIST = []
    for state in MY_LIST:
        for i in range(5):
            new_state = {
                'player_hp': state['player_hp'],
                'player_mana': state['player_mana'],
                'player_armor': state['player_armor'],
                'mana_spent': state['mana_spent'],
                'boss_hp': state['boss_hp'],
                'boss_damage': state['boss_damage'],
                'shield_timer': state['shield_timer'],
                'poison_timer': state['poison_timer'],
                'recharge_timer': state['recharge_timer']
            }

            new_state['player_hp'] = new_state['player_hp'] - LOSE_HP
            if new_state['player_hp'] <= 0:
                # print 'Player lose (not enough hp)'
                continue

            # Handle the effects during the player's turn
            if new_state['shield_timer'] > 0:
                new_state['shield_timer'] = new_state['shield_timer'] - 1
                new_state['player_armor'] = 7
            else:
                new_state['player_armor'] = 0

            if new_state['poison_timer'] > 0:
                new_state['poison_timer'] = new_state['poison_timer'] - 1
                new_state['boss_hp'] = new_state['boss_hp'] - 3

            if new_state['recharge_timer'] > 0:
                new_state['recharge_timer'] = new_state['recharge_timer'] - 1
                new_state['player_mana'] += 101

            if new_state['boss_hp'] <= 0:
                MANA_SPENT[new_state['mana_spent']] = True
                # print 'Boss dead during the player\'s turn'
                # print new_state['mana_spent']
                continue

            # Cannot cast a spell, the player lose
            if new_state['player_mana'] <= 53:
                # print 'Player lose (not enough mana)'
                break

            # Cast a spell
            # Magic Missile
            if i == 0 and new_state['player_mana'] >= 53:
                new_state['player_mana'] = new_state['player_mana'] - 53
                new_state['mana_spent'] = new_state['mana_spent'] + 53
                new_state['boss_hp'] = new_state['boss_hp'] - 4
            # Drain
            elif i == 1 and new_state['player_mana'] >= 73:
                new_state['player_mana'] = new_state['player_mana'] - 73
                new_state['mana_spent'] = new_state['mana_spent'] + 73
                new_state['player_hp'] = new_state['player_hp'] + 2
                new_state['boss_hp'] = new_state['boss_hp'] - 2
            # Shield
            elif i == 2 and new_state['shield_timer'] <= 0 and new_state['player_mana'] >= 113:
                new_state['player_mana'] = new_state['player_mana'] - 113
                new_state['mana_spent'] = new_state['mana_spent'] + 113
                new_state['shield_timer'] = 6
            # Poison
            elif i == 3 and new_state['poison_timer'] <= 0 and new_state['player_mana'] >= 173:
                new_state['player_mana'] = new_state['player_mana'] - 173
                new_state['mana_spent'] = new_state['mana_spent'] + 173
                new_state['poison_timer'] = 6
            # Recharge
            elif i == 4 and new_state['recharge_timer'] <= 0 and new_state['player_mana'] >= 229:
                new_state['player_mana'] = new_state['player_mana'] - 229
                new_state['mana_spent'] = new_state['mana_spent'] + 229
                new_state['recharge_timer'] = 5
            # Can cast a spell but not the current one
            else:
                continue

            # Handle the effects during the boss's turn
            if new_state['shield_timer'] > 0:
                new_state['shield_timer'] = new_state['shield_timer'] - 1
                new_state['player_armor'] = 7
            else:
                new_state['player_armor'] = 0

            if new_state['poison_timer'] > 0:
                new_state['poison_timer'] = new_state['poison_timer'] - 1
                new_state['boss_hp'] = new_state['boss_hp'] - 3

            if new_state['recharge_timer'] > 0:
                new_state['recharge_timer'] = new_state['recharge_timer'] - 1
                new_state['player_mana'] += 101

            if new_state['boss_hp'] <= 0:
                MANA_SPENT[new_state['mana_spent']] = True
                # print 'Boss dead during his turn'
                # print new_state['mana_spent']
                continue

            # Boss does the damage
            boss_damage = new_state['boss_damage'] - new_state['player_armor']
            new_state['player_hp'] = new_state['player_hp'] - boss_damage

            if new_state['player_hp'] <= 0:
                # print 'Player lose (not enough hp)'
                continue

            NEW_LIST.append(new_state)
    MY_LIST = NEW_LIST

#print MANA_SPENT
print min(MANA_SPENT.keys())
# print "Day22 --- Part One --- result is: {0}".format(HIT_POINTS)
# print "Day22 --- Part Two --- result is: {0}".format(BOSS_DAMAGE)
