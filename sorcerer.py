def sorcerer(level=None):  # optional argument with a default value
    if level is None:
        level_string = input("Enter level: ")
        try:
            level = int(level_string)
        except ValueError:
            print(f'You entered {level_string}, which is not a valid integer.')
            return sorcerer()

    if level < 8:
        print('You need to be at least level 8')
        return None, None

    hp = 185
    mana = 35
    hp_per_level = 5
    mana_per_level = 30

    calculated_hp = hp + hp_per_level * (level - 8)
    calculated_mana = mana + mana_per_level * (level - 8)

    print(f'HP:{calculated_hp} and MANA:{calculated_mana} at lvl:{level}.')

    return calculated_mana, calculated_hp
