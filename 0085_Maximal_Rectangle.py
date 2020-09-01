'''
mono stack
'''
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        
        if not matrix:
            return 0
        
        width = len(matrix[0])
        height = len(matrix)
        heights = [0 for i in range(width)]
        
        res = 0
        for i in range(height):
            for j in range(width):
                if matrix[i][j] == '1':
                    heights[j] += 1
                else:
                    heights[j] = 0
            
            #print(heights)
            
            left = [0 for i in range(width)]
            left_stack = []
            for it in range(0, width):
                while left_stack and heights[it] <= heights[left_stack[-1] - 1]:
                    left_stack.pop()
                left[it] = left_stack[-1] if left_stack else 0
                left_stack.append(it + 1)
            #print(left)    
            
            right = [width for i in range(width)]
            right_stack = []
            for it in range(width -1, -1, -1):
                while right_stack and heights[it] <= heights[right_stack[-1]]:
                    right_stack.pop()
                right[it] = right_stack[-1] if right_stack else width
                right_stack.append(it)
            #print(right)
            
            #print()
            for it in range(width):
                temp = heights[it] * (right[it] - left[it])
                if temp > res:
                    res = temp
        
        return res
            
            
            
