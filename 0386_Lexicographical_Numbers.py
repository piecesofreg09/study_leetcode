'''
dfs search
if 1 is searched, next should be 10 - 19
if 100 is searched, next should be 1000 - 1009
'''
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res = []
        def dfs(x):
            if x <= n:
                res.append(x)
            for digit in range(10):
                if x*10 + digit <= n:
                    dfs(x*10 + digit)
        
        for i in range(1, 10):
            dfs(i)
        
        return res
