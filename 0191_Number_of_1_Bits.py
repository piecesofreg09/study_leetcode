'''
n & n - 1 will remove the rightmost 1 to be 0
'''

class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n != 0:
            count += 1
            n = n & n - 1
        
        return count
