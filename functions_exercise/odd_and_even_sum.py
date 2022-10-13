def even_odd_digits(my_number):
    sum_of_even = 0
    sum_of_odd = 0
    for current_number in my_number:
        if int(current_number) % 2 == 0:
            sum_of_even += int(current_number)
        else:
            sum_of_odd += int(current_number)
    return f"Odd sum = {sum_of_odd}, Even sum = {sum_of_even}"


number = input()
print(even_odd_digits(number))
