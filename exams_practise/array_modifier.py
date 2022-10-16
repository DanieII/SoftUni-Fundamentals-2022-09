lst = input().split()
lst_of_numbers = [int(x) for x in lst]
command = input()
while command != "end":
    current_command = command.split()
    action = current_command[0]
    if action == "decrease":
        current_index = 0
        for current_number in lst_of_numbers:
            current_number -= 1
            lst_of_numbers[current_index] = current_number
            current_index += 1
        command = input()
        continue
    index_1 = int(current_command[1])
    index_2 = int(current_command[2])
    if action == "swap":
        lst_of_numbers[index_1], lst_of_numbers[index_2] = lst_of_numbers[index_2], lst_of_numbers[index_1]
    elif action == "multiply":
        result = lst_of_numbers[index_1] * lst_of_numbers[index_2]
        lst_of_numbers[index_1] = result
    command = input()
print(", ".join([str(x) for x in lst_of_numbers]))
