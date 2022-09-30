from sys import maxsize


max_number = -maxsize
for i in range(3):
    current_number = int(input())
    if current_number > max_number:
        max_number = current_number
print(max_number)
