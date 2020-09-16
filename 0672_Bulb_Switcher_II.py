'''
simulate
'''
class Solution:
    def flipLights(self, n: int, m: int) -> int:
        n = min(n, 6)
        ini = sum([1 << i for i in range(n)])
        #print(bin(ini))
        
        opt1 = ini
        opt2 = sum([1 << i for i in range(0, n, 2)])
        opt3 = sum([1 << i for i in range(1, n, 2)])
        opt4 = sum([1 << i for i in range(0, n, 3)])
        #print(bin(opt1))
        #print(bin(opt2))
        #print(bin(opt3))
        #print(bin(opt4))
        opts = [opt1, opt2, opt3, opt4]
        if m == 0:
            return 1
        res0 = {ini}
        temp = set()
        for opt in opts:
            temp = temp | {t ^ opt for t in res0}
            
        res = {i for i in temp}
        #print([bin(i) for i in res])
        for round in range(1, m):
            temp = set()
            for opt in opts:
                #print({bin(t ^ opt) for t in res})
                temp = temp | {t ^ opt for t in res}
            res = temp
            #print([bin(i) for i in res])
        
        return len(res)

'''
Maths
'''
class Solution:
    def flipLights(self, n: int, m: int) -> int:
        n = min(n, 3)
        if m == 0:
            return 1
        if m == 1:
            res = [2, 3, 4]
        elif m == 2:
            res = [2, 4, 7]
        else:
            res = [2, 4, 8]
        return res[n - 1]
