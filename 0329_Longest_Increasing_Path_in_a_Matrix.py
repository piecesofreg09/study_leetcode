'''
dynamic programming
'''
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        if not matrix:
            return 0
        if not matrix[0]:
            return 0
        
        dirs = [[-1,0],[1,0],[0,-1],[0,1]]
        dp = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
        
        ans = 1
        
        def dfs(i, j):
            nonlocal ans
            if dp[i][j] > 0:
                return dp[i][j]
            
            res = [0]
            for dir_t in dirs:
                x = i + dir_t[0]
                y = j + dir_t[1]
                
                if 0 <= x < len(matrix) and 0 <= y < len(matrix[0]) and matrix[x][y] < matrix[i][j]:
                    res.append(dfs(x, y))
            
            dp[i][j] = 1 + max(res)
            ans = max(ans, dp[i][j])
            return dp[i][j]
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                dfs(i, j)
        
        return ans


'''
generic backtrack (TLE)
'''
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        if not matrix:
            return 0
        if not matrix[0]:
            return 0
        
        dirs = [[-1,0],[1,0],[0,-1],[0,1]]
        
        visited = [[False for i in range(len(matrix[0]))] for i in range(len(matrix))]
        
        res = 1
        def backtrack(i, j, curlength):
            nonlocal res
            res = max(res, curlength)
            
            for dir_t in dirs:
                x = i + dir_t[0]
                y = j + dir_t[1]
                
                if 0 <= x < len(matrix) and 0 <= y < len(matrix[0]) and (not visited[x][y]) and matrix[x][y] < matrix[i][j]:
                    visited[x][y] = True
                    backtrack(x, y, curlength+1)
                    visited[x][y] = False
                    
            return
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                visited[i][j] = True
                backtrack(i, j, 1)
                visited[i][j] = False
        
        return res

