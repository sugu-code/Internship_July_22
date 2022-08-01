class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums=[]
        for i in range(int(n)):
            nums.append(start+2*i)
        output=nums[0]^nums[1]
        for i in range(2,len(nums)):
            output^=nums[i]
        return output