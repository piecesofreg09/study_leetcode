'''
Using bisect model
find the location is the most important step
using binary search the search can be done in log(n) time
'''

import bisect

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        res = []
        
        right = []
        
        for i in range(len(nums) - 1, -1, -1):
            num = nums[i]
            loc = bisect.bisect_left(right, num)
            res.append(loc)
            right.insert(loc, num)
            #print(right)
        
        return res[::-1]
