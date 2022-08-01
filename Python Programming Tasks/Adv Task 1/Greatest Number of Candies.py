class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        output=[]
        for i in range(len(candies)):
            c= candies[i]+extraCandies>=max(candies)
            output.append(c)
        return output   
        
        