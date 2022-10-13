def calculator(first, second, command):
    if command == "multiply":
        return first * second
    elif command == "divide":
        return first // second
    elif command == "add":
        return first + second
    elif command == "subtract":
        return first - second


operator = input()
first_number = int(input())
second_number = int(input())
print(calculator(first_number, second_number, operator))
