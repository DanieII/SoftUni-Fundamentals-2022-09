sequence = input().split()
for word in sequence:
    print(word * len(word), end="")
# Comprehension
# [print(word * len(word)) for word in input().split()]
