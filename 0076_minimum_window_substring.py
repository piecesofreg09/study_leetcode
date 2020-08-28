'''
two pointers
'''

from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        l = 0
        r = 0
        correct = 0
        
        t_count = Counter(t)
        sub_count = {c:0 for c in t_count}
        res = [float('inf'), ""]
        
        while r < len(s):
            
            
            if s[r] in t_count:
                if sub_count[s[r]] < t_count[s[r]]:
                    correct += 1
                sub_count[s[r]] += 1
            
            while l <= r and correct == len(t):
                #print()
                #print(s[l:r+1])
                if r - l + 1 < res[0]:
                    res = [r - l + 1, s[l:r+1]]
                
                if s[l] in sub_count:
                    sub_count[s[l]] -= 1
                    if sub_count[s[l]] < t_count[s[l]]:
                        correct -= 1
                l += 1
            
            r += 1
        
        return res[1]
