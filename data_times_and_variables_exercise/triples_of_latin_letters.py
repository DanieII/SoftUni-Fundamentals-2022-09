iterations = int(input())
for first in range(iterations):
    for second in range(iterations):
        for third in range(iterations):
            print(f"{chr(97 + first)}{chr(97 + second)}{chr(97 + third)}")