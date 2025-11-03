import random

n = int(input("Enter the number of which you want cube root of: "))
g = random.randint(1,n)

while True:
    g = (2*g + n/(g*g)) / 3

    if abs((g**3) - n) < 1e-6:
        break
print("Approximate cubed:", g)
print("Integer cubed:", int(g))
