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

#slightly changed 
class Solution:
    def findDuplicate(self, nums):
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return nums[i]

#using hash table, runtime updated, space degraded
class Solution:
    def findDuplicate(self, nums):
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)

#slow, fast pointer approach --- floyds cycle detection algorithm
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow = nums[0]
        fast = nums[0]

        slow = nums[slow]
        fast = nums[nums[fast]]

        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return fast
