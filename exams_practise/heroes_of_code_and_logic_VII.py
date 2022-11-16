def cast_spell(name, needed, spell):
    global mp
    global dict_with_heroes
    if mp >= needed:
        mp -= needed
        dict_with_heroes[name][1] -= needed
        return f"{name} has successfully cast {spell} and now has {mp} MP!"
    else:
        return f"{name} does not have enough MP to cast {spell}!"


def take_damage(name, my_damage, my_attacker):
    global hp
    global dict_with_heroes
    if hp - my_damage > 0:
        hp -= my_damage
        dict_with_heroes[name][0] -= my_damage
        return f"{name} was hit for {my_damage} HP by {my_attacker} and now has {hp} HP left!"
    else:
        del dict_with_heroes[name]
        return f"{name} has been killed by {my_attacker}!"


def recharge_func(name, amount_to_add):
    global mp
    global dict_with_heroes
    if mp + amount_to_add > 200:
        recovered = 200 - mp
        mp = 200
        dict_with_heroes[name][1] = 200
    else:
        recovered = amount_to_add
        mp += amount_to_add
        dict_with_heroes[name][1] += amount_to_add
    return f"{name} recharged for {recovered} MP!"


def heal_func(name, amount):
    global hp
    global dict_with_heroes
    if hp + amount > 100:
        healed = 100 - hp
        hp = 100
        dict_with_heroes[name][0] = 100
    else:
        healed = amount
        hp += amount
        dict_with_heroes[name][0] += amount
    return f"{name} healed for {healed} HP!"


number_of_iterations = int(input())
dict_with_heroes = {}
for _ in range(number_of_iterations):
    name, hp, mp = input().split()
    dict_with_heroes[name] = [int(hp), int(mp)]

while True:
    command = input()
    if command == "End":
        break

    split = command.split(" - ")
    action = split[0]
    hero_name = split[1]
    hp = int(dict_with_heroes[hero_name][0])
    mp = int(dict_with_heroes[hero_name][1])
    if action == "CastSpell":
        mana_needed = int(split[2])
        spell_name = split[3]
        print(cast_spell(hero_name, mana_needed, spell_name))
    elif action == "TakeDamage":
        damage = int(split[2])
        attacker = split[3]
        print(take_damage(hero_name, damage, attacker))
    elif action == "Recharge":
        amount = int(split[2])
        print(recharge_func(hero_name, amount))
    elif action == "Heal":
        amount_to_heal = int(split[2])
        print(heal_func(hero_name, amount_to_heal))

for k, v in dict_with_heroes.items():
    print(k)
    print(f"HP: {v[0]}")
    print(f"MP: {v[1]}")
