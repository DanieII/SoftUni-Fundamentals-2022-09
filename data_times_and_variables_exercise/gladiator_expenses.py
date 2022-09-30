iterations = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
price_for_repair = 0
shields_broken = 0
for i in range(1, iterations + 1):
    if i % 2 == 0:
        price_for_repair += helmet_price
    if i % 3 == 0:
        price_for_repair += sword_price
        if i % 2 == 0:
            shields_broken += 1
            price_for_repair += shield_price
            if shields_broken % 2 == 0:
                price_for_repair += armor_price
print(f"Gladiator expenses: {price_for_repair:.2f} aureus")