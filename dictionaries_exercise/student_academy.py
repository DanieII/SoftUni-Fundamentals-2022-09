my_dict = {}
only_above_average = {}
iterations = int(input())
for _ in range(iterations):
    name = input()
    grade = float(input())
    if name not in my_dict:
        my_dict[name] = [grade]
    else:
        my_dict[name].append(grade)

# filtering only the ones with average grade more than 4.50 in another dictionary
for student, average_grade in my_dict.items():
    current_average_grade = sum(average_grade) / len(average_grade)
    if current_average_grade >= 4.50:
        only_above_average[student] = current_average_grade
        print(f"{student} -> {current_average_grade:.2f}")
