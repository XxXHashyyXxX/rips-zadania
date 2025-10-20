import random
from math import comb

deck = list(range(52))
exact = comb(39,3) / comb(52,3)  # ~0.41398

hits = 0
n = 0
relativeError = 1.0

while relativeError > 0.001:  # 0.1%
    card1, card2, card3 = random.sample(deck, 3)
    n += 1
    if all(c//13 != 0 for c in (card1, card2, card3)):  # brak trefli (Clubs=0)
        hits += 1

    estimate = hits / n
    relativeError = abs(estimate - exact) / exact

print(f"Estimate = {hits/n:.6f}\nExact value = {exact:.6f}\n#iterations = {n}")
