'''
Using stacks to do bfs traversal
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        stack = [root]
        
        res = []
        odd = True
        while stack:
            templen = len(stack)
            temp = []
            for i in range(templen):
                temp.append(stack[i].val)
                if stack[i].left:
                    stack.append(stack[i].left)
                if stack[i].right:
                    stack.append(stack[i].right)
            res.append(temp[:] if odd else temp[::-1])
            odd = not odd
            stack = stack[templen:]
        
        return res
