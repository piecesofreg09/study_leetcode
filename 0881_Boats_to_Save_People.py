'''
sort first
pair from both ends, because there is a limit of 2 on each boat 
'''
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        
        left = 0
        right = len(people) -1
        res = 0
        
        while left <= right:
            res += 1
            if people[left] + people[right] <= limit:
                left += 1
            right -= 1
        
        return res
