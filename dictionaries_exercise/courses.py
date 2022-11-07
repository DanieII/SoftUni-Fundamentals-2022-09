students = {}
while True:
    command = input()
    if command == "end":
        break

    course, name = command.split(" : ")
    if course not in students:
        students[course] = [name]
    else:
        students[course].append(name)
for course_name, registered in students.items():
    print(f"{course_name}: {len(students[course_name])}")
    for current_student in students[course_name]:
        print(f"-- {current_student}")
