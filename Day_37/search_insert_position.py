class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        len_num = len(nums)
        for i, num in enumerate(nums):
            if nums[i] > target:
                return i
            if num == target:
                return i

        if target > nums[len_num-1]:
            return len_num
            


if __name__ == '__main__':

    nums = [1,3,5,6]
    target = 7
    instance = Solution()
    solution = instance.searchInsert(nums, target)

    print(solution)
