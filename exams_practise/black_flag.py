days = int(input())
daily = int(input())
expected = float(input())
plunder = 0

for day in range(1, days + 1):
    plunder += daily
    if day % 3 == 0:
        plunder += daily / 2
    if day % 5 == 0:
        plunder -= plunder * 0.3

if plunder >= expected:
    print(f"Ahoy! {plunder:.2f} plunder gained.")
else:
    percentage = (plunder / expected) * 100
    print(f"Collected only {percentage:.2f}% of the plunder.")
