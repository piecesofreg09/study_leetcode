'''
Recursive
ABCDEF = A + (BCDEF)
child problem is the (k - n)-th value in BCDEF
'''
class Solution:
    def combina(self, n):
        self.com = [0]
        multi = 1
        for i in range(1, n + 1):
            multi *= i
            self.com.append(multi)
    def get(self, nums, k):
        
        if k == 1:
            return ''.join(nums)
        
        lenn = len(nums)
        amount = self.com[lenn - 1]
        #print(amount)
        rounds = (k - 1)// amount
        #print('to skip')
        #print(rounds)
        x = nums.pop(rounds)
        #print(nums)
        #print()
        left_v = k - rounds * amount
        if left_v == 0:
            return x + "".join(nums[::-1])
        else:
            temp = self.get(nums, left_v)
            #print(temp)
        
            return x + temp
        
    def getPermutation(self, n: int, k: int) -> str:
        
        nums = [str(i) for i in range(1, n + 1)]
        self.combina(n)
        #print(self.com)
        
        result = self.get(nums, k)
        
        return result
