iterations = int(input())
word = input()
lst = []
filtered_lst = []
for i in range(iterations):
    current_input = input()
    lst.append(current_input)
    if word in current_input:
        filtered_lst.append(current_input)
print(f'{lst}')
print(f'{filtered_lst}')
