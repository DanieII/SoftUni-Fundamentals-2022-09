my_dict = {}
while True:
    command = input()
    if command == "Lumpawaroo":
        break

    if "|" in command:
        side, user = command.split(" | ")
        already_on_a_side = False
        for lst in my_dict.values():
            if user in lst:
                already_on_a_side = True
                break
        if not already_on_a_side:
            if side not in my_dict:
                my_dict[side] = [user]
            else:
                my_dict[side].append(user)

    elif "->" in command:
        user, side = command.split(" -> ")
        found = False
        for current_side, lst in my_dict.items():
            if user in lst:
                found = True
                removed = my_dict[current_side].pop(lst.index(user))
                break

        if side not in my_dict:
            my_dict[side] = [user]

        else:
            my_dict[side].append(user)
        print(f"{user} joins the {side} side!")
for key, value in my_dict.items():
    if len(value) > 0:
        print(f"Side: {key}, Members: {len(value)}")
        print("\n".join([f"! {x}" for x in value]))
