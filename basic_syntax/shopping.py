budget = int(input())
command = input()
while command != "End":
    current_purchase = int(command)
    budget -= current_purchase
    if budget < 0:
        print("You went in overdraft!")
        break
    command = input()
else:
    print("You bought everything needed.")
