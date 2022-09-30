command = input()
successful_sorting = True
while command != "Welcome!":
    current_name = command
    if current_name == "Voldemort":
        print("You must not speak of that name!")
        successful_sorting = False
        break
    current_len = len(current_name)
    if current_len < 5:
        print(f"{current_name} goes to Gryffindor.")
    elif current_len == 5:
        print(f"{current_name} goes to Slytherin.")
    elif current_len == 6:
        print(f"{current_name} goes to Ravenclaw.")
    elif current_len > 6:
        print(f"{current_name} goes to Hufflepuff.")
    command = input()
if successful_sorting:
    print("Welcome to Hogwarts.")