'''
for each node
go for its deepest left and deepest right
if leftcount == rightcount, then this node is a perfect complete binary tree, in this case the count would be
(1 << count) - 1

if leftcount != rightcount, then recursively count again for left child and right child

Note:
a leaf is a perfect complete binary tree, with count as 1, the return result is (1 << 1) - 1 = 2 - 1 = 1

'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        
        def dfs(root):
            if not root:
                return 0
            
            left = root.left
            countleft = 1
            while left:
                left = left.left
                countleft += 1
            
            right = root.right
            countright = 1
            while right:
                right = right.right
                countright += 1
            
            if countleft == countright:
                return (1 << countleft) - 1
            else:
                xleft = dfs(root.left)
                xright = dfs(root.right)
                
                return xleft + xright + 1
        
        res = dfs(root)
        
        return res
