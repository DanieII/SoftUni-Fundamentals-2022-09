quantity_of_food = float(input()) * 1000
quantity_of_hay = float(input()) * 1000
quantity_of_cover = float(input()) * 1000
pig_kilograms = float(input()) * 1000
current_day = 1
everything_is_enough = True
while True:
    if current_day > 30:
        break
    quantity_of_food -= 300
    if current_day % 2 == 0:
        quantity_of_hay -= quantity_of_food * 0.05
    if current_day % 3 == 0:
        quantity_of_cover -= pig_kilograms / 3
    if quantity_of_cover <= 0 or quantity_of_hay <= 0 or quantity_of_food <= 0:
        everything_is_enough = False
        break
    current_day += 1

if everything_is_enough:
    print(f"Everything is fine! Puppy is happy! Food: {quantity_of_food / 1000:.2f}, Hay: {quantity_of_hay / 1000:.2f}, Cover: {quantity_of_cover / 1000:.2f}.")

else:
    print("Merry must go to the pet store!")
