class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        split=[]
        for i in range(len(str(n))):
            split.append(str(n)[i])
        prod=1
        sum=0
        for i in split:
            prod*=int(i)
            sum+=int(i)
        result=prod-sum
                
        return result