'''
dynamic programming
'''
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        dp = [1 for i in range(len(nums))]
        
        res = 1
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = (dp[j] + 1) if (dp[j] + 1) > dp[i] else (dp[i])
            #print(dp)
            res = res if res > dp[i] else dp[i]
        
        return res
