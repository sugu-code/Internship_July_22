# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
tot=250
n=100
m=2.4
sd=2.0

def cen(x,M,std):
    output=1/2*(1+math.erf((x-M) / std / 2**(1/2)))
    return output

if __name__=='__main__':
    M=n*m
    std=sd*n**(0.5)
    result=cen(tot,M,std)
    print(round(result,4))