class Solution(object):
    def isUgly(self, n):
        """
        :type n: int
        :rtype: bool
        """
        prime_factors=[2,3,5]
        if n<=0:
            return False
        
        for i in prime_factors:
            while n%i==0:
                n=n//i
        return n==1
                
        