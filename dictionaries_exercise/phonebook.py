my_dict = {}
while True:
    command = input().split("-")
    if len(command) < 2:
        iterations = int(command[0])
        break

    user, number = command
    my_dict[user] = number

for _ in range(iterations):
    current_search = input()
    if current_search in my_dict:
        number = my_dict[current_search]
        print(f"{current_search} -> {number}")
        continue
    print(f"Contact {current_search} does not exist.")
