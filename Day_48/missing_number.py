class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
    
        dict = {}
        for num in nums:
            if num not in dict:
                dict[num] = 1
            else:
                dict[num] += 1
                return True
        return False
               
    def cotains_duplicate_faster(self,nums):
        len_nums = len(nums)
        expected = (len_nums * (le_nums +1)) //2
        actual = sum(nums)

        return expected - actual
