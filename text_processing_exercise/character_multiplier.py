first, second = input().split()
total_sum = 0
if len(first) > len(second):
    for index in range(len(second)):
        total_sum += ord(first[index]) * ord(second[index])
    for element in first[len(second):]:
        total_sum += ord(element)
elif len(second) > len(first):
    for index in range(len(first)):
        total_sum += ord(first[index]) * ord(second[index])
    for element in second[len(first):]:
        total_sum += ord(element)
else:
    for index in range(len(first)):
        total_sum += ord(first[index]) * ord(second[index])
print(total_sum)
