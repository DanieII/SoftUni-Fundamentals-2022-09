my_dict = {}
while True:
    command = input().split(":")
    if len(command) == 1:
        break
    name, id, course = command
    if course not in my_dict:
        my_dict[course] = []
    my_dict[course].append(f"{name} - {id}")
course_to_show = command[0].replace("_", " ")
for student in my_dict[course_to_show]:
    print(student)
