level = input()
hp = 185
mana = 35
hp_per_level = 5
mana_per_level = 30

if int(level) == 8:
    print("HP and MANA at lvl 8: ")
    print(hp)
    print(mana)
elif int(level) > 8:
    print("HP and MANA at lvl " + level + ": ")
    print(hp + hp_per_level * (int(level) - 8))
    print(mana + mana_per_level * (int(level) - 8))
elif int(level) < 8:
    print('You need to be at least level 8')


