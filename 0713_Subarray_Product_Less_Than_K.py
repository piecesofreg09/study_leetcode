'''
for each right, find the left that makes [left, right] subarray that has product slightly smaller than k
add in all subarrays that ends with 'right'
for example
[3,4,5,6,7,1,2,8], k = 40

all the subarrays are
end 3: [3]
end 4: [3, 4]
end 5: [4,5]
end 6: [5,6]
end 7: [7]
end 1: [7,1]
end 2: [7,1,2]
end 8: [1,2,8]

'''
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        
        if k <=1 :
            return 0
        
        left = 0
        
        product = 1
        
        res = 0
        
        for idd, num in enumerate(nums):
            product *= num
            while product >= k:
                product = product / nums[left]
                left += 1
            
            res += (idd - left) + 1
        
        return res
