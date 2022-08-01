class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        output=0
        for i in nums:
            c=len(str(i))
            if c%2==0:
                output+=1
        return output