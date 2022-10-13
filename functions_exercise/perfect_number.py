def get_divisors(my_number):
    divisors = []
    for current_number in range(1, (my_number // 2) + 1):
        if my_number % current_number == 0:
            divisors.append(current_number)
    if my_number == sum(divisors):
        return "We have a perfect number!"
    return "It's not so perfect."


number = int(input())
print(get_divisors(number))
