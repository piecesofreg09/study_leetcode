'''
Using bisect model
find the location is the most important step
using binary search the search can be done in log(n) time
'''

import bisect

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        res = []
        
        right = []
        
        for i in range(len(nums) - 1, -1, -1):
            num = nums[i]
            loc = bisect.bisect_left(right, num)
            res.append(loc)
            right.insert(loc, num)
            #print(right)
        
        return res[::-1]

    

'''
self-implemented binary search
'''
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        res = []
        
        right = []
        
        def search(li, num):
            if len(li) == 0:
                return 0
            
            left = 0
            right = len(li) - 1
            
            while left <= right:
                med = (left + right) // 2
                
                if num <= li[med]:
                    if med == 0:
                        #print('here')
                        return med
                    else:
                        right = med - 1
                else:
                    if med == len(li) - 1:
                        #print('heereeeee')
                        return med + 1
                    elif li[med + 1] >= num:
                        return med + 1
                    else:
                        left = med + 1
        
        for i in range(len(nums) - 1, -1, -1):
            #print(right)
            num = nums[i]
            #print(num)
            #loc = bisect.bisect_left(right, num)
            loc1 = search(right, num)
            #print(loc)
            #print(loc1)
            res.append(loc1)
            right.insert(loc1, num)
            #print(right)
        
        return res[::-1]
