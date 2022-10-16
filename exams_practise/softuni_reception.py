# first_employee_efficiency = int(input())
# second_employee_efficiency = int(input())
# third_employee_efficiency = int(input())
# student_count = int(input())
# number_of_answers_per_hour = first_employee_efficiency + second_employee_efficiency + third_employee_efficiency
# current_hour = 1
# all_answered = False
# while not all_answered:
#     if current_hour % 4 == 0:
#         current_hour += 1
#     if student_count - number_of_answers_per_hour <= 0:
#         all_answered = True
#         break
#     student_count -= number_of_answers_per_hour
#     current_hour += 1
# if all_answered:
#     print(f"Time needed: {current_hour}h.")


########## using while True ###########
first_employee_efficiency = int(input())
second_employee_efficiency = int(input())
third_employee_efficiency = int(input())
student_count = int(input())
number_of_answers_per_hour = first_employee_efficiency + second_employee_efficiency + third_employee_efficiency
current_hour = 1
while True:
    if current_hour % 4 == 0:
        current_hour += 1
    if student_count - number_of_answers_per_hour <= 0:
        print(f"Time needed: {current_hour}h.")
        break
    student_count -= number_of_answers_per_hour
    current_hour += 1
