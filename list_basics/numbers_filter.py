iterations = int(input())
COMMAND_EVEN = "even"
COMMAND_ODD = "odd"
COMMAND_NEGATIVE = "negative"
COMMAND_POSITIVE = "positive"
lst_of_numbers = []
filtered_lst = []
for _ in range(iterations):
    current_number = int(input())
    lst_of_numbers.append(current_number)
command = input()

for index in range(len(lst_of_numbers)):
    filtered = (
        (COMMAND_EVEN == command and lst_of_numbers[index] % 2 == 0) or
        (COMMAND_ODD == command and lst_of_numbers[index] % 2 != 0) or
        (COMMAND_NEGATIVE == command and lst_of_numbers[index] < 0) or
        (COMMAND_POSITIVE == command and lst_of_numbers[index] >= 0)
    )
    if filtered:
        filtered_lst.append(lst_of_numbers[index])
print(filtered_lst)
