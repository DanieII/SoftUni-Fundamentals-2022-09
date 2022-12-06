def enroll_hero(name):
    if name in heroes:
        print(f"{hero_name} is already enrolled.")
    else:
        heroes[name] = []


def learn_func(name, spell):
    if name not in heroes:
        print(f"{name} doesn't exist.")
    else:
        if spell in heroes[name]:
            print(f"{name} has already learnt {spell}.")
        else:
            heroes[name].append(spell)


def unlearn_func(name, spell):
    if name not in heroes:
        print(f"{name} doesn't exist.")
    else:
        if spell not in heroes[name]:
            print(f"{name} doesn't know {spell}.")
        else:
            heroes[name].remove(spell)


heroes = {}
while True:
    command = input()
    if command == "End":
        break

    split = command.split()
    action = split[0]
    if action == "Enroll":
        hero_name = split[1]
        enroll_hero(hero_name)
    elif action == "Learn":
        current_name = split[1]
        spell_name = split[2]
        learn_func(current_name, spell_name)
    elif action == "Unlearn":
        current_name = split[1]
        spell_name = split[2]
        unlearn_func(current_name, spell_name)
print("Heroes:")
for k, v in heroes.items():
    spells = ", ".join(v)
    print(f"== {k}: {spells}")
