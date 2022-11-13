initial_lst = input().split("!")
command = input()
while command != "Go Shopping!":
    current_command = command.split()
    action = current_command[0]
    if action == "Urgent":
        item = current_command[1]
        if item not in initial_lst:
            initial_lst.insert(0, item)
    elif action == "Unnecessary":
        item = current_command[1]
        if item in initial_lst:
            initial_lst.remove(item)
    elif action == "Correct":
        old_item = current_command[1]
        new_item = current_command[2]
        if old_item in initial_lst:
            old_item_index = initial_lst.index(old_item)
            initial_lst[old_item_index] = new_item
    elif action == "Rearrange":
        item = current_command[1]
        if item in initial_lst:
            item_index = initial_lst.index(item)
            item_to_add = initial_lst.pop(item_index)
            initial_lst.append(item_to_add)
    command = input()
print(", ".join(initial_lst))
