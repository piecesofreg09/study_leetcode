class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix or not matrix[0]:
            return [[]]
        n = len(matrix)
        m = len(matrix[0])
        res = [[float('inf') if matrix[j][i] != 0 else 0 for i in range(m)] for j in range(n)]
        
        for i in range(n):
            for j in range(m):
                if matrix[i][j] != 0:
                    if i > 0:
                        res[i][j] = min(res[i-1][j]+1, res[i][j])
                    if j > 0:
                        res[i][j] = min(res[i][j-1]+1, res[i][j])
        
        
        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                if matrix[i][j] != 0:
                    if i < n-1:
                        res[i][j] = min(res[i+1][j]+1, res[i][j])
                    if j < m-1:
                        res[i][j] = min(res[i][j+1]+1, res[i][j])
        
        return res
