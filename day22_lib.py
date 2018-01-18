"""Day 22 puzzle solutions"""

def get_min_mana_to_win(player_hp, player_mana, boss_hp, boss_damage, lose_hp):
    """
    get_min_mana_to_win returns
    """
    combat_states = [{
        'player_hp': player_hp,
        'player_mana': player_mana,
        'mana_spent': 0,
        'player_armor': 0,
        'boss_hp': boss_hp,
        'boss_damage': boss_damage,
        'shield_timer': 0,
        'poison_timer': 0,
        'recharge_timer': 0
    }]

    mana_spent = {}
    while len(mana_spent.keys()) < 10:
        new_combat_states = []
        for state in combat_states:
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

                # The player is dead
                new_state['player_hp'] = new_state['player_hp'] - lose_hp
                if new_state['player_hp'] <= 0:
                    continue

                # Handle the effects during the player's turn
                new_state = handle_effects(new_state)

                # The boss is dead
                if new_state['boss_hp'] <= 0:
                    mana_spent[new_state['mana_spent']] = True
                    continue

                # The player loses because he does not have enough mana to cast a spell
                if new_state['player_mana'] <= 53:
                    break

                # The player casts a spell
                # Magic Missile
                if i == 0:
                    cast_spell('magic_missile', new_state, 53, 0, 4, 0)
                # Drain
                elif i == 1:
                    cast_spell('drain', new_state, 73, 2, 2, 0)
                # Shield
                elif i == 2 and new_state['shield_timer'] <= 0:
                    cast_spell('shield', new_state, 113, 0, 0, 6)
                # Poison
                elif i == 3 and new_state['poison_timer'] <= 0:
                    cast_spell('poison', new_state, 173, 0, 0, 6)
                # Recharge
                elif i == 4 and new_state['recharge_timer'] <= 0:
                    cast_spell('recharge', new_state, 229, 0, 0, 5)
                # Can cast a spell but not the current one
                else:
                    continue

                # Handle the effects during the boss's turn
                new_state = handle_effects(new_state)

                # The boss is dead
                if new_state['boss_hp'] <= 0:
                    mana_spent[new_state['mana_spent']] = True
                    # print 'Boss dead during his turn'
                    # print new_state['mana_spent']
                    continue

                # Boss does the damage
                boss_damage = new_state['boss_damage'] - new_state['player_armor']
                new_state['player_hp'] = new_state['player_hp'] - boss_damage

                # The player is dead
                if new_state['player_hp'] <= 0:
                    continue

                new_combat_states.append(new_state)
        combat_states = new_combat_states
    return min(mana_spent.keys())

def handle_effects(state_combat):
    """
    handle_effects returns
    """
    # Handle the effects during the player's turn
    if state_combat['shield_timer'] > 0:
        state_combat['shield_timer'] = state_combat['shield_timer'] - 1
        state_combat['player_armor'] = 7
    else:
        state_combat['player_armor'] = 0

    if state_combat['poison_timer'] > 0:
        state_combat['poison_timer'] = state_combat['poison_timer'] - 1
        state_combat['boss_hp'] = state_combat['boss_hp'] - 3

    if state_combat['recharge_timer'] > 0:
        state_combat['recharge_timer'] = state_combat['recharge_timer'] - 1
        state_combat['player_mana'] += 101
    return state_combat

def cast_spell(spell_name, combat_state, mana_cost, healing_hp, damage_hp, timer):
    """
    cast_spell returns the combat state updated with the effect of the casted spell
    """
    success = False
    if combat_state['player_mana'] >= mana_cost:
        combat_state['player_mana'] = combat_state['player_mana'] - mana_cost
        combat_state['mana_spent'] = combat_state['mana_spent'] + mana_cost
        combat_state['player_hp'] = combat_state['player_hp'] + healing_hp
        combat_state['boss_hp'] = combat_state['boss_hp'] - damage_hp
        if timer > 0:
            combat_state[spell_name + '_timer'] = timer
        success = True
    return success, combat_state
