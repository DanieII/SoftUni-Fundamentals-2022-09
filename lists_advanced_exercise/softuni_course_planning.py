def add(lst, my_lesson):
    if my_lesson not in lst:
        lst.append(my_lesson)
    return lst


def insert(lst, my_lesson, my_index):
    if my_lesson not in lst:
        lst.insert(my_index, my_lesson)
    return lst


def remove(lst, my_lesson):
    if my_lesson in lst:
        lst.remove(my_lesson)
    if f"{my_lesson}-Exercise" in lst:
        lst.remove(f"{my_lesson}-Exercise")
    return lst


def exercise(lst, my_lesson):
    # USING EXTEND BUT JUDGE DOESN'T GIVE 100/100
    # if my_lesson in lst:
    #     lesson_index = courses.index(my_lesson)
    #     if not courses[lesson_index + 1] == f"{my_lesson}-Exercise":
    #         courses.insert(lesson_index + 1, f"{my_lesson}-Exercise")
    # else:
    #     items_to_add = [my_lesson, f"{my_lesson}-Exercise"]
    #     courses.extend(items_to_add)
    if my_lesson not in lst:
        lst.append(my_lesson)
    if f'{my_lesson}-Exercise' not in lst:
        index_of_lesson = lst.index(my_lesson)
        lst.insert(index_of_lesson + 1, f'{my_lesson}-Exercise')
    return lst


def swap(lst, my_first, my_second):
    if my_first in lst and my_second in lst:
        first_index = lst.index(my_first)
        second_index = lst.index(my_second)
        lst[first_index], lst[second_index] = lst[second_index], lst[first_index]
        # Putting the exercise after the lesson in case we swap a lesson with an exercise
        if f'{my_first}-Exercise' in courses:
            courses.remove(f'{my_first}-Exercise')
            courses.insert(second_index + 1, f'{my_first}-Exercise')
        if f'{my_second}-Exercise' in courses:
            courses.remove(f'{my_second}-Exercise')
            courses.insert(first_index + 1, f'{my_second}-Exercise')
    return lst


courses = input().split(", ")

while True:
    command = input()
    if command == "course start":
        break
    current_command = command.split(":")
    action = current_command[0]
    lesson = current_command[1]

    if action == "Add":
        courses = add(courses, lesson)
    elif action == "Insert":
        index = int(current_command[2])
        courses = insert(courses, lesson, index)
    elif action == "Remove":
        courses = remove(courses, lesson)
    elif action == "Swap":
        first, second = current_command[1], current_command[2]
        courses = swap(courses, first, second)
    elif action == "Exercise":
        courses = exercise(courses, lesson)
print("\n".join([f"{number + 1}.{lesson}" for number, lesson in enumerate(courses)]))
