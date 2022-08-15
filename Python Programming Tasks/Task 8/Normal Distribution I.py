# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
m=20
sd=2
def nor(x):
    output=1/2*(1+math.erf((x-m) / sd / 2**(1/2)))
    return output
if __name__=='__main__':
    result1=nor(19.5)
    result2=nor(22)-nor(20)
    print(round(result1,3))
    print(round(result2,3))