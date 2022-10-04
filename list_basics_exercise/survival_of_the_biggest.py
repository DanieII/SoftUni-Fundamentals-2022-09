lst_of_input = input().split()
lst_of_input_as_int = [int(lst_of_input[x]) for x in range(len(lst_of_input))]
number_of_removed_items = int(input())

for _ in range(number_of_removed_items):
    current_minimal_value = min(lst_of_input_as_int)
    lst_of_input_as_int.remove(current_minimal_value)
print(", ".join(map(str, lst_of_input_as_int)))
