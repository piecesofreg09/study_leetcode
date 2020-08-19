'''
move lower boundary inward
calculate current area to update max are
'''

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        
        current_max = 0
        
        while right != left:
            if height[left] < height[right]:
                area = height[left] * (right - left)
                if area > current_max:
                    current_max = area
                left += 1
            else:
                area = height[right] * (right - left)
                if area > current_max:
                    current_max = area
                right -= 1
            
        return current_max
