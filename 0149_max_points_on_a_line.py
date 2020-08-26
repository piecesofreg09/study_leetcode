'''
Using slope and intersection point as flags, i.e. (slope, intersection)
remember duplicates in a hash map
using set to update points with a certain pair of (slope, intersection)
'''

import math
from decimal import getcontext, Decimal
getcontext().prec = 30
class Solution:
    def maxPoints(self, pointsori: List[List[int]]) -> int:
        
        points_dict = {}
        for point in pointsori:
            if tuple(point) in points_dict:
                points_dict[tuple(point)] += 1
            else:
                points_dict[tuple(point)] = 1
        #print(points_dict)
        points = list(points_dict)
        
        if not points:
            return 0
        if len(points) == 1:
            return points_dict[points[0]]
        hash_dict = {}
        for i in range(len(points)):
            for j in range(i):
                x1, y1 = points[i]
                x2, y2 = points[j]
                if x1 == x2:
                    a = float('inf')
                    b = x1
                else:
                    a = Decimal(y1-y2)/Decimal(x1-x2)
                    b = Decimal(y2*x1-y1*x2)/Decimal(x1-x2)
                temp = (a, b) 
                if temp in hash_dict:
                    hash_dict[temp].add(points[i])
                    hash_dict[temp].add(points[j])
                else:
                    hash_dict[temp] = {points[i], points[j]}
        #print(hash_dict)
        res = {}
        for loc, points in hash_dict.items():
            temp = 0
            for point in points:
                temp += points_dict[point]
            res[loc] = temp
        #print(res)
        res = sorted(res.items(), key=lambda x:x[1], reverse=True)
        count = res[0][1]
        
        return count
