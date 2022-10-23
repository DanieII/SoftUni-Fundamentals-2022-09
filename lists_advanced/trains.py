number_of_wagons = int(input())
wagons = [0] * number_of_wagons

while True:
    command = input()
    if command == "End":
        break
    current_command = command.split()
    action = current_command[0]
    if action == "add":
        people_to_add = int(current_command[1])
        wagons[-1] += people_to_add
    elif action == "insert":
        index = int(current_command[1])
        people_to_add = int(current_command[2])
        wagons[index] += people_to_add
    elif action == "leave":
        index = int(current_command[1])
        people_to_leave = int(current_command[2])
        wagons[index] -= people_to_leave
print(wagons)
