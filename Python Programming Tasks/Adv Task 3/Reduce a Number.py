class Solution:
    def numberOfSteps(self, num: int) -> int:
        output=0
        obtain=num
        while (obtain!=0):
            if obtain%2==0:
                obtain=obtain//2
            else:
                obtain-=1
            output+=1
        return output