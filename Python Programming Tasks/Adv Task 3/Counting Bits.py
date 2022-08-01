class Solution:
    def countBits(self, n: int) -> List[int]:
        output=[]
        for i in range(n+1):
            sum=0
            c=bin(i)[2:]
            while(int(c)>0):
                sum+=(int(c)%10)
                c=int(c)//10
            output.append(sum)
        return output
        