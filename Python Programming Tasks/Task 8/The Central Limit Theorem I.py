# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
tot=9800
n=49
m=205
sd=15
def cen(x,M,std):
    output = 1/2*(1+math.erf((x-M) / std / 2**(1/2)))
    return output

M=n*m
std=sd*n**(0.5)
result=cen(tot,M,std)
print(round(result,4))