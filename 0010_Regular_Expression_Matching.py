'''
dynamic programming
s = "" and p = any, the edge case is determined by the following
  if p[j - 1] == "*", the result is dp[j][0] = dp[j-2][0]
  if p[j - 1] == ".", the result is false
s = any and p = "", the edge case should be false
s = "" and p = "", the edge case is True

then the case:
  if p[i-1] = "*":
    then if the char before "*" match with the current char, then we can either ignore the "*" case, or ignore the last char in the string
    if the char doens't match: then check the result if ignoring the letter+"*" combination
  else:
    if matches: dp[i][j] = dp[i-1][j-1]
    else: false

'''

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False for i in range(len(s) + 1)] for j in range(len(p) + 1)]
        
        dp[0][0] = True
        
        for j in range(1, len(p) + 1):
            if p[j - 1] == '*':
                dp[j][0] = dp[j - 2][0]
            elif p[j - 1] == '.':
                dp[j][0] = False
            else:
                dp[j][0] = False
        #print(dp)
        for i in range(1, len(p) + 1):
            for j in range(1, len(s) + 1):
                if p[i - 1] == "*":
                    if p[i-2] == s[j-1] or p[i-2] == '.':
                        dp[i][j] = dp[i-2][j] or dp[i][j-1]
                    else:
                        dp[i][j] = dp[i-2][j]
                elif p[i - 1] ==  ".":
                    dp[i][j] = dp[i-1][j-1]
                else:
                    if p[i - 1] == s[j - 1]:
                        dp[i][j] = dp[i-1][j-1]
                #print(dp)
        
        return dp[-1][-1]
