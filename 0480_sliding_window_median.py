'''
Using two heaps, to keep track of the center item
'''
import heapq, math

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        if k == 1:
            return nums
        res = []
        temp = sorted(nums[:k])
        med = temp[math.floor((k-1)/2)] / 2 + temp[math.ceil((k-1)/2)] / 2
        res.append(med)
        #print(temp)
        #print(med)
        
        self.left = [-i for i in temp[:(k//2)]]
        self.right = temp[(k//2):]
        #print(self.left)
        #print(self.right)
        
        heapq.heapify(self.left)
        heapq.heapify(self.right)
        
        if k % 2:
            
            for i in range(1, len(nums) - k + 1):
                cur = nums[i + k - 1]
                #print(nums[i - 1])
                # if in left heap
                
                if -nums[i - 1] in self.left:
                    idd = self.left.index(-nums[i - 1])
                    self.left.pop(idd)
                    heapq.heapify(self.left)
                    if cur < self.right[0]:
                        heapq.heappush(self.left, -cur)
                    else:
                        rightmin = heapq.heappop(self.right)
                        heapq.heappush(self.left, -rightmin)
                        heapq.heappush(self.right, cur)
                    res.append(self.right[0])
                    continue        
                
                # if in right heap
                idd = self.right.index(nums[i - 1])
                self.right.pop(idd)
                heapq.heapify(self.right)
                if cur < -self.left[0]:
                    leftmax = -heapq.heappop(self.left)
                    heapq.heappush(self.right, leftmax)
                    heapq.heappush(self.left, -cur)
                else:
                    heapq.heappush(self.right, cur)
                res.append(self.right[0])
                
        else:
            for i in range(1, len(nums) - k + 1):
                cur = nums[i + k - 1]
                # if in left heap
                if -nums[i - 1] in self.left:
                    idd = self.left.index(-nums[i - 1])
                    self.left.pop(idd)
                    heapq.heapify(self.left)
                    if cur < self.right[0]:
                        heapq.heappush(self.left, -cur)
                    else:
                        rightmin = heapq.heappop(self.right)
                        heapq.heappush(self.left, -rightmin)
                        heapq.heappush(self.right, cur)
                    res.append(self.right[0] / 2 - self.left[0] / 2)
                    continue        
                
                # if in right heap
                idd = self.right.index(nums[i - 1])
                self.right.pop(idd)
                heapq.heapify(self.right)
                if cur < -self.left[0]:
                    leftmax = -heapq.heappop(self.left)
                    heapq.heappush(self.right, leftmax)
                    heapq.heappush(self.left, -cur)
                else:
                    heapq.heappush(self.right, cur)
                res.append(self.right[0] / 2 - self.left[0] / 2)
        
        return res
            
