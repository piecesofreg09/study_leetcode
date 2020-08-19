'''
1. loop upper limit optimization: current answer length d, will shrink the 
iterator index to be n - d

2. using dict (hash map) to compare of length of current string
if len(dict) = len(str), then valid
if not, then move on

3. sliding window increases everytime d increases
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        resd = 0
        chardict = {}
        
        idd = 0
        
        while idd < (len(s) - resd):
            if s[idd + resd] not in chardict:
                chardict[s[idd + resd]] = 1
            else:
                chardict[s[idd + resd]] += 1
            
            if (idd - 1) >= 0:
                if chardict[s[idd - 1]] == 1:
                    chardict.pop(s[idd - 1])
                else:
                    chardict[s[idd - 1]] -= 1
            
            if len(chardict) == (resd + 1):
                j = idd + resd + 1
                resd += 1
                while j < len(s):
                    if s[j] not in chardict:
                        resd += 1
                        chardict[s[j]] = 1
                    else:
                        chardict[s[j]] += 1
                        break
                    j += 1
            
            
            idd += 1
                    
                
        return resd
            
