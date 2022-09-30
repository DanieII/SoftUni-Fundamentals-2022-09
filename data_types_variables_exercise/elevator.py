from math import ceil
number_of_people = int(input())
capacity = int(input())
number_of_courses = number_of_people / capacity
print(ceil(number_of_courses))