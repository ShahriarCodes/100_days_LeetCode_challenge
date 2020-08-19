class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """


if __name__ == '__main__':

    nums = [1,3,5,6]
    target = 5
    instance = Solution()
    solution = instance.searchInsert(nums, target)

    print(solution)
