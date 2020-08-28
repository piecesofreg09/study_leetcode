'''
https://leetcode.com/problems/single-number-ii/discuss/43295/Detailed-explanation-and-generalization-of-the-bitwise-operation-method-for-single-numbers
https://medium.com/@lenchen/leetcode-137-single-number-ii-31af98b0f462
'''
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        x1 = 0
        x2 = 0
        mask = 0;
         
        for i in nums:
            x2 ^= x1 & i
            x1 ^= i
            mask = ~(x1 & x2)
            x2 &= mask
            x1 &= mask

        return x1

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = (sum(set(nums)) * 3 - sum(nums)) // 2

        return res
        
