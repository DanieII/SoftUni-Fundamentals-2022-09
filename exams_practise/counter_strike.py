energy = int(input())
won_battles = 0
command = input()

while command != "End of battle":
    current_energy = int(command)
    won_battles += 1
    energy -= current_energy

    if won_battles % 3 == 0:
        energy += won_battles

    if energy <= 0:
        energy = 0
        print(f"Not enough energy! Game ends with {won_battles} won battles and {energy} energy")
        break
    command = input()

else:
    print(f"Won battles: {won_battles}. Energy left: {energy}")
