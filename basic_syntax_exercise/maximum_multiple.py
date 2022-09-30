from sys import maxsize
divisor = int(input())
boundary = int(input())
max_num = -maxsize

for i in range(1, boundary + 1):
    if i % divisor == 0 and boundary >= i > 0 and i > max_num:
        max_num = i
print(max_num)