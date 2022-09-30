command = input()

while command != "End":
    current_string = command
    if current_string == "SoftUni":
        command = input()
        continue
    else:
        for i in current_string:
            print(i*2, end="")
    print("")
    command = input()
