from math import ceil
from sys import maxsize


number_of_students = int(input())
number_of_lectures = int(input())
additional_bonus = int(input())
biggest_score = -maxsize
attendances_of_the_best_student = 0

for _ in range(number_of_students):
    current_attendances = int(input())
    bonus_points = round(current_attendances / number_of_lectures * (5 + additional_bonus))
    if bonus_points > biggest_score:
        biggest_score = bonus_points
        attendances_of_the_best_student = current_attendances
print(f"Max Bonus: {biggest_score}.")
print(f"The student has attended {ceil(attendances_of_the_best_student)} lectures.")
