def sorted_numbers(my_numbers):
    ascending = sorted(my_numbers)
    final_lst = list(ascending)
    return final_lst


lst = input().split()
numbers = [int(x) for x in lst]
print(sorted_numbers(numbers))
