class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        count = 0
        
        nums = [-float('inf')] + nums + [float('inf')]
        
        count = 0
        for i in range(len(nums) - 1):
            if nums[i] > nums[i+1]:
                count += 1
                if count >= 2:
                    return False
                temp = i
                
        if count == 0 or temp == 0 or temp == len(nums) - 2 or nums[temp-1] <= nums[temp+1] or nums[temp] <= nums[temp+2]:
            return True
