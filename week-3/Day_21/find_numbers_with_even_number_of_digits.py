class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        output = 0
        for num in nums:
            if len(str(num)) % 2 == 0:
                output +=1
        return output


if __name__ == '__main__':

    nums = [555,901,482,1771]
    instance = Solution()
    solution = instance.findNumbers(nums)

    print(solution)
