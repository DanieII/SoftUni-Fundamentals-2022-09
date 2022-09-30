iterations = int(input())
final_sum = 0
for i in range(iterations):
    current_char = input()
    final_sum += ord(current_char)
print(f"The sum equals: {final_sum}")