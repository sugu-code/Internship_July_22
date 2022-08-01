class Solution:
    def numTeams(self, rating: List[int]) -> int:
        output=[]
        t=[]
        for i in range(len(rating)-2):
            for j in range(i,len(rating)-1):
                for k in range(j,len(rating)):
                    if rating[i]<rating[j]<rating[k] or rating[i]>rating[j]>rating[k]:
                        t=[rating[i],rating[j],rating[k]]
                        print(t)
                        output.append(list(t))
        return len(output)