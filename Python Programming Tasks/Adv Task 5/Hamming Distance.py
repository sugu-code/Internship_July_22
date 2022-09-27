class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        sum=0
        xy=bin(x^y)
        number_xy=xy[2:]
        for i in number_xy:
            sum+=int(i)
        return sum