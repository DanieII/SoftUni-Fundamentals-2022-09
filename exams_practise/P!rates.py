cities = {}
while True:
    command = input()
    if command == "Sail":
        break

    city, population_as_str, gold_as_str = command.split("||")
    population = int(population_as_str)
    gold = int(gold_as_str)

    if city not in cities:
        cities[city] = [population, gold]
    else:
        cities[city][0] += population
        cities[city][1] += gold
# After sailing
while True:
    current_command = input()
    if current_command == "End":
        break

    split = current_command.split("=>")
    action = split[0]
    town = split[1]

    if action == "Plunder":
        people_to_kill = int(split[2])
        gold_to_steal = int(split[3])
        cities[town][0] -= people_to_kill
        cities[town][1] -= gold_to_steal
        print(f"{town} plundered! {gold_to_steal} gold stolen, {people_to_kill} citizens killed.")
        # If the city is left with no more people or gold
        if cities[town][0] == 0 or cities[town][1] == 0:
            print(f"{town} has been wiped off the map!")
            del cities[town]
            continue

    elif action == "Prosper":
        gold_to_add = int(split[2])
        if gold_to_add < 0:
            print("Gold added cannot be a negative number!")
            continue
        cities[town][1] += gold_to_add
        print(f"{gold_to_add} gold added to the city treasury. {town} now has {cities[town][1]} gold.")
# Final prints
if len(cities) > 0:
    print(f"Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:")
    for k, v in cities.items():
        current_population = v[0]
        current_gold = v[1]
        print(f"{k} -> Population: {current_population} citizens, Gold: {current_gold} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
