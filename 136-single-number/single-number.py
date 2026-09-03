class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        xor=0
        for i in range(n):
            xor=xor^nums[i]
        return xor

        