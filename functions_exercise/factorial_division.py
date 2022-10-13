def factorial(my_number):
    number = 1
    for current_number in range(2, my_number + 1):
        number *= current_number
    return number


first_number = int(input())
second_number = int(input())
first_factorial, second_factorial = factorial(first_number), factorial(second_number)
result = first_factorial / second_factorial
print(f"{result:.2f}")
