'''
sort from large to small
calculate accu sum from the beginning
add the accu sum to the result
one the accu sum < 0, stop the result
a1
a1,a2
a1,a2,a3
a1,a2,a3,a4 <- if this accu sum is smaller than 0, means there is no need to add more
'''

class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        
        satisfaction.sort(reverse=True)
        
        csum = 0
        total = 0
        res = 0
        for s in satisfaction:
            csum += s
            total += csum
            if total > res:
                res = total
            
            if csum < 0:
                break
        
        return res
        
