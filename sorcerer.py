def sorcerer(level=None):  # optional argument with a default value
    if level is None:
        level = get_valid_integer("Enter level: ")

    calculated_mana, calculated_hp = get_calculated_hp_and_mana(level)

    print(f'You are at level: {level} with mana: {calculated_mana} and hp: {calculated_hp}.')

    return calculated_mana, calculated_hp


def get_calculated_hp_and_mana(level, base_hp=185, base_mana=35, hp_per_level=5, mana_per_level=30, min_level=8):
    if level < min_level:
        print(f'You need to be at least level {min_level}')
        return None, None

    calculated_hp = base_hp + hp_per_level * (level - min_level)
    calculated_mana = base_mana + mana_per_level * (level - min_level)

    return calculated_mana, calculated_hp


def get_valid_integer(prompt):
    input_string = input(prompt)
    try:
        valid_int = int(input_string)
    except ValueError:
        print(f'You entered {input_string}, which is not a valid integer.')
        return get_valid_integer(prompt)

    return valid_int
