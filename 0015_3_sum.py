'''
use hash map (dict) to speed up single value lookup
go through all possible two value pairs
'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        dict_list = {}
        for i in nums:
            if i in dict_list:
                dict_list[i] += 1
            else:
                dict_list[i] = 1
        #print(dict_list)
        nums.sort()
        
        res = []
        res_tuple = {}
        for i in range(len(nums) - 2):
            if nums[i] > 0:
                break
            for j in range(i + 1, len(nums) - 1):
                
                sub = 0 - nums[i] - nums[j]
                
                if sub in dict_list:
                    
                    if len(res) == 0:
                        if sub == nums[i]:
                            dict_list[sub] -= 1
                        if sub == nums[j]:
                            dict_list[sub] -= 1
                        if dict_list[sub] > 0:
                            temp = sorted([nums[i], nums[j], sub])
                            temp_tuple = tuple(temp)
                            res_tuple[temp_tuple] = True
                            res.append(temp)
                        
                    else:
                        
                        if sub == nums[i]:
                            dict_list[sub] -= 1
                        if sub == nums[j]:
                            dict_list[sub] -= 1
                        if dict_list[sub] > 0:
                            temp = sorted([nums[i], nums[j], sub])
                            temp_tuple = tuple(temp)
                            if temp_tuple not in res_tuple:
                                res_tuple[temp_tuple] = True
                                res.append(temp)
                            
        
        return res
                
