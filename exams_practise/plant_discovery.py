import re


def add_plants(name, rarity):
    plants[name] = [rarity, []]


def rate_func(plant_name, plant_rarity):
    plants[plant_name][1].append(plant_rarity)


def update_func(plant_name, new_plant_rarity):
    plants[plant_name][0] = new_plant_rarity


def reset_func(plant_name):
    plants[plant_name][1].clear()


def find_average(lst):
    if len(lst) == 0:
        return 0.00
    return sum(lst) / len(lst)


number_of_plants = int(input())
plants = {}
for _ in range(number_of_plants):
    string = input().split("<->")
    plant_name = string[0]
    plant_rarity = int(string[1])
    add_plants(plant_name, plant_rarity)

while True:
    command = input()
    if command == "Exhibition":
        break

    split = re.split(r": | - ", command)
    action = split[0]
    plant = split[1]

    if action == "Rate":
        if plant not in plants:
            print("error")
        else:
            rarity = int(split[2])
            rate_func(plant, rarity)
    elif action == "Update":
        if plant not in plants:
            print("error")
        else:
            rarity = int(split[2])
            update_func(plant, rarity)
    elif action == "Reset":
        if plant not in plants:
            print("error")
        else:
            reset_func(plant)
print("Plants for the exhibition:")
for key, value in plants.items():
    current_rarity = value[0]
    current_average = find_average(value[1])
    print(f"- {key}; Rarity: {current_rarity}; Rating: {current_average:.2f}")
