'''
F(k) = F(k-1) + totalsum - n * A[n-k]
'''
class Solution:
    def maxRotateFunction(self, A: List[int]) -> int:
        orisum = sum([i * n for i, n in enumerate(A)])
        total = sum(A)
        n = len(A)
        res = orisum
        cur = res
        for num in A[:-1]:
            cur = cur - total + n * num
            res = max(cur, res)
        
        return res
