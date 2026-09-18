class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        resultlist=[]

        self.backtrack(resultlist,[],nums)

        return resultlist
    

    def backtrack(self,resultlist,templist,nums):
        #Base condition
        if len(templist)==len(nums):
            resultlist.append(templist[:])
            return

        for num in nums:
            #If number is already in temporary list, we will just skip and move to nxt number
            if num in templist:
                continue
            
            #if not in temporary list, will add it
            templist.append(num)

            self.backtrack(resultlist,templist,nums)

            templist.pop()
            



