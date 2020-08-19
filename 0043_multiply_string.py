class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        x = [int(i) for i in num1][::-1]
        #print(x)
        y = [int(i) for i in num2][::-1]
        #print(y)
        
        res = [0 for i in range(len(x) + len(y))]
        
        for idi, i in enumerate(x):
            for idj, j in enumerate(y):
                res[idi + idj] += i * j
        
        #print(res)
        
        
        for i in range(len(res) - 1):
            ten = res[i] // 10
            ge = res[i] % 10
            res[i] = ge
            res[i + 1] += ten
        
        #print(res)
        
        pos = len(res)
        while res[pos - 1] == 0 and pos > 0:
            pos -= 1
        
        if pos == 0:
            return "0"
        
        rest = "".join([str(i) for i in res[:pos]][::-1])
        
        #print(rest)
        return rest
