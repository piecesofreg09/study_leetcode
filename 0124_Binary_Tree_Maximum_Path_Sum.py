'''
current node has three components to form sum
largest from parent, largest from left child, largest from right child
if the results can be labelled as m1, m2, m3 (sorting from minimum to maximum)

then the max can only be
max(node.val, node.val + m3, node.val + m3 + m2, current_res)

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def maxPath(self, root, parentmax):
        
        
        parentmax_cur = max(0, parentmax) + root.val
        
        leftmax = 0
        rightmax = 0
        
        if root.left:
            leftleft, leftright = self.maxPath(root.left, parentmax_cur)
            leftmax = max(0, leftleft, leftright) + root.left.val
        if root.right:
            rightleft, rightright = self.maxPath(root.right, parentmax_cur)
            rightmax = max(0, rightleft, rightright) + root.right.val
        
        m1, m2, m3 = sorted([parentmax, leftmax, rightmax])
        
        self.res = max(self.res, root.val + m2 + m3, root.val + m3, root.val)
        
        return [leftmax, rightmax]
        
    
    def maxPathSum(self, root: TreeNode) -> int:
        
        self.res = -float('inf')
        
        self.maxPath(root, 0)
        
        return self.res
