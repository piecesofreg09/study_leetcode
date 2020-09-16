'''
pre allocate
'''
class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        n = len(matrix)
        m = len(matrix[0])
        total = n + m + 1
        
        start = [[0, i] for i in range(m)] + [[i, m - 1] for i in range(1, n)]
        #print(start)
        length = [min(i+1, m, n) for i in range(m)] + [min(n - i, m, n) for i in range(1, n)]
        #print(length)
        count = -1
        
        res = []
        for st, le in zip(start, length):
            count += 1
            if count % 2 == 1:
                for j in range(le):
                    res.append(matrix[st[0]+j][st[1]-j])
            else:
                res.extend([None] * le)
                for j in range(le):
                    res[-j-1] = matrix[st[0]+j][st[1]-j]
        
        return res
                
        
        
