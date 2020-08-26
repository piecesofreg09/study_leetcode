'''
Dynamic programming
compare the s3[i+j+1] character with the s1[i] or s2[j]
The result is only related with the results above or left
'''

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        dp = [[False for i in range(len(s2) + 1)] for j in range(len(s1) + 1)]
        
        dp[0][0] = True
        
        for i in range(len(s1)):
            if s3[i] == s1[i]:
                dp[i + 1][0] = True and dp[i][0]
        
        for i in range(len(s2)):
            if s3[i] == s2[i]:
                dp[0][i + 1] = True and dp[0][i]
        
        for i in range(len(s1)):
            for j in range(len(s2)):
                dp[i + 1][j + 1] = (dp[i][j+1] and s3[i+j+1] == s1[i]) or (dp[i+1][j] and s3[i+j+1] == s2[j])
        
        return dp[-1][-1]
