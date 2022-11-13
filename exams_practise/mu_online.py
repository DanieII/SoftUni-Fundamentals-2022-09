all_rooms = input().split("|")
health = 100
bitcoins = 0
best_room = 0

for room in all_rooms:
    best_room += 1
    current_room = room.split()
    command = current_room[0]
    number = int(current_room[1])
    if command == "potion":
        if health + number >= 100:
            healed = 100 - health
            health = 100
        else:
            health += number
            healed = number
        print(f"You healed for {healed} hp.")
        print(f"Current health: {health} hp.")

    elif command == "chest":
        bitcoins += number
        print(f"You found {number} bitcoins.")

    else:
        monster = command
        if health - number <= 0:
            print(f"You died! Killed by {monster}.")
            print(f"Best room: {best_room}")
            break
        else:
            health -= number
            print(f"You slayed {monster}.")

else:
    print(f"""You've made it!
Bitcoins: {bitcoins}
Health: {health}
""")
