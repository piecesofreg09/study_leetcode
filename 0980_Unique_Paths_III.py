'''
backtrack
try with initial starting point
then treat each point as initial point
if the trail run into itself or it's an obstacle then stop and retrace back
mark visited along way, until all ways are visited
backtrack needs to return back to original state
'''

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        rown, coln = len(grid), len(grid[0])
        non_obs = 0
        startr = 0
        startc = 0
        
        for row in range(rown):
            for col in range(coln):
                c = grid[row][col]
                if c >= 0:
                    non_obs += 1
                if c == 1:
                    startr = row
                    startc = col
        
        res_count = 0
        
        def backtrack(row, col, remain):
            nonlocal res_count
            
            if grid[row][col] == 2 and remain == 1:
                res_count += 1
                return
            
            temp = grid[row][col]
            grid[row][col] = -4
            remain -= 1
            
            disp = [[0,1],[0,-1],[1,0],[-1,0]]
            
            for x, y in disp:
                nextr = row + x
                nextc = col + y
                
                if not ( 0<= nextr < rown and 0<= nextc < coln):
                    continue
                if grid[nextr][nextc] < 0:
                    # either an obstacle or already visited
                    continue
                backtrack(nextr, nextc, remain)
            grid[row][col] = temp
        
        backtrack(startr, startc, non_obs)
        
        return res_count
