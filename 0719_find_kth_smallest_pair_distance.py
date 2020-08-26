'''
binary search
count number of pairs that is bigger than the guess, set it as n, return n >= k
shrink down the choices of guess
'''
class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        
        def pos(guess):
            count = 0
            left = 0
            for right, num in enumerate(nums):
                while num - nums[left] > guess:
                    left += 1
                count += right - left
            
            return count >= k
        
        nums.sort()
        lo = 0
        hi = nums[-1] - nums[0]
        while lo < hi:
            mi = (lo + hi) // 2
            if pos(mi):
                hi = mi
            else:
                lo = mi + 1
        
        return lo

'''
finding all pairs, Time Limit Exceeded
'''
class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        
        dict_count = {}
        
        for num in nums:
            if num in dict_count:
                dict_count[num] += 1
            else:
                dict_count[num] = 1
        
        distinct_nums = set(dict_count)
        if len(distinct_nums) == 1:
            return 0
        
        N = len(distinct_nums)
        n_groups = int(((len(nums) ** 2) / (2 * k + len(nums))) // 1)
        #print(n_groups)
        
        min_v = min(distinct_nums)
        max_v = max(distinct_nums)
        dis = (max_v - min_v) // n_groups + 1
        #print(dis)
        
        temp = [[] for i in range(n_groups)]
        
        for num in distinct_nums:
            idd = (num - min_v) // dis
            temp[idd].append(num)
        
        #print(temp)
        res = {0:0}
        for num, count in dict_count.items():
            res[0] += int(count * (count - 1) / 2)
            
        for group in temp:
            group.sort()
            #print(group)
            for idd, n1 in enumerate(group[:-1]):
                for n2 in group[(idd + 1):]:
                    if (n2 - n1) in res:
                        res[n2 - n1] += dict_count[n1] * dict_count[n2]
                    else:
                        res[n2 - n1] = dict_count[n1] * dict_count[n2]
        
        for idd in range(len(temp) - 1):
            group1 = temp[idd]
            group2 = temp[idd + 1]
            for n1 in group1:
                for n2 in group2:
                    if (n2 - n1) <= dis:
                        if (n2 - n1) in res:
                            res[n2 - n1] += dict_count[n1] * dict_count[n2]
                        else:
                            res[n2 - n1] = dict_count[n1] * dict_count[n2]
        #print(res)
        x = sorted(res.items(), key=lambda t:t[0])
        #print(x)
        res = 0
        for key, count in x:
            res += count
            if res >= k:
                return key
