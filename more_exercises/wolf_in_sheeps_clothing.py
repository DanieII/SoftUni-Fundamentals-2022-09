yard = input().split(", ")
if yard[-1] == "wolf":
    print("Please go away and stop eating my sheep")
else:
    for i in range(len(yard)):
        if yard[i] == "wolf":
            sheep_number = len(yard) - 1 - i
            print(f"Oi! Sheep number {sheep_number}! You are about to be eaten by a wolf!")
