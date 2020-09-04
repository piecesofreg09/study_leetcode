'''
Accumulated sum is recorded
the accumelated sum array will be sorted for faster binary search
for example, for array 
[-2,5,-2,1,2,3,4,-1,2,4,-5,-1]
lower = -4
upper = 4

for the fourth item, the accu list is
[-2, 0, 1, 3], and the current acc sum is 2

lower <= currentsum - prev <= upper
currentsum - upper <= prev <= currentsum - lower
find the left end for (currentsum - upper)
find the right end for (currentsum - lower)
the items in between will be the result that we need
'''

import bisect
class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        acc = 0
        cusum = [0]
        res = 0
        for i in range(0, len(nums)):
            acc += nums[i]
            res += bisect.bisect_right(cusum, acc - lower) - bisect.bisect_left(cusum, acc - upper) 
            bisect.insort(cusum, acc)
        
            #print(cusum)
        
        return res
