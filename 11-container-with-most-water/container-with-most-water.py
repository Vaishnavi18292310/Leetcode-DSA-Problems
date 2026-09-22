class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        #Using two pointer approach
        n=len(height)
        max_water=0
        left_p=0
        right_p=n-1

        while(left_p<right_p):
            width=abs(left_p-right_p)
            h=min(height[left_p],height[right_p])
            curr_water=width*h
            max_water=max(max_water,curr_water)

            if (height[left_p]<height[right_p]):
                left_p+=1
            else:
                right_p-=1

        return max_water







        # #brute force
        # max_water=0
        # for i in range(len(height)):
        #     for j in range(i+1,len(height)):
        #         width=j-i
        #         h=min(height[i],height[j])
        #         current_water=width*h
        #         max_water=max(current_water,max_water)
        # return max_water



