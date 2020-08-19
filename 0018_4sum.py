'''
find all two value pairs, create hash map for value lookup
'''
class Solution:
    
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        
        nums.sort()
        #print(nums)
        sums_hash = {}
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                li_sum = nums[i] + nums[j]
                if li_sum not in sums_hash:
                    sums_hash[li_sum] = [[i, j]]
                else:
                    sums_hash[li_sum].append([i, j])
        #print(sums_hash)
        
        
        res = []
        res_hash = {}
        for key, pairs in sums_hash.items():
            if (target - key) in sums_hash:
                
                pairs_1 = pairs
                pairs_2 = sums_hash[(target - key)]

                for i in range(len(pairs_1)):
                    for j in range(len(pairs_2)):
                        if len(set(pairs_1[i] + pairs_2[j])) < 4:
                            break
                        temp = sorted([nums[pairs_1[i][0]], nums[pairs_1[i][1]], nums[pairs_2[j][0]], nums[pairs_2[j][1]]])
                        temp_tuple = tuple(temp)
                        if temp_tuple not in res_hash:
                            res.append(temp)
                            res_hash[temp_tuple] = True
        return res
