message = input().split()
receiving_command = input()

while receiving_command != "3:1":
    command_list = receiving_command.split()
    command = command_list[0]
    starting_index = int(command_list[1])
    end_index = int(command_list[2])

    if command == "merge":
        # Putting the indexes in the range in case they are out of it
        if starting_index < 0:
            starting_index = 0
        if end_index > len(message) - 1:
            end_index = len(message) -1
        # Getting the number of indices we have to get rid of
        diff_indices = end_index - starting_index
        if end_index == len(message):
            diff_indices -= 1
        new_message = message[starting_index:end_index + 1]
        message_to_add = "".join(new_message)
        for _ in range(diff_indices + 1):
            if len(message) > 0:
                message.pop(starting_index)
            else:
                continue
        message.insert(starting_index, message_to_add)
        receiving_command = input()
    elif command == "divide":
        new_message = message[starting_index]
        message.pop(starting_index)
        words_to_add = len(new_message) // end_index
        remainder = len(new_message) % end_index
        substrings_added = 0
        start_part = 0
        end_part = words_to_add
        while substrings_added < end_index:
            message.insert(starting_index, new_message[start_part:end_part])
            starting_index += 1
            substrings_added += 1
            if substrings_added + 1 == end_index:
                start_part += words_to_add
                end_part += words_to_add + remainder
            else:
                start_part += words_to_add
                end_part += words_to_add
        receiving_command = input()
print(" ".join(message))
