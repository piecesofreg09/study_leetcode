'''
backtrack
sort the data first
then add in the elements one by one
'''
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates.sort()
        
        res = []
        def backtrack(index, path, target):
            nonlocal res, candidates
            #print(path)
            if target < 0:
                return
            if target == 0:
                res.append(path)
                return
            #print(candidates[index:])
            for idd in range(index, len(candidates)):
                if idd > index and candidates[idd] == candidates[idd - 1]:
                    continue
                else:
                    backtrack(idd + 1, path + [candidates[idd]], target - candidates[idd])
            return
        backtrack(0, [], target)
        return res
