'''
Construct from bottom
'''
class Solution1:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = [[]]
        for num in nums:
            res += [cur + [num] for cur in res]
        return res
        
'''
Using masks
'''
class Solution2:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        limit = 1 << len(nums)
        res = [None for i in range(limit)]
        masks = [1 << i for i in range(limit)]
        for idd in range(limit):
            temp = []
            for c, mask in enumerate(masks):
                if idd & mask:
                    temp.append(nums[c])
            res[idd] = temp
        return res
