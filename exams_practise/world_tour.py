def add(my_stops, my_index, my_string):
    if my_index in range(len(my_stops)):
        return all_stops[:index] + my_string + all_stops[index:]
    return my_stops


def remove(my_stops, my_start, my_end):
    if my_start in range(len(my_stops)) and end in range(len(my_stops)):
        return my_stops[:my_start] + my_stops[my_end + 1:]
    return my_stops


def switch(my_stops, my_old, my_new):
    if my_old in my_stops:
        return my_stops.replace(my_old, my_new)
    return my_stops


all_stops = input()
while True:
    command = input()

    if command == "Travel":
        break

    splitted = command.split(":")
    action = splitted[0]

    if action == "Add Stop":
        index = int(splitted[1])
        string = splitted[2]
        all_stops = add(all_stops, index, string)

    elif action == "Remove Stop":
        start = int(splitted[1])
        end = int(splitted[2])
        all_stops = remove(all_stops, start, end)

    elif action == "Switch":
        old = splitted[1]
        new = splitted[2]
        all_stops = switch(all_stops, old, new)

    print(all_stops)

print(f"Ready for world tour! Planned stops: {all_stops}")
