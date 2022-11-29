def process_values(value, default_value):
    try:
        damage = int(value)
    except ValueError:
        damage = default_value
    return damage


def sort(values_of_the_types):
    new_dict = {}
    # Making a new dictionary and putting the current type as a key and the sorted value/dragons as a value
    for k, v in values_of_the_types.items():
        new_dict[k] = dict(sorted(v.items(), key=lambda x: x[0]))
    return new_dict


def find_average(values_of_the_dragons):
    length_of_dragons = len(values_of_the_dragons)
    all_damage = 0
    all_health = 0
    all_armor = 0
    for stats in values_of_the_dragons.values():
        current_damage, current_health, current_armor = stats.values()
        all_damage += current_damage
        all_health += current_health
        all_armor += current_armor
    return f"{all_damage / length_of_dragons:.2f}/{all_health / length_of_dragons:.2f}/{all_armor / length_of_dragons:.2f}"


def print_func(dict):
    for current_type, dragons in dict.items():
        average = find_average(dragons)
        print(f"{current_type}::({average})")
        for name, stats in dict[current_type].items():
            damage = stats["DAMAGE"]
            health = stats["HEALTH"]
            armor = stats["ARMOR"]
            print(f"-{name} -> damage: {damage}, health: {health}, armor: {armor}")


def add_dragons(dragons, number):
    for _ in range(number):
        type, name, damage_as_str, health_as_str, armor_as_str = input().split()
        damage, health, armor = process_values(damage_as_str, 45), process_values(health_as_str, 250), process_values(
            armor_as_str, 10)
        if type not in dragons:
            dragons[type] = {name: {"DAMAGE": damage, "HEALTH": health, "ARMOR": armor}}
        else:
            dragons[type][name] = {"DAMAGE": damage, "HEALTH": health, "ARMOR": armor}


number_of_dragons = int(input())


# Main Function
def dragon_army(number):
    dragons = {}
    add_dragons(dragons, number)
    dragons = sort(dragons)
    print_func(dragons)


dragon_army(number_of_dragons)
