all_houses = list(map(int, input().split("@")))
command = input().split()
house = 0
all_valentine_days = 0

while True:
    if len(command) < 2:
        break

    current_jump = int(command[1])
    house += current_jump
    # Checking if the given index is out of the houses' range
    if current_jump > len(all_houses) - 1 or house > len(all_houses) - 1:
        house = 0
    # Checking if the current_house has already had a Valentine's Day
    if all_houses[house] == 0:
        print(f"Place {house} already had Valentine's day.")
        command = input().split()
        continue
    all_houses[house] -= 2
    if all_houses[house] == 0:
        print(f"Place {house} has Valentine's day.")
        all_valentine_days += 1
    command = input().split()

print(f"Cupid's last position was {house}.")
if all_valentine_days == len(all_houses):
    print(f"Mission was successful.")
else:
    houses_that_did_not_celebrated = len(all_houses) - all_valentine_days
    print(f"Cupid has failed {houses_that_did_not_celebrated} places.")
