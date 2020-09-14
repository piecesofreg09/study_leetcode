'''
Original thoughts
'''
class Solution:
    def findNthDigit(self, n: int) -> int:
        digit = 1
        first = 9
        count = 0
        pre = 0
        base = 1
        
        
        while count + first * digit < n:
            pre = count
            count += first * digit
            first *= 10
            digit += 1
            base *= 10
            #print([pre, count, first, digit, base])
        
        pre = count
        
        remainder = (n - pre)
        
        numbers_in = remainder //  digit
        number_pos = remainder % digit
        
        if number_pos > 0:
            return str(base + numbers_in)[number_pos - 1]
        else:
            return str(base + numbers_in - 1)[-1]


'''
Improved version
'''
class Solution:
    def findNthDigit(self, n: int) -> int:
        digit = 1
        #first = 9
        count = 0
        base = 1
        
        pro = base * digit * 9
        while count + pro < n:
            count += pro
            digit += 1
            base *= 10
            pro = base * digit * 9
            #print([pre, count, first, digit, base])
        
        numbers_in = (n - count) //  digit
        number_pos = (n - count) % digit
        
        if number_pos > 0:
            return str(base + numbers_in)[number_pos - 1]
        else:
            return str(base + numbers_in - 1)[-1]
