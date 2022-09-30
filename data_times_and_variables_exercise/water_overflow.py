capacity = 255
iterations = int(input())
water_stored = 0
for _ in range(iterations):
    current_pouring = int(input())
    if capacity - current_pouring < 0:
        print("Insufficient capacity!")
        continue
    capacity -= current_pouring
    water_stored += current_pouring
print(water_stored)