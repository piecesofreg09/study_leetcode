'''
Dynamic programming
state transfer:
compare if the current pair of char is equal
if equal: min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1] - 1) + 1
if not equal: min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
'''

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0 for i in range(len(word1) + 1)] for j in range(len(word2) + 1)]
        
        for i in range(len(word2)):
            dp[i + 1][0] = i + 1
        
        for j in range(len(word1)):
            dp[0][j + 1] = j + 1
        
        for i in range(1, len(word2) + 1):
            for j in range(1, len(word1) + 1):
                if word1[j - 1] != word2[i - 1]:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1] - 1) + 1
        #print(dp)
        return dp[-1][-1]
