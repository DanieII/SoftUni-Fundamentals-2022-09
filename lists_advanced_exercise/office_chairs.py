number_of_rooms = int(input())
total_free = 0
total_needed = 0
game_on = True
for current_room in range(1, number_of_rooms + 1):
    command = input().split()
    current_number_of_chairs = len(command[0])
    current_number_of_visitors = int(command[1])
    if current_number_of_chairs >= current_number_of_visitors:
        total_free += current_number_of_chairs - current_number_of_visitors
        continue

    current_needed = current_number_of_visitors - current_number_of_chairs
    total_needed += current_number_of_visitors - current_number_of_chairs
    print(f"{current_needed} more chairs needed in room {current_room}")
    game_on = False
if game_on:
    print(f"Game On, {total_free} free chairs left")
