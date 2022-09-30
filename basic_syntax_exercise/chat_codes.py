iterations = int(input())

for i in range(iterations):
    current_input = int(input())
    if current_input == 88:
        print("Hello")
    elif current_input == 86:
        print("How are you?")
    elif current_input != 88 and current_input != 86 and current_input < 88:
        print("GREAT!")
    elif current_input > 88:
        print("Bye.")
