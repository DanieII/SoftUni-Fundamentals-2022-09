import re

text = input()
pattern = r"([\#\|])([A-Za-z\s]+)\1(\d{2}\/\d{2}\/\d{2})\1(\d{1,5})\1"
result = re.findall(pattern, text)
sum_of_calories = sum([int(x[3]) for x in result])
days_to_last = sum_of_calories // 2000
print(f"You have food to last you for: {days_to_last} days!")
for item in result:
    product, expiration_date, calories = item[1], item[2], item[3]
    print(f"Item: {product}, Best before: {expiration_date}, Nutrition: {calories}")
