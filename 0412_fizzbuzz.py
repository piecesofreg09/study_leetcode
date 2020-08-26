class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = [str(i + 1) for i in range(n)]
        
        for i in range(n // 3):
            res[(i+1) * 3 - 1] = 'Fizz'
        for j in range(n // 5):
            res[(j+1) * 5 - 1] = 'Buzz'
        for k in range(n // 15):
            #print(k)
            res[(k+1) * 15 - 1] = 'FizzBuzz'
        
        return res
