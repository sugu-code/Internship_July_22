import math


p = 1.09/(1+1.09)
q=1-p
B = 0
for i in range(3):
    B += math.factorial(6) / math.factorial(i) / math.factorial(6-i) * p**i * (1-p)**(6-i)
print(round(1-B, 3))