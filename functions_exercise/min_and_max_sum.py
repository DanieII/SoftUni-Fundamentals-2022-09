def number_definer(numbers):
    lst_of_numbers = [int(x) for x in numbers]
    min_number = min(lst_of_numbers)
    max_number = max(lst_of_numbers)
    sum_of_numbers = sum(lst_of_numbers)
    return f"""The minimum number is {min_number}
The maximum number is {max_number} 
The sum number is: {sum_of_numbers}"""


all_numbers = input().split()
print(number_definer(all_numbers))
