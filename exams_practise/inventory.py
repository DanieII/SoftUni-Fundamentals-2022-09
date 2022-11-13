items = input().split(", ")
command = input().split(" - ")

while True:
    if len(command) < 2:
        print(", ".join(items))
        break
    action = command[0]
    item = command[1]
    if action == "Collect":
        if item in items:
            continue
        items.append(item)

    elif action == "Drop":
        if item in items:
            items.remove(item)

    elif action == "Combine Items":
        old_and_new = item.split(":")
        old = old_and_new[0]
        new = old_and_new[1]
        if old in items:
            index = items.index(old) + 1
            items.insert(index, new)

    elif action == "Renew":
        if item in items:
            items.remove(item)
            items.append(item)
    command = input().split(" - ")
