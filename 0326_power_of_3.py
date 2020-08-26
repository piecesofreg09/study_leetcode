'''
using mathematics: logn(x) = logm(n)/logm(x)
'''
import math
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        
        temp = math.log(n) / math.log(3)
        if (temp + 1e-10) % 1 <= 2 * 1e-10:
            return True
        return False

'''
keep dividing 3
'''
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 0:
            return False
        while n != 1:
            temp = n % 3
            if temp:
                return False
            n = n // 3
        
        return True
