all_numbers = list(map(int, input().split(', ')))
group = 10

while len(all_numbers) > 0:
    current_group = [x for x in all_numbers if x <= group]
    for number in current_group:
        if number in all_numbers:
            all_numbers.remove(number)
    print(f"Group of {group}'s: {current_group}")
    group += 10
