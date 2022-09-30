n = int(input())
for i in range(1, n + 1):
    special_number = False
    current_sum = 0
    digits = i
    while digits > 0:
        current_sum += digits % 10
        digits = digits // 10
    if current_sum == 5 or current_sum == 7 or current_sum == 11:
        special_number = True
    print(f"{i} -> {special_number}")