from typing import List
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        output=[]
        c=0
        for i in range(len(nums)):
            c+=nums[i]
            output.append(c)
        return output
        