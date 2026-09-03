class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        ans=0
        for bitindex in range(32):
            count=0
            for num in nums:
                if num &(1<<bitindex):
                    count+=1
            if(count%3==1):
                ans=ans | (1<<bitindex)
        #handle negative values
        if ans>=2**31:
            ans-=2**32
        return ans

        