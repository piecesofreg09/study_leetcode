# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        
        nodetd = None
        stack = [(root, None, None)]
        if not root:
            return root
        while stack:
            #print(stack)
            count = len(stack)
            out = False
            for node, parent, dirr in stack:
                if node.val == key:
                    nodetd = node
                    nodeparent = parent
                    dirt = dirr
                    out = True
                    break
                else:
                    if node.left:
                        stack.append((node.left, node, 'left'))
                    if node.right:
                        stack.append((node.right, node, 'right'))
            if out:
                break
            stack = stack[count:]
        if nodetd:
            print(nodetd)
            if not nodetd.left and not nodetd.right:
                if not parent:
                    return None
                else:
                    if dirt == 'left':
                        parent.left = None
                    else:
                        parent.right = None
                return root
            
            if not nodetd.left:
                if not parent:
                    return nodetd.right
                else:
                    if dirt == 'left':
                        parent.left = nodetd.right
                    else:
                        parent.right = nodetd.right
                return root
            
            if not nodetd.right:
                if not parent:
                    return nodetd.left
                else:
                    if dirt == 'left':
                        parent.left = nodetd.left
                    else:
                        parent.right = nodetd.left
                return root
            
            if nodetd.left and nodetd.right:
                leftmostparent = nodetd.right
                leftmost = nodetd.right.left
                while leftmost:
                    leftmostparent = leftmost
                    leftmost = leftmost.left
                
                leftmostparent.left = nodetd.left.right
                nodetd.left.right = nodetd.right
                if not parent:
                    return nodetd.left
                if dirt == 'left':
                    parent.left = nodetd.left
                else:
                    parent.right = nodetd.left
                    
                        
        
        return root
