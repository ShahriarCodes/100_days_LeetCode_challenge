class Solution:
    def search(self, nums: List[int], target: int) -> int:
        s = 0
        e = len(nums) - 1
        while s<=e:
            m  = (s + e)//2
            if nums[m] == target:
                return m
            # part1 = nums[s:m-1]
            # part2 = nums[s:m+1]
            if target < nums[m]:
                e = m-1
            elif target > nums[m]:
                s = m+1
        return -1   
    
