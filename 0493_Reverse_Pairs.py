import bisect

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        left = []
        
        res = 0
        for i in range(len(nums)):
            num = nums[i]
            #print(left)
            loc = bisect.bisect_right(left, 2 * num)
            #print(loc)
            temp = len(left) - loc
            res += temp
            bisect.insort_left(left, num)
            
        
        return res
