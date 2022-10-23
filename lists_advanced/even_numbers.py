def even_numbers(numbers):
    even_indices = []
    for current_number in numbers:
        if current_number % 2 == 0:
            even_indices.append(numbers.index(current_number))
    return even_indices


lst_of_numbers = list(map(int, input().split(", ")))
print(even_numbers(lst_of_numbers))

# Using comprehension
lst_of_numbers = list(map(int, input().split(", ")))
indices = [current_index for current_index in range(len(lst_of_numbers)) if lst_of_numbers[current_index] % 2 == 0]
print(indices)
