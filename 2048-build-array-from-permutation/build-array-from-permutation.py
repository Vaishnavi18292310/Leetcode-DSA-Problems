class Solution(object):
    def buildArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        # ans=[]

        # for i in range(len(nums)):
        #     ans.append(nums[nums[i]])
        # return ans

        ans=[i for i in range(len(nums))]
        for i in range(len(nums)):
            ans[i] = nums[nums[i]]
        return ans


