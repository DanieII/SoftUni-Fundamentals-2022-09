energy = 100
coins = 100
events = input().split("|")
bakery_is_open = True
for event_and_number in events:
    current_event = event_and_number.split("-")
    event = current_event[0]
    number = int(current_event[1])
    gained = 0
    if event == "rest":
        current_energy = energy
        energy += number
        if energy > 100:
            energy = 100
        gained = energy - current_energy
        print(f"You gained {gained} energy.")
        print(f"Current energy: {energy}.")
    elif event == "order":
        if energy - 30 >= 0:
            energy -= 30
            coins += number
            print(f"You earned {number} coins.")
        else:
            energy += 50
            print(f"You had to rest!")
    else:
        if coins >= number:
            coins -= number
            print(f"You bought {event}.")
        else:
            print(f"Closed! Cannot afford {event}.")
            bakery_is_open = False
            break
if bakery_is_open:
    print(f"""Day completed!
Coins: {coins}
Energy: {energy}""")
