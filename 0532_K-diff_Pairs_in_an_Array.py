'''
Use hashmap to count
consider special case of k == 0
'''
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        hashmap = {}
        for num in nums:
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1
        result = 0
        if k == 0:
            for num, k in hashmap.items():
                if k > 1:
                    result += 1
            return result
        else:
            #print(hashmap)
            for num, _ in hashmap.items():
                if (num + k) in hashmap:
                    result += 1
                if (num - k) in hashmap:
                    result += 1
            
            return int(result // 2)
