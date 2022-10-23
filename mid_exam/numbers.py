numbers = list(map(int, input().split()))

while True:
    command = input()
    if command == "Finish":
        break
    commands = command.split()
    action = commands[0]
    number = int(commands[1])

    if action == "Add":
        numbers.append(number)
    elif action == "Remove":
        numbers.remove(number)
    elif action == "Replace":
        old = number
        new = int(commands[2])
        if old in numbers:
            index = numbers.index(old)
            numbers[index] = new
    elif action == "Collapse":
        for i in range(len(numbers) - 1, -1, -1):
            if numbers[i] < number:
                numbers.remove(numbers[i])

as_string = [str(x) for x in numbers]
print(" ".join(as_string))
