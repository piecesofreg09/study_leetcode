'''
two candidates
increase the counter when the candidate is matched
update the candidate when counter is 0
if no match: decrease values
'''
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count1 = 0
        count2 = 0
        candi1 = None
        candi2 = None
        
        for num in nums:
            if candi1 == num:
                count1 += 1
                continue
            if candi2 == num:
                count2 += 1
                continue
                
            if count1 == 0:
                candi1 = num
                count1 = 1
                continue
            
            if count2 == 0:
                candi2 = num
                count2 = 1
                continue
                
            count1 -= 1
            count2 -= 1
        
        res = set([candi1, candi2])
        r = []
        for pot in list(res):
            count = 0
            for num in nums:
                if pot == num:
                    count += 1
            if count > len(nums) // 3:
                r.append(pot)
        
        return r
