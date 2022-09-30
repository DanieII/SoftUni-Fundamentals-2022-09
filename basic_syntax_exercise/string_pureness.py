# iterations = int(input())
# pure = True
# for i in range(iterations):
#     current_string = input()
#     for j in current_string:
#         if j == "," or j == "." or j == "_":
#             pure = False
#             break
#         else:
#             continue
#     if pure:
#         print(f"{current_string} is pure.")
#     elif not pure:
#         print(f"{current_string} is not pure!")

iterations = int(input())
for _ in range(iterations):
    current_string = input()
    if "," in current_string or "." in current_string or "_" in current_string:
        print(f"{current_string} is not pure!")
    else:
        print(f"{current_string} is pure.")
