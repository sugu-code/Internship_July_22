class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        c=0
        for i in range(len(startTime)):
            if (queryTime>startTime[i] and queryTime>endTime[i]) or (queryTime<startTime[i] and queryTime<endTime[i]) :
                c+=1
        return len(startTime)-c
        