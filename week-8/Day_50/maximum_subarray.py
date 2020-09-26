class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ### kadane's Algorithm 
        max_so_far = nums[0]
        max_ending_here = 0
        
        (start, end, s) = (0, 0, 0)
        
        for i in range(len(nums)):
            max_ending_here += nums[i]
            
            if max_so_far < max_ending_here:
                max_so_far = max_ending_here
                start = s
                end = i
            
            if max_ending_here < 0:
                max_ending_here = 0
                s = i+1
        
        return max_so_far
                
if __name__  == '__main__':
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    instance = Solution()
    print(instance.maxSubArray(nums))
            
            
            
            
            
            
         
