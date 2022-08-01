class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        a=set(nums)
        output=[]
        for i in a:
            if nums.count(i)==1:
                output.append(i)
        return output