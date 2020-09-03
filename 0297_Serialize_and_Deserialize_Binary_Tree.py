# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        stack = [root]
        res = []
        
        while stack:
            length = len(stack)
            for node in stack:
                if node:
                    res.append(node.val)
                    stack.append(node.left)
                    stack.append(node.right)
                else:
                    res.append(None)
            stack = stack[length:]
            #print(res)
            return ",".join([str(item) for item in res])

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        #print(data)
        li = data.split(',')
        
        if li[0] == 'None':
            return None
        
        root = TreeNode(int(li[0]))
        
        parent_layer_num = 1
        cur = 1
        li[0] = root
        parent_layer = [root]
        while parent_layer_num > 0:
            #print(cur)
            #print(parent_layer_num)
            child_layer_num = 0
            child_layer = []
            for idd in range(parent_layer_num):
                if li[cur + idd * 2] != 'None':
                    node = TreeNode(int(li[cur + idd * 2]))
                    child_layer_num += 1
                    parent_layer[idd].left = node
                    child_layer.append(node)
                if li[cur + idd * 2 + 1] != 'None':
                    node = TreeNode(int(li[cur + idd * 2 + 1]))
                    #print(node)
                    child_layer_num += 1
                    parent_layer[idd].right = node
                    child_layer.append(node)
            cur += parent_layer_num * 2
            parent_layer_num = child_layer_num
            parent_layer = [node for node in child_layer]
        
        return root
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
