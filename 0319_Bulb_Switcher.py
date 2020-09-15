'''
math.floor(math.sqrt(n))
'''
class Solution:
    def bulbSwitch(self, n: int) -> int:
        res = 1
        
        while res ** 2 <= n:
            res += 1
        
        return res - 1
        
