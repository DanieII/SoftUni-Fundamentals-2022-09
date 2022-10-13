def sum_numbers(number1, number2):
    return number1 + number2


def subtract(sum_of_first, number3):
    return sum_of_first - number3


def add_and_subtract(number1, number2, number3):
    sum_of_first_func = sum_numbers(number1, number2)
    return subtract(sum_of_first_func, number3)


first_number = int(input())
second_number = int(input())
third_number = int(input())
print(add_and_subtract(first_number, second_number, third_number))
