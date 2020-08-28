'''
Using hash map to record lamps that are still lit up
for a lamp that is lit up, with cor (row, col)
the eigen values are row, col, row+col, row-col

if another point with cor (r, c) exists, it will be lit up if any of the four conditions is met
r = row, c = col, r+c = row+col, r-c = row-col
so keep a hash map for all possible values of row, col, row+col, row-col

also keep a number of those records
for example row=10 might be supported by lamps [10,11],[10,12],[10,15], so the count of row=10 will be 3, recorded as 10:3
if [10,11] is turned off, row=10 is still supported to lit up
'''
class Solution:
    def gridIllumination(self, N: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        #row, col, ad, sub
        lit = [{} for i in range(4)]
        lamps_hash = {}
        off = set([])
        
        for lamp in lamps:
            row = lamp[0]
            col = lamp[1]
            if (row, col) not in lamps_hash:
                lamps_hash[(row, col)] = 1
            
                t3 = row+col
                t4 = row-col
                if row in lit[0]:
                    lit[0][row] += 1
                else:
                    lit[0][row] = 1
                if col in lit[1]:
                    lit[1][col] += 1
                else:
                    lit[1][col] = 1
                if t3 in lit[2]:
                    lit[2][t3] += 1
                else:
                    lit[2][t3] = 1
                if t4 in lit[3]:
                    lit[3][t4] += 1
                else:
                    lit[3][t4] = 1
                
                
        res = []
        for query in queries:
            row = query[0]
            col = query[1]
            
            temp1 = False
            pot = [row, col, row+col, row-col]
            for idd in range(4):
                if pot[idd] in lit[idd]:
                    temp1 = True
                    break
            
            if temp1:
                res.append(1)
            else:
                res.append(0)
            
            dis = [[0,0], [-1,0], [1,0], [0,1], [0,-1], [1,1],[1,-1],[-1,1],[-1,-1]]
            
            for dx, dy in dis:
                drow = row + dx
                dcol = col + dy
                
                dt3 = drow + dcol
                dt4 = drow - dcol
                
                if (drow, dcol) in lamps_hash:
                    lamps_hash[(drow, dcol)] -= 1
                    if lamps_hash[(drow, dcol)] == 0:
                        del lamps_hash[(drow, dcol)]
                    
                    lit[0][drow] -= 1
                    if lit[0][drow] == 0:
                        del lit[0][drow]
                    
                    lit[1][dcol] -= 1
                    if lit[1][dcol] == 0:
                        del lit[1][dcol]
                    
                    lit[2][dt3] -= 1
                    if lit[2][dt3] == 0:
                        del lit[2][dt3]
                    
                    lit[3][dt4] -= 1
                    if lit[3][dt4] == 0:
                        del lit[3][dt4]
            
        
        return res
