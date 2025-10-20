import random

n = 0
sum = 0

N = int(input("Podaj ilość iteracji: "))

for i in range(N):
    x = random.uniform(0, 1)
    y = random.uniform(0, 1)

    n += 1
    sum += 1 if x*x + y*y <= 1 else 0

P = sum / n

pi = 4 * P
print("pi = ", pi)