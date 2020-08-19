'''
mono stack 
left boundary and right boundary
'''
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        n = len(heights)
        
        left = [0 for i in range(n)]
        right = [n for i in range(n)]
        
        left_stack = []
        for i in range(n):
            while left_stack and heights[i] <= heights[left_stack[-1] - 1]:
                left_stack.pop()
            left[i] = left_stack[-1] if left_stack else 0
            left_stack.append(i + 1)
            
        
        right_stack = []
        for i in range(n - 1, -1, -1):
            while right_stack and heights[i] <= heights[right_stack[-1]]:
                right_stack.pop()
            right[i] = right_stack[-1] if right_stack else n
            right_stack.append(i)
            
        res = 0
        for i in range(n):
            temp = heights[i] * (right[i] - left[i])
            if temp > res:
                res = temp
        
        return res
            
