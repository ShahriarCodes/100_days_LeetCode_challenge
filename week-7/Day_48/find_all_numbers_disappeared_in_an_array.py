class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        len_nums = len(nums)
        
        if len(nums) == 0:
            return []
        set_nums =  set(nums)
       
        return [i for i in range(1, len_nums+1) if i not in set_nums]
