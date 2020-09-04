class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.res = []
        self.nums = nums
        self.dfs(0, [])
        return self.res
    def dfs(self, idd, path):
        #print(path)
        self.res.append(path)
        for i in range(idd, len(self.nums)):
            if i > idd and self.nums[i] == self.nums[i - 1]:
                continue
            else:
                self.dfs(i+1, path + [self.nums[i]])
        return
