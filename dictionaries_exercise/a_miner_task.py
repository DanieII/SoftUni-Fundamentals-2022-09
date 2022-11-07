my_dict = {}
while True:
    command = input()
    if command == "stop":
        break
    resource = command
    quantity = int(input())
    if resource not in my_dict:
        my_dict[resource] = 0
    my_dict[resource] += quantity

print("\n".join(f"{key} -> {value}" for key, value in my_dict.items()))
