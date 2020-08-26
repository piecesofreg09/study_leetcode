'''
sort directly
'''

class Solution:
        
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        res = []
        for i in matrix:
            res.extend(i)
        res.sort()
        
        return res[k-1]
        
'''
merge line by line
'''
class Solution:
    def merge(self, l1, l2):
        idd1 = 0
        idd2 = 0
        
        res = []
        #print(l1)
        #print(l2)
        while True:
            if idd1 == len(l1):
                res.extend(l2[idd2:])
                break
            if idd2 == len(l2):
                res.extend(l1[idd1:])
                break
            
            if l1[idd1] <= l2[idd2]:
                res.append(l1[idd1])
                idd1 += 1
            else:
                res.append(l2[idd2])
                idd2 += 1
        
        return res
        
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        temp = matrix[0]
        for li in matrix[1:]:
            temp = self.merge(temp, li)
        #print(temp)
        
        return temp[k-1]
