'''
find left boundary and right boundary for each height
'''
class Solution:
    def trap(self, height: List[int]) -> int:
        left_max_list = [0 for i in range(len(height))]
        left_max = 0
        for i in range(len(height)):
            if height[i] >= left_max:
                left_max = height[i]
            left_max_list[i] = left_max
        #print(left_max_list)
        
        right_max_list = [0 for i in range(len(height))]
        right_max = 0
        for i in range(len(height) - 1, -1, -1):
            if height[i] >= right_max:
                right_max = height[i]
            right_max_list[i] = right_max
        #print(right_max_list)
        
        
        res = 0
        for i in range(len(height)):
            res += min(left_max_list[i], right_max_list[i]) - height[i]
        
        return res
