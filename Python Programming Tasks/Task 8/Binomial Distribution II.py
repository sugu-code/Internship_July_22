import math

p=0.12
q=1-p
result1=0
for i in range(3):
    result1 +=math.factorial(10)/math.factorial(i)/math.factorial(10-i)*(p**i)*(q**(10-i))
    if i==1:
        result2=1-result1
print(round(result1,3))
print(round(result2,3))