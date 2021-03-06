'''
---(i-1, j-1)---(i,j-1)---
----    r1   ----  r2  ---
---(i-1, j)-----(i,j)---
----    r3   ----  r4 ----

when the p is "*", then match with the r2 || r3
when the p is "?", then match with r1
when the p is a letter, then match with r1 || p[i] == s[j]

'''
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False for i in range(len(s) + 1)] for j in range(len(p) + 1)]
        
        dp[0][0] = True
        
        for i in range(1, len(p) + 1):
            if p[i - 1] == "*":
                dp[i][0] = dp[i-1][0]
                
        for j in range(1, len(p) + 1):
            for i in range(1, len(s) + 1):
                if p[j - 1] == "*":
                    dp[j][i] = dp[j - 1][i] or dp[j][i - 1]
                elif p[j - 1] == "?":
                    dp[j][i] = dp[j - 1][i - 1]
                else:
                    if p[j - 1] == s[i - 1]:
                        dp[j][i] = dp[j - 1][i - 1]
        
        return dp[-1][-1]
