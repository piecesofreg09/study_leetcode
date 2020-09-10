'''
https://leetcode.com/problems/split-array-into-consecutive-subsequences/discuss/106495/Java-O(n)-time-and-O(1)-space-solution-greedily-extending-shorter-subsequence

cur != pre + 1: for this case, cur cannot be added to any consecutive subsequences
ending at pre, therefore, we must have p1 == 0 && p2 == 0; 
otherwise the input array cannot be split into consecutive subsequences of length >= 3. 
Now let c1, c2, c3 be the number of consecutive subsequences ending at cur with length of 1, length of 2 and length >= 3, 
respectively, we will have c1 = cnt, c2 = 0, c3 = 0, 
which means we only have consecutive subsequence ending at cur with length of 1 and its number given by cnt.

cur == pre + 1: for this case, cur can be added to consecutive subsequences ending at pre and thus extend those subsequences. 
But priorities should be given to those with length of 1 first, then length of 2 and lastly length >= 3. 
Also we must have cnt >= p1 + p2; otherwise the input array cannot be split into consecutive subsequences of length >= 3. 
Again let c1, c2, c3 be the number of consecutive subsequences ending at cur with length of 1, length of 2 and length >= 3, 
respectively, we will have: c2 = p1, c3 = p2 + min(p3, cnt - (p1 + p2)), c1 = max(cnt - (p1 + p2 + p3), 0). 
The meaning is as follows: first adding cur to the end of subsequences of length 1 will make them subsequences of length 2, 
and we have p1 such subsequences, therefore c2 = p1. 
Then adding cur to the end of subsequences of length 2 will make them subsequences of length 3, and we have p2 such subsequences, therefore c3 is at least p2. 
If cnt > p1 + p2, we can add the remaining cur to the end of subsequences of length >= 3 to make them even longer subsequences. 
The number of such subsequences is the smaller one of p3 and cnt - (p1 + p2).
In total, c3 = p2 + min(p3, cnt - (p1 + p2)). If cnt > p1 + p2 + p3, then we still have remaining cur that cannot be added to any subsequences. 
These residual cur will form subsequences of length 1, hence c1 = max(cnt - (p1 + p2 + p3), 0).
'''
from collections import Counter

class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        
        counts = Counter(nums)
        
        pre = -float('inf')
        p1 = 0
        p2 = 0
        p3 = 0
        
        c1 = 0
        c2 = 0
        c3 = 0
        
        
        for num, count in counts.items():
            cur = num
            
            if cur != pre + 1:
                if (p1 != 0 or p2 != 0):
                    return False
                
                c1 = count
                c2 = 0
                c3 = 0
            else:
                if count < p1 + p2:
                    return False
                
                c1 = max(0, count - (p1 + p2 + p3))
                c2 = p1
                c3 = p2 + min(p3, count - p1 - p2)
            
            pre = cur
            p1 = c1
            p2 = c2
            p3 = c3
        
        return p1 == 0 and p2 == 0
