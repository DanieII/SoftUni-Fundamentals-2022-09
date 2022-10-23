from math import ceil

budget = float(input())
students = int(input())
price_for_one_flour = float(input())
price_for_one_egg = float(input())
price_for_one_apron = float(input())
current_managing = 1
free_packages = students // 5

full_price = price_for_one_apron * (ceil(students * 1.20)) + price_for_one_egg * 10 * students + price_for_one_flour * (students - free_packages)

if budget >= full_price:
    print(f"Items purchased for {full_price:.2f}$.")
else:
    needed_money = full_price - budget
    print(f"{needed_money:.2f}$ more needed.")
