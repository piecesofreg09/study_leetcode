'''
for one interval sum, use kadane

for two interval sum,

sum = sumleft + sumright

sumleft is prefix sum
sumright is max post fix sum, where sumright[i] >= sumright[i+1] >= sumright[i+2]...
sumright[i] is the maximum sum of any subarray starts after i and ends at the array end.

'''
class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        res = A[0]
        cur = A[0]
        
        for num in A[1:]:
            cur = num + max(0, cur)
            res = max(cur, res)
        
        presum = [0 for i in range(len(A))]
        accu = 0
        for i in range(len(A)):
            accu += A[i]
            presum[i] = accu
        
        
        postsum = [0 for i in range(len(A))]
        postsum[-1] = A[-1]
        accu = A[-1]
        for i in range(len(A) - 2, -1, -1):
            accu += A[i]
            postsum[i] = max(postsum[i + 1], accu)
        
        
        for i in range(0, len(A) - 2):
            res = max(presum[i] + postsum[i + 2], res)
            
        
        
        return res
            
  
 
 '''
 use three Kadane's algo
 
 for one interval sum, use kadane
 
 for two interval sum, sum = sum(all) - min(sub_sum)
 -min(sub_sum) equals to max(sub_sum)
 
 '''
 class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        res = A[0]
        cur = A[0]
        sumn = sum(A)
        
        
        for num in A[1:]:
            cur = num + max(0, cur)
            res = max(cur, res)
        
        if len(A) >= 2:
            mincur = -A[1]
            minres = -A[1]
            for num in A[2:]:
                mincur = -num + max(0, mincur)
                minres = max(minres, mincur)
                
            res = max(res, sumn + minres)
            
            mincur = -A[0]
            minres = -A[0]
            for num in A[1:(len(A)-1)]:
                mincur = -num + max(0, mincur)
                minres = max(minres, mincur)
                
            res = max(res, sumn + minres)
        
        return res
            
 
 
