'''
a b
a = a ^ b
b = (a & b) << 1
a + b = (a^b) + (a&b)<<1
until b is zero, a will be equal to a + b
if b overflows, apply mask on a
is b = 0xffffffff + 1
then a will be super negative, apply a mask on a will make it correct
'''
class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xffffffff
        while (b & mask) != 0:
            carry = (a & b) << 1
            a = (a ^ b)
            b = carry
        print(b)
        print(a)
        return a & mask if b > 0 else a
