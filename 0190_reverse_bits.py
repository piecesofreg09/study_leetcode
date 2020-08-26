'''
The only difference between the two solutions:
<< n or 2 ** n
<< is much faster
'''

class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        power = 31
        for i in range(32):
            temp = n % 2
            if temp:
                res += temp * 1 << (31 - i)
            n = n >> 1
        
        return res

class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            temp = n % 2
            if temp:
                res += temp * 2 ** (31 - i)
            n = n >> 1
        
        return res
