'''
One through
keep a list for the current continuous range
'''
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        res = []
        temp = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] == temp[-1] + 1:
                temp.append(nums[i])
            else:
                if len(temp) == 1:
                    res.append(str(temp[0]))
                else:
                    res.append(str(temp[0]) + "->" + str(temp[-1]))
                temp = [nums[i]]
        if len(temp) == 1:
            res.append(str(temp[0]))
        else:
            res.append(str(temp[0]) + "->" + str(temp[-1]))
        return res
