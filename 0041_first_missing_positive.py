'''
put all numbers 1, 2, 3, 4 in place
and find the first missing not in-place value
'''
class Solution:
    def firstMissingPositive(self, nums_ori: List[int]) -> int:
        
        if len(nums_ori) == 0:
            return 1
        
        hash_dict = {}
        nums = []
        for num in nums_ori:
            if num not in nums:
                nums.append(num)
                hash_dict[num] = True
        
        for i in range(len(nums)):
            if nums[i] != i + 1:
                temp = nums[i]
                while temp > 0 and temp <= len(nums) and temp != i + 1:
                    xx = nums[temp - 1]
                    nums[temp - 1] = temp
                    temp = xx
                    #print(nums)
                if temp != i + 1:
                    nums[i] = 0
                else:
                    nums[i] = temp
            
        res = len(nums) + 1
        for i in range(len(nums)):
            if nums[i] != i + 1:
                res = i + 1
                break
        
        return res
