'''
three pointers
left: right edge of 0s
cur: current element to be processed
right: left edge of 2s

trick: between left and cur it should all be 1s

'''
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        cur = 0
        r = len(nums) - 1
        
        while cur <= r:
            if nums[cur] == 0:
                nums[cur], nums[l] = nums[l], nums[cur]
                l += 1
                cur += 1
            elif nums[cur] == 1:
                cur += 1
            else:
                nums[cur], nums[r] = nums[r], nums[cur]
                r -= 1
            #print(nums)
                    
        
