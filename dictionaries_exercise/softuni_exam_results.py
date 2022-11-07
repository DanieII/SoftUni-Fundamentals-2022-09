students = {}
languages = {}
while True:
    command = input()
    if command == "exam finished":
        break

    splitted_command = command.split("-")
    if len(splitted_command) < 3:
        user = splitted_command[0]
        del students[user]

    else:
        username, language, points_as_str = splitted_command
        points = int(points_as_str)
        if language not in languages:
            languages[language] = 0
        languages[language] += 1
        if username not in students:
            students[username] = points
        else:
            if students[username] < points:
                students[username] = points
print("Results:")
print("\n".join([f"{key} | {points}" for key, points in students.items()]))
print("Submissions:")
print("\n".join([f"{k} - {v}" for k, v in languages.items()]))
