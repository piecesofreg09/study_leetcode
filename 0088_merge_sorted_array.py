'''
The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is equal to m + n) to hold additional elements from nums2.
Merge from end, so number of moves will be the least
'''

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        end = m + n - 1
        
        cur1 = m - 1
        cur2 = n - 1
        while cur1 >= 0 and cur2 >= 0:
            if nums1[cur1] > nums2[cur2]:
                nums1[end] = nums1[cur1]
                cur1 -= 1
                end -= 1
            else:
                nums1[end] = nums2[cur2]
                cur2 -= 1
                end -= 1
            print(nums1)
        
        if cur2 >= 0:
            nums1[:(end+1)] = nums2[:(cur2+1)]
