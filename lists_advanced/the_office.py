def average(lst):
    return sum(lst) / len(lst)


happiness = list(map(int, input().split()))
happiness_improvement = int(input())
after_improvement = [(x * happiness_improvement) for x in happiness]
average_happiness = (average(after_improvement))
greater_than_average = [x for x in after_improvement if x > average_happiness]
if len(greater_than_average) >= len(after_improvement) // 2:
    print(f"Score: {len(greater_than_average)}/{len(after_improvement)}. Employees are happy!")
else:
    print(f"Score: {len(greater_than_average)}/{len(after_improvement)}. Employees are not happy!")
