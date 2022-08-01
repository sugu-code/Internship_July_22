class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        l=[]
        c=n
        m=0
        for i in range(len(nums)):
            if i==c and m<2:
                l.insert(i-n-2,nums[i])
                c=i+1
                m+=1
            else:
                l.append(nums[i])
        return l    
        
        