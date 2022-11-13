number = int(input())
number_to_search_for = int(input())
counter = 0
divisor = number

while divisor > 0:
    remainder = divisor % 2
    divisor //= 2
    if remainder == number_to_search_for:
        counter += 1
print(counter)
