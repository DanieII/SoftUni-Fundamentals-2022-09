age = int(input())

products = ["toddy", "coke", "beer", "whisky"]

if age <= 14:
    print("drink " + products[0])
elif 14 < age <= 18:
    print("drink " + products[1])
elif 18 < age <= 21:
    print("drink " + products[2])
elif 21 < age:
    print("drink " + products[3])