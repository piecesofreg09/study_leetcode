class Solution:
    def com(self, li, k):
        if k == 1:
            return [[i] for i in li]
        res = []
        for i in range(len(li)):
            temp = li[:i]
            longli = self.com(temp, k - 1)
            for j in longli:
                res.append(j+[li[i]])
        
        return res
            
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = self.com(list(range(1, n+1)), k)
        
        return res
