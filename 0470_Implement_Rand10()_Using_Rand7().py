# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        ran1 = rand7()
        while ran1 > 5:
            ran1 = rand7()
        
        ran2 = rand7()
        while ran2 == 7:
            ran2 = rand7()
        
        if ran2 % 2 == 0:
            return ran1
        else:
            return ran1 + 5
