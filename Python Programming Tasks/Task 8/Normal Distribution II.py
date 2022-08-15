# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
m=70
sd=10
def nor(x):
    output=1/2*(1+math.erf((x-m) / sd / 2**(1/2)))
    return output

if __name__=='__main__':
    result1=(1-nor(80))*100
    result2=(1-nor(60))*100
    result3=nor(60)*100
    print(round(result1,2))
    print(round(result2,2))
    print(round(result3,2))