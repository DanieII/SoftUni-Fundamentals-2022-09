def average(lst):
    return sum(lst) / len(lst)


def top_numbers(numbers):
    lst_of_all_top_numbers = []
    lst_of_all_numbers = []
    average_number = average(numbers)
    for current_number in numbers:
        if current_number > average_number:
            lst_of_all_top_numbers.append(current_number)
    descending_order = sorted(lst_of_all_top_numbers, reverse=True)
    if len(descending_order) == 0:
        return "No"
    if len(lst_of_all_top_numbers) >= 5:
        current_index = 0
        for current_number in descending_order:
            if current_index < 5:
                lst_of_all_numbers.append(current_number)
            current_index += 1
        without_lst = [str(x) for x in lst_of_all_numbers]
        return " ".join(without_lst)
    without_lst = [str(x) for x in descending_order]
    return " ".join(without_lst)


string = input().split()
lst_of_numbers = [int(x) for x in string]
print(top_numbers(lst_of_numbers))
