class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lst = []
        index = []
        #check if ith num is greater than the following num
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1] :
                lst.append(nums[i])
                index.append(i)

        # if len(lst) > 0:
        #     length = lst[-1] - lst[0] + 2
        # else:
        #     length  = 0

        return  lst, index


if __name__ == '__main__':

    nums = [2,6,4,8,10,9,9]
    nums = [1,3,2,2,2]
    nums = [4,2,2,2,1,9]

    instance = Solution()
    solution = instance.findUnsortedSubarray(nums)
    print(solution)
