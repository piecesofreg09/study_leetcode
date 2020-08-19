'''
dynamic programming
'''
class Solution:
    def jump(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return 0
        elif len(nums) == 2:
            return 1
        
        n = len(nums)
        res = [[] for i in range(n)]
        
        #print(res)
        #print(n)
        
        res[n - 1].append(0)
        res[n - 2].append(1)
        #print(res)
        
        curmax = nums[n - 2]
        curid = n - 2
        for i in range(n - 3, -1, -1):
            if i != 0 and nums[i] > curmax and nums[i] < nums[i - 1]:
                curmax = nums[i]
                continue
            else:
                curmax = nums[i]
                curid = i
            inside_min = float('inf')
            for j in range(curid - i, nums[i] + 1):
                if i + j < n:
                    for k in res[i + j]:
                        if 1 + k < inside_min:
                            inside_min = 1 + k
            res[i] = [inside_min]
            #print(res)
        
        return min(res[0])
