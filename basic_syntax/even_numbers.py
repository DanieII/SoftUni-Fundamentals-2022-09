n = int(input())


for i in range(n):
    current_number = int(input())
    if current_number % 2 != 0:
        print(f"{current_number} is odd!")
        numbers_not_even = True
        break
else:
    print("All numbers are even.")