full_string = input()
for index in range(len(full_string)):
    if full_string[index] == ":":
        second_part = full_string[index + 1]
        print(f":{second_part}")
