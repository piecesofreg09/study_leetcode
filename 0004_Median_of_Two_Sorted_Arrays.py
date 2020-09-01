'''
Remove at least half of the smaller list each time.
'''
class Solution:
    
    def med_a(self, l, r):
        dev = (l + r) // 2
        if (l - r) % 2:
            return (self.nums1[dev] + self.nums1[dev + 1]) / 2
        else:
            return self.nums1[dev]
    
    def med_b(self, l, r):
        dev = (l + r) // 2
        if (l - r) % 2:
            return (self.nums2[dev] + self.nums2[dev + 1]) / 2
        else:
            return self.nums2[dev]
    
    def findMedian(self, al, ar, bl, br):
        
        #print([al, ar, bl, br])
        
        if al == ar + 1:
            self.res = self.med_b(bl, br)
            return
        if bl == br + 1:
            self.res = self.med_a(al, ar)
            return
        
        a_med = self.med_a(al, ar)
        b_med = self.med_b(bl, br)
        '''
        if al == ar and bl < br:
            dev = (bl + br) // 2
            if (br - bl) % 2:
                temp = [self.nums2[dev], self.nums2[dev + 1], self.nums1[al]]
                temp.sort()
                self.res = temp[1]
            else:
                temp = [self.nums2[dev], self.nums2[dev + 1], self.nums2[dev - 1], self.nums1[al]]
                temp.sort()
                self.res = (temp[1] + temp[2]) / 2
            return
                
        
        if bl == br and al < ar:
            #print('in here')
            dev = (al + ar) // 2
            if (ar - al) % 2:
                temp = [self.nums1[dev], self.nums1[dev + 1], self.nums2[bl]]
                temp.sort()
                self.res = temp[1]
            else:
                temp = [self.nums1[dev], self.nums1[dev + 1], self.nums1[dev - 1], self.nums2[bl]]
                temp.sort()
                self.res = (temp[1] + temp[2]) / 2
            #print(temp)
            return
        '''
        if al == ar and bl == br:
            self.res = (self.nums1[al] + self.nums2[bl]) / 2
            return
        
        if ar - al < 2:
            if br - bl < 2:
                temp = self.nums1[al:(ar+1)] + self.nums2[bl:(br+1)]
                temp.sort()
                #print(temp)
                if len(temp) % 2 == 0:
                    self.res = (temp[len(temp) // 2] + temp[len(temp) // 2 - 1]) / 2
                else:
                    self.res = temp[len(temp) // 2]
                return
            else:
                if self.nums1[al] < self.nums2[bl]:
                    al += 1
                else:
                    bl += 1
                if self.nums1[ar] < self.nums2[br]:
                    br -= 1
                else:
                    ar -= 1
                    
                self.findMedian(al, ar, bl, br)
                return
                
                    
        elif br - bl < 2:
            if self.nums1[al] < self.nums2[bl]:
                al += 1
            else:
                bl += 1
            if self.nums1[ar] < self.nums2[br]:
                br -= 1
            else:
                ar -= 1
            self.findMedian(al, ar, bl, br)
            return
        
        
        if a_med == b_med:
            self.res = a_med
        elif a_med > b_med:
            rm = min((ar - al) // 2, (br - bl) //2)
            self.findMedian(al, ar - rm, bl + rm, br)
        else:
            rm = min((ar - al) // 2, (br - bl) //2)
            self.findMedian(al + rm, ar, bl, br - rm)
        
        return
        
    
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        self.nums1 = nums1
        self.nums2 = nums2
        
        if len(self.nums1) == 0:
            return self.med_b(0, len(self.nums2) - 1)
        if len(self.nums2) == 0:
            return self.med_a(0, len(self.nums1) - 1)
        
        self.findMedian(0, len(self.nums1) - 1, 0, len(self.nums2) - 1)
        
        return self.res
