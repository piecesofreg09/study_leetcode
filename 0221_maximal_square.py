'''
dp
dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + 1
'''
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        n = len(matrix)
        m = len(matrix[0])
        
        dp = [[0 for j in range(m)] for i in range(n)]
        
        res = 0
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == "1":
                    dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + 1
                    res = res if res > dp[i][j] else dp[i][j]
                    #print(dp)
        
        return res * res
