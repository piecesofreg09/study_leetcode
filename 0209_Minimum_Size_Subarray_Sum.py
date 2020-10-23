'''
Two cursors
'''
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if s > sum(nums):
            return 0
        res = float('inf')
        nums = nums
        cur1 = 0
        cur2 = 0
        summ = 0
        while cur2 < len(nums) and summ < s:
            summ += nums[cur2]
            cur2 += 1
        res = min(cur2 - cur1, res)
        #print([cur1, cur2])
        
        while cur1 < len(nums) and summ >= s:
            while cur1 < len(nums) and summ >= s:
                
                summ -= nums[cur1]
                cur1 += 1
            res = min(cur2 - cur1 + 1, res)
            #print([cur1, cur2])
                
            while cur2 < len(nums) and summ < s:
                summ += nums[cur2]
                cur2 += 1
            res = min(cur2 - cur1 + 1, res)
            #print([cur1, cur2])
        
        return res
