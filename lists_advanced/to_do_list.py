lst = []
while True:
    command = input()
    if command == "End":
        break
    current_command = command.split("-")
    priority = current_command[0]
    task = current_command[1]
    lst.append([priority, task])
final_lst = [x[1] for x in sorted(lst)]
print(final_lst)
