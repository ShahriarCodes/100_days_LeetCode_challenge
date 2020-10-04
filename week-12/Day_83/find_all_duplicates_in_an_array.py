class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output = []
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            if nums[index] < 0:
                output.append(index + 1)
            
            nums[index] = - nums[index]
                
        return output

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        if len(nums) < 2:
            return []

        nums = sorted(nums)
        prev_num = nums[0]
        output = []
        for i in range(1, len(nums)):
            if nums[i] == prev_num:
                output.append(nums[i])
            elif nums[i] != prev_num:
                prev_num = nums[i]
        return output
