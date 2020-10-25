class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        leftid = []
        rightid = []
        
        if seats[0] == 0:
            leftid.append(0)
        
        for idd in range(1, len(seats)):
            if seats[idd] == 0 and seats[idd-1] == 1:
                leftid.append(idd)
        
        if seats[-1] == 0:
            rightid.append(len(seats) - 1)
        
        for idd in range(len(seats) - 2, -1, -1):
            if seats[idd] == 0 and seats[idd+1] == 1:
                rightid.append(idd)
        
        rightid = rightid[::-1]
        
        #print(leftid)
        #print(rightid)
        
        mindis = 0
        
        for i in range(len(leftid)):
            if leftid[i] != 0 and rightid[i] != 0:
                temp = (rightid[i] - leftid[i] + 2) // 2
                if temp > mindis:
                    mindis = temp
        
        if leftid[0] == 0:
            mindis = max(mindis, rightid[0] + 1)
        
        if rightid[-1] == (len(seats) - 1):
            mindis = max(mindis, rightid[-1] - leftid[-1] + 1)
        
        #print(mindis)
        
        return mindis
