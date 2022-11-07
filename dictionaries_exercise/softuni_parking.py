my_dict = {}
iterations = int(input())
for _ in range(iterations):
    command = input().split()
    action = command[0]
    if action == "register":
        name, license_plate = command[1], command[2]
        if name not in my_dict:
            my_dict[name] = license_plate
            print(f"{name} registered {license_plate} successfully")
        else:
            print(f"ERROR: already registered with plate number {license_plate}")
    elif action == "unregister":
        name = command[1]
        if name not in my_dict:
            print(f"ERROR: user {name} not found")
        else:
            del my_dict[name]
            print(f"{name} unregistered successfully")
print("\n".join([f"{username} => {license_plate_number}" for username, license_plate_number in my_dict.items()]))
