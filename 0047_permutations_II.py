'''
remove duplicates by removing first duplicate first candidates
question decomposed into 
current element + [how to permute remainder element]
eliminate current element in the process
'''
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        def search(nums):
            if len(nums) == 0:
                return [[]]
            if len(nums) == 1:
                return [nums]
            prev = None
            res = []
            for idd, num in enumerate(nums):
                if num == prev:
                    continue
                prev = num
                
                temp = search(nums[:idd] + nums[(idd+1):])
                for templist in temp:
                    res.append([num] + templist)
            #print(res)
            return res
        
        return search(nums)
            
