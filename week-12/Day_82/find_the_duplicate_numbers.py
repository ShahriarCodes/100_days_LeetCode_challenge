class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums = sorted(nums)
        count = 1
        max_count = 0
        prev_num = nums[0]
        
        for i in range(1, len(nums)):
            if nums[i] == prev_num:
                count += 1
                prev_num = nums[i]
            if nums[i] != prev_num:
                count = 1
                prev_num = nums[i]
                
            if count > max_count:
                output = nums[i]
                max_count = count
        
        return output
