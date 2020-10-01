'''
Input:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

Output:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]

sort by the height first
insert the people by their height, if m people is inserted, the (m+1)-th person is definitely shorter than all m people
if the data is [5, 2], it means there should be 2 people taller than him
the correct position should be the 2-th position in the existing queue
with the same height, the people that have less tall people in front of him/her should be inserted first

'''
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        if len(people) == 0:
            return []
        peo = sorted(people, key=lambda x: [-x[0], x[1]])
        res = []
        for p in peo:
            res.insert(p[1], p)
        
        return res
