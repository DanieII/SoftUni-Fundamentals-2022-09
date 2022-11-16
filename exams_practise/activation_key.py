def contains_func(my_string, sub):
    if sub in my_string:
        return f"{my_string} contains {sub}"
    return "Substring not found!"


def flip_func(my_string, my_case, start, end):
    if my_case == "Lower":
        string_to_change = my_string[start:end]
        new_string = string_to_change.lower()
    else:
        string_to_change = my_string[start:end]
        new_string = string_to_change.upper()
    final_string = my_string[:start] + new_string + my_string[end:]
    return final_string


def slice_func(my_string, start, end):
    left_side = my_string[:start]
    right_side = my_string[end:]
    my_string = left_side + right_side
    return my_string


key = input()
while True:
    command = input()
    if command == "Generate":
        break

    split = command.split(">>>")
    action = split[0]

    if action == "Contains":
        substring = split[1]
        print(contains_func(key, substring))
    elif action == "Flip":
        case = split[1]
        start_index = int(split[2])
        end_index = int(split[3])
        key = flip_func(key, case, start_index, end_index)
        print(key)
    elif action == "Slice":
        start_index = int(split[1])
        end_index = int(split[2])
        key = slice_func(key, start_index, end_index)
        print(key)
print(f"Your activation key is: {key}")
