'''
DFS
'''
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        if not node:
            return None
        
        nodeini = Node(val=node.val)
        self.created = {}
        self.cloneGraphMini(node, nodeini)
        
        return nodeini
    
    def cloneGraphMini(self, nodeori, nodecopied):
        #print(nodecopied.val)
        neis = []
        self.created[nodeori.val] = nodecopied
        for neighbor in nodeori.neighbors:
            
            if neighbor.val not in self.created:
                nodenew = Node(val=neighbor.val)
                self.cloneGraphMini(neighbor, nodenew)
            else:
                nodenew = self.created[neighbor.val]
                
            neis.append(nodenew)
        
        nodecopied.neighbors = neis
