'''
Remove leaves until there is no more than 2 nodes
'''
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        adj = {}
        for inn, out in edges:
            if inn in adj:
                adj[inn].add(out)
            else:
                adj[inn] = {out}
            
            if out in adj:
                adj[out].add(inn)
            else:
                adj[out] = {inn}
        
        #print(adj)
        
        while len(adj) > 2:
            
            temp = []
            for inn in adj:
                if len(adj[inn]) == 1:
                    temp.append(inn)
            #print(temp)
            for rem in temp:
                node = adj[rem].pop()
                adj[node].remove(rem)
                del adj[rem]
            #print(adj)
        
        return list(adj.keys())
