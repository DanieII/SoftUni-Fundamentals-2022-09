def same_hats_func(dict, color, name):
    if color not in dict:
        dict[color] = 1
    else:
        dict[color] += 1
    return dict


dwarfs = {}
same_hats = {}
while True:
    command = input()
    if command == "Once upon a time":
        break

    dwarf_name, dwarf_color, dwarf_physics_as_str = command.split(" <:> ")
    dwarf_physics = int(dwarf_physics_as_str)
    current_name = f"{dwarf_name}:{dwarf_color}"
    if current_name not in dwarfs:
        dwarfs[current_name] = [dwarf_color, dwarf_physics]
        # Same hats
        same_hats = same_hats_func(same_hats, dwarf_color, dwarf_name)
    else:
        if dwarf_physics > dwarfs[current_name][1]:
            dwarfs[current_name][1] = dwarf_physics
# x[1][1] is the physics and x[1][0] is the color
sorted_dwrafs = dict(sorted(dwarfs.items(), key=lambda x: (x[1][1], same_hats[x[1][0]]), reverse=True))
for key, value in sorted_dwrafs.items():
    name, color = key.split(":")
    print(f"({color}) {name} <-> {value[1]}")
